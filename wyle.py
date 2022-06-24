# x = int (input('Input the number: '))
# count =  0
# y = 1
# while count < x:
#     count += 1
#     y *= count
#     print(count, ': ', y)
#     # print( y )

m = 'zalupa dadada'
b  = [22,21,1,51]
a = []
b.copy()
for i in b:
    print(b.index(i), ': ', i)

# print(b)
print("total number of 22: ", b.count(22))
# total number

print("NON sorted: ", b) 
# default array

newdict = b.copy()

b.sort()
b.append('privet')
print("sorted: ", b)
# printing sorted array

print("lets see: ", newdict)
# 
cor = tuple('zalupa!')
print("cortezh: ",cor)

ccc = (1,2,3,24)
cc2 = []
cc2.append(ccc)
print("cor2:", cc2)

# range(len(b))
# print(len(b))
for i in range(len(ccc)):
    a.append(ccc[i])
print(a)
