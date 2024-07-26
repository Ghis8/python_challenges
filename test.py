#! /usr/bin/python3
import decimal
 
name="Ghislain"
#print(name.count('i'))
#print(name.find("i"))
#print(name.isalnum())
#print(name.join('t'))
#print(name.split(',',1))

#for i in name:print(i)
#print(list(name))
#print(list(range(0,100)))
#l=range(0,11)
#square=[i**2 for i in l]
#print(square)

#def f1(x): return x*2
#def f2(x): return x*4

#lst=[]

"""
for i in range(16):
	lst.append(f1(f2(i)))
"""
# comprehensible way to explain the loop above
#print([f1(x) for x in range(64) if x in [f2(j) for j in range(64)]])
#print: [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]
#list1=[list(range(1,4))]
#list1.extend([list(range(4,7))])
#result=[i*j for i in list1[0] for j in list1[1]]
#print(set(result))

#result=list(map(lambda x:x **2,list(range(1,5))))
#divisibleByTwo=list(filter(lambda x:x%2==0,list(range(101))))
#print(divisibleByTwo)
#gen=(i**2 for i in list(range(1,5)))
#for i in gen:print(i)
#x=1
#y="1"
#print(x == y)
#a=3+5j
#print(a.real)

x=decimal.Decimal(3.14); y=decimal.Decimal(2.7)
result=decimal.getcontext().prec=4
print(x*y)
