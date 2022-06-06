def calc(num):
    try:
        num = 1 / num
        print(num)
    except ZeroDivisionError:
        print("You cabbot divide by zero.")
    else:
        print("All good")

calc(0)
calc(10)
