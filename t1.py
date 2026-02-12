def aochange(stringInput):
    result = ""

    for i in stringInput:
        if i == "а":
            result += "@"
        elif i == "о":
            result += "0"
        else:
            result += i
    print(result)
    return result

aochange(input())
