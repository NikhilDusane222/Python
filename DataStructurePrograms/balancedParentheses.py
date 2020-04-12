open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

#Function to check parentheses
def check(mystr):
    stack = []
    for i in mystr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"

string = input("Enter an Arithmetic Expression:")
if (check(string)):
    print(string, "Valid Expression")
else:
    print(string, "Invalid Expression")