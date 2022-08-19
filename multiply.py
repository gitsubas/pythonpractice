def multiply(*arguments):
    product = 1
    for num in arguments:
        product *= num
    print(product)
multiply(1, 4, 6, 3)
