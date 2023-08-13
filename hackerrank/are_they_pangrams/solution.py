def isPangram(pangram):
    # Write your code here
    result = ""
    for string in pangram:
        if len(set([char for char in string.lower() if char != " "])) == 26:
            result += "1"
        else:
            result += "0"
    print(result)
    return result
