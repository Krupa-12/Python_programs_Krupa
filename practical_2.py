#
l=[5,4,3,2]
print(l)
print(type(l))
print("length",len(l))
l.append(1)
print("after append",l)
l.insert(1,6)
print("after insert:",l)
l.remove(6)
print("after remove:",l)
print("count of 3:",l.count(3))
l.sort()
print("after sorting:",l)
l.clear()
print("cleared list:",l)
l=[1,2,3,4,5]
l.pop(3)
print("after pop up:",l)
print("after reverse:",l)
print("length:",len(l))
print("slice",l[1:3])
print("odd no. present in the list:",l[::2])
print("last two second numbers:",l[-3:-1])
s={100,200,300}
l.extend(s)
print("after extending set:",l)

#output:
'''[5, 4, 3, 2]
<class 'list'>
length 4
after append [5, 4, 3, 2, 1]
after insert: [5, 6, 4, 3, 2, 1]
after remove: [5, 4, 3, 2, 1]
count of 3: 1
after sorting: [1, 2, 3, 4, 5]
cleared list: []
after pop up: [1, 2, 3, 5]
after reverse: [1, 2, 3, 5]
length: 4
slice [2, 3]
odd no. present in the list: [1, 3]
last two second numbers: [2, 3]
after extending set: [1, 2, 3, 5, 200, 100, 300]'''

t=(10,15,20,25,30)
print(type(t))
print("count of 50:",t.count(50))
print("index of 30:",t.index(30))
print("length",len(t))
print("slice",t[1:3])
print("odd no. present in the list:",l[::2])
print("last two second numbers",t[-3:-1])

#output:
'''<class 'tuple'>
count of 50: 0
index of 30: 4
length 5
slice (15, 20)
odd no. present in the list: [1, 3, 5]
last two second numbers (20, 25)'''

s={"a,b,c,d"}
print(type(s))
s.add("e")
print("after the addition of set:",s)
s.remove("e")
print("after the removine one ele. of set:",s)

#output:
'''<class 'set'>
after the addition of set: {'e', 'a,b,c,d'}
after the removine one ele. of set: {'a,b,c,d'}'''

d={'a':1,'b':2,'c':3,'d':4,'e':5}
print(type(d))
print(d)
print(d.keys())
print(d.values())
print(d.items())
d1=d.copy()
print("copy dictionary of d:",d1)
dn={'x':6,'y':7,'z':8}
d1.update(dn)
print("updated dictionary",d1)
print(d.get('b'))
d1.setdefault('w')
print("after set",d1)
d1.pop('w')
print("after pop",d1)

#output:
'''<class 'dict'>
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_keys(['a', 'b', 'c', 'd', 'e'])
dict_values([1, 2, 3, 4, 5])
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
copy dictionary of d: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
updated dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 6, 'y': 7, 'z': 8}
2
after set {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 6, 'y': 7, 'z': 8, 'w': None}
after pop {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 6, 'y': 7, 'z': 8}'''