def caseCounter(string):
    lower = 0 
    upper = 0
    
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    
    print("Великих літер:", upper, ", малих літер:", lower)
    return lower, upper

caseCounter(input())
