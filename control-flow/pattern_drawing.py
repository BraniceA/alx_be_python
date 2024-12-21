# Making a square out of asteriscs
size = int(input("Enter the size of the pattern:"))
while size:
    for j in range(size):
        for j in range(size):
            print("*", end=" ")
        print()
    break
