def calc(num):
    try:
        num = 1 / num
        print(num)
    except ZeroDivisionError:
        print("You cabbot divide by zero.")
    else:
        print("All good")
    finally:
        print("Done with calc!")

calc(0)
calc(10)
