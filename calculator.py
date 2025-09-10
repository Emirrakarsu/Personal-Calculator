def cal(x, y):
    add = x + y
    sbs = x - y
    dvd = x / y
    mlt = x * y
    exp = x ** y
    prcss = add, sbs, dvd, mlt, exp
    return prcss

while True :
    prc1 = float(input("Please enter a number\n__"))
    prc2 = float(input("Please enter a number\n__"))

    choice = input("What would you do\n ( add / sbs / dvd / mlt / exp / q)")

    try :
        if choice == 'add':
            print(prc1 + prc2)
        elif choice == 'sbs':
            print(prc1 - prc2)
        elif choice == 'dvd' :
            print(prc1 / prc2)
        elif choice == 'mlt' :
            print(prc1 * prc2)
        elif choice == 'exp' :
            print(prc1 ** prc2)
        elif choice == 'q' :
            break
    except ValueError:
        print("Unfortunately you had a {' ValueError'} !!")
    except TypeError:
        print("Unfortunately you had a {' TypeError'} !!")



    


