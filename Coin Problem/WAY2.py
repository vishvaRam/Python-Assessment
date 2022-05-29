def curramount(amount):
    currency = [1000, 500, 100, 50, 20, 10, 5, 1]
    output = {}

    for i in currency:
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            output[i] = j

    for k, v in output.items():
        print(f'{k} : {v}')




curramount(590)
