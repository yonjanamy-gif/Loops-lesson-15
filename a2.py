for x in range(7777777777777777777):
    if x %20 == 0:
        print("twist")

    elif x % 15 == 0:
        pass

    elif x % 5 == 0:
        print("fizz")

    elif x % 7 == 0:
        print("buzz")
    else:
        print(x)