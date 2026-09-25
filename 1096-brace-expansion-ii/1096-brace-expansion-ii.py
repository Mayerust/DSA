class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def combine(term_sets: list[set[str]]) -> set[str]:
            res = {""}
            for s in term_sets:
                res = {a + b for a in res for b in s}
            return res
        def parse(expr: str) -> set[str]:
            groups = []
            current_term = []
            i = 0
            n = len(expr)
            while i < n:
                if expr[i] == '{':
                    j = i
                    level = 0
                    while j < n:
                        if expr[j] == '{':
                            level += 1
                        elif expr[j] == '}':
                            level -= 1
                            if level == 0:
                                break
                        j += 1
                    inner_set = parse(expr[i + 1 : j])
                    current_term.append(inner_set)
                    i = j + 1
                elif expr[i] == ',':
                    groups.append(combine(current_term))
                    current_term = []
                    i += 1
                else:
                    current_term.append({expr[i]})
                    i += 1
            if current_term:
                groups.append(combine(current_term))
            ans = set()
            for group in groups:
                ans.update(group)
            return ans
        return sorted(list(parse(expression)))