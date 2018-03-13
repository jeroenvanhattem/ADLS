import opdracht_2

valid = {
	"(" : ")",
	"[" : "]",
	"{" : "}",
	"<" : ">"
}

def check_brackets(value):
    """
    Description
    This function requires you to push a list of brackets to the stack. When you did that, you'll have to check the stack using the check() function
    
    Parameters
    ----------
    brackets_to_push	:	List
        A list containing several brackets
        
    Return
    ------
    Feedback	:	String
        If the passed list is all right, a True value will be returned
        If the passed list contains invalid characters, a False value and a message will be returned
        If the passed list contains an invalid use of brackets, the current stack will be returned
    
    Example
    -------
    #value = ['(',')']
    return = True
    """
    bracket_stack = opdracht_2.stack()
    for given in value:
        if given in valid.keys():
            bracket_stack.push(given)
        elif given in valid.values():
            for x in valid.values():
                if given == x:
                    bracket_stack.pop()
        else:
            print(given + " is not allowed | Return: ", end=" ")
            return False

    if bracket_stack.is_empty():
        return True
    else:
        # print(bracket_stack.peek())
        print("It goes wrong at: " + str(bracket_stack.peek()))
        return str(bracket_stack.peek())




# First test
print("Test 1: ", end="")
brackets_to_push = ['<', '(', ')','>']
result = check_brackets(brackets_to_push)
print(result)


# Second test
print("Test 2: ", end="")
brackets_to_push = ['<', '(', 'a','>']
result = check_brackets(brackets_to_push)
print(result)


# Third test
print("Test 3: ", end="")
brackets_to_push = ['<', '(', '(','>']
result = check_brackets(brackets_to_push)
print(result)