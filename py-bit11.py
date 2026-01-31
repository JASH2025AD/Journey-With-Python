def f(x):
    try:
        if x==0:
            raise ValueError
        print("ok")
    except ValueError:
        return "caught"
    else:
        return "no-except"
    finally:
        print("in-finally")
print(f(1))
print(f(0))            