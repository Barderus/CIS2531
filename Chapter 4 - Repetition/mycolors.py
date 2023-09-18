count = 0

while True:
    first_name = input("Enter your first name (Enter DONE to quit):  ")
    if first_name == "DONE":
        break
    count += 1
print(f"You entered {count} student first names")