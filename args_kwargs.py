def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(100, 50, 25, galleons=105, sickles=55, knuts=30)

