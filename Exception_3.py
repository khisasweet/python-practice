try:
    x = int(input("Enter a number: "))
    y = 1 /x
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except:
    print("Something else went wrong")

print("All done!")  
