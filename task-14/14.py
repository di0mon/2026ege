for x in range(1,9431):
    num = int(f"39 ** 483 + 39 ** 235 - {x}",39)
    i = num.count("0")
    print(i)