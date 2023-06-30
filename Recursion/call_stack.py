
def Three():
    print("Three")


def Two():
    Three()
    print("Two")

def One():
    Two()
    print("One")

One()