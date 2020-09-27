from random import randint

def shuffle(arr):
    temp = []
    while len(arr) > 0:
        index = randint(0,len(arr)-1)
        temp.append(arr[index])
        del arr[index]
    return temp

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

while True:
    counter = 0
    #ask for number of elements
    num = int(input("How many elements to sort? "))
    arr = [*range(0, num)]
    arr = shuffle(arr)
    while not isSorted(arr):
        arr = shuffle(arr)
        print("Trying ",arr)
        counter = counter + 1
    print("Finished",arr," in ",counter)
