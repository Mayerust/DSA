class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge array into a hash map for O(1) average lookup time
        lookup = {key: val for key, val in knowledge}
        
        result = []
        key_buffer = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(key_buffer)
                # Replace with knowledge value if key exists, otherwise '?'
                result.append(lookup.get(key, "?"))
                key_buffer.clear()
            elif in_bracket:
                # Accumulate characters belonging to the key name
                key_buffer.append(char)
            else:
                # Accumulate standard output characters
                result.append(char)
                
        return "".join(result)