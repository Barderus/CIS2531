user_input = input("Enter a string: ")

digit_count = 0
uppercase_count = 0
lowercase_count = 0

for char in user_input:
    if char.isdigit():
        digit_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print("Number of digits:", digit_count)
print("Number of uppercase characters:", uppercase_count)
print("Number of lowercase characters:", lowercase_count)
