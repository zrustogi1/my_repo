lst=[10,20,30,40,50]

lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(50)
print(lst)
lst.pop(4)
print(lst)
lst.pop()
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

newlst=lst[1:]
print(newlst)

lst.append(20)
lst.append(20)
print(lst)

count20=lst.count(20)
print(count20)

index20=lst.index(20)
print(index20)

cpylst=lst
cpylst[0]=999
print(cpylst)
print(lst)

cpylst=lst.copy()
cpylst=lst[:]
cpylst[-1]=999
print(cpylst)
print(lst)


empty=[]
print(empty)
for val in lst:
    if val >= 20 and val <= 50:
        empty.append(val)
print(empty)

empty=[0] * 10
print(empty)
empty[0]=99
print(empty)

squares=[]
for i in range(1,9):
    squares.append(i*i)
print(squares)

squares=[i*i for i in range(1,9)]
print(squares)
newlst=[val for val in lst if val>=20 and val<=50]
print(newlst)

aset=set()
aset={1,2,3,4,3,3,3}
print(aset)
aset.add(40)
print(aset)
#print(aset[0])

fav_foods={"kathleen": 'pizza', 'steve':'burger', 'john':'steak',
           'michelle':'chicken','pat':'pizza'}
food=fav_foods['kathleen']
print(food)

if 'bob' in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob']='ice cream'
print(fav_foods)

for name, fav_food in fav_foods.items():
    print(name,fav_food)
