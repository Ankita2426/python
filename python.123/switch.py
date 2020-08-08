def one():
    return "sunday"
def two():
    return "monday"
def three():
    return "asdsddf"
def four():
    return "qwerr"
def num(a):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four
    }
    func = switcher.get(a)
    print(func)
    
