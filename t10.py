userInput = input("Введіть дані: ")

partInput = userInput.split(", ")

name = partInput[0].split(": ")[1].strip('"')
age = partInput[1].split(": ")[1].strip('"')
city = partInput[2].split(": ")[1].strip('"')

text1 = "{}, якому {} рік, проживає у місті {}.".format(name, age, city)

text2 = f"{name}, якому {age} рік, проживає у місті {city}."

print(text1)
print(text2)
