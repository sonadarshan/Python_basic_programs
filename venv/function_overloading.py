def check():
    print("Checking")

def check(a):
    print(a*5)

def check1(val=0):
    if val > 0:
        return val*5
    return val
print (check1(9))