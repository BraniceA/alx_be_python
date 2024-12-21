# Multiplication table
number = int(input("Enter a number to see its multiplication table:"))
# multiplys [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for multiply in range(1, 11):
    product = number * multiply
    print(f"{number} * {multiply} = {product}")
