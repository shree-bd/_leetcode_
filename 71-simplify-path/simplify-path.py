class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""


        for c in path + "/":
            if c == "/":                        # Slash marks the end of a directory name
                if curr =="..":                 # Handle 'go to parent directory'
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                # Reset the current directory name for the next one
                curr = ""
            else:
                # Build the current directory name character by character
                curr += c

        return "/" + "/".join(stack)

             
        