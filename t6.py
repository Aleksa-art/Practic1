rowSet = int(input("Кількість рядків: "))
columnSet = int(input("Кількість стовпців: "))

matrix = []
for i in range(rowSet):
    row = list(map(int, input(f"Елементи для рядка {i+1}: ").split()))
    if len(row) != columnSet:
        print("Error")
        exit()
    matrix.append(row)

transposed = []
for j in range(columnSet):
    new_row = []
    for i in range(rowSet):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

for row in transposed:
    print(" ".join(map(str, row)))
