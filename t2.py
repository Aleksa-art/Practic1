def half(string):
    result = ""
    halfLen = len(string)//2 + (len(string)%2)

    for i in range(halfLen):
        result += string[i]

    print(result)
    return result

half(input())
