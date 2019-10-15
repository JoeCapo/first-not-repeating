
def first_not_repeating(str):
    """
    Returns the first non-repeating character in the input string.
    Returns _ if no non-repeating character is found.
    """
    charList = []
    charCounter = {}

    for char in str:
        if char in charCounter:
            charCounter[char] +=1
        else:
            charCounter[char] = 1
            charList.append(char)
    for char in charList:
        if charCounter[char] == 1:
            return char
    return "_" 