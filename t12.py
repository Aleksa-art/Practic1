i = int(input())
last = i
isTrue = True

while i != 0:
    i = int(input())
    if i != 0 and i <= last:  
        isTrue = False
    last = i

if isTrue:
    print("Так")
else:
    print("Ні")
