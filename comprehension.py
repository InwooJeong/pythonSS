# myList = []
# for i in range(1,11):
#     myList.append(i)

# print(myList)

myList = [i*100 for i in range(1,11) if i % 2 == 0]
print(myList)

myList = [i for i in range(1,11)]
myDict = {i:i for i in myList}
print(myDict)

keys = ['kor','eng','math']
values = [90,100,100]
score = {keys[i]:values[i] for i in range(len(keys))}
print(score)

doe = {'kor':100,'eng':90,'math':90}
getKeys = [key for key in doe]
getValues = [value for value in doe.values()]
print(getKeys)
print(getValues)

myKeys = [key for key,value in doe.items()]
myValues = [value for key,value in doe.items()]
print(myKeys)
print(myValues)