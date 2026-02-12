def search(nested_list):
    searchfor = input("Введіть елемент для пошуку: ")
    isfound = False

    for sublist in nested_list:
        for item in sublist:
            if str(item) == searchfor:
                isfound = True
                break
        if isfound:
            break

    if isfound:
        print(f"Елемент '{searchfor}' знайдено.")
    else:
        print(f"Елемент '{searchfor}' не знайдено.")

myList = [[1, 2, 3], ["Львів", "Київ", "Одеса"], [4, 5, 6]]
search(myList)
