def productOfAll(*numbers):
    count = 0
    for n in numbers:
        count += 1

    if count == 0:
        return 1
    else:
        result = 1
        for num in numbers:
            result *= num
        return result

print(productOfAll(1, 3, 5, 7, 9, 11))
