import imp


import os

folder = os.walk('Z:\\Новая папка')
newAr = []

def show():
    for ad, dir, file, in folder:
        newAr.append(file)
    print(newAr)
# show()

def newFunc(arr1, arr2):
    return arr1+arr2

newArr = newFunc(2,3)
print(newArr)