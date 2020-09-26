def fact(n):
    if (n<2):
        return 1
    return fact(n-1)*n;


while True:
    print("Factorial is ",fact(int(input("Put in a number"))))
