def evenDetector(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            result.append("парне")
        else:
            result.append(numbers[i])
    print(result)
    return result

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenDetector(testList)
