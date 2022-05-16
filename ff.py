import random
import sympy
import math

k=3

p = sympy.randprime(2**7,2**8)
q = sympy.randprime(2**7,2**8)
n = p * q
print("P:" , p)
print("Q:" , q)
print("n:" , n)
s=[]
v=[]


for i in range(k):
    temp = random.randrange(2,n-2)
    temp1 = None
    while(temp1 == None):
        try:
            while(math.gcd(temp,n)!=1):
                temp = random.randrange(2,n-2)
            t = temp**2
            temp1 = pow(t, -1, n)
        except ValueError:
            temp1 = None
    s.append(temp)
    v.append(temp1)
    

print("S:", s)
print("V:", v)

r = random.randrange(1,n-1)
x = r**2 % n
c=[]
for i in range(k):
    c.append(random.randrange(0,50))

y = r
for i in range(k):
    y*=(s[i]**c[i])

y = y % n

print("x:", x)
print("y:", y)

check = y**2
for i in range(k):
    check *= (v[i]**c[i])
check = check % n
    
print("Check Value:", check)

if check == x:
    print("Probable")
else:
    print("Improbable")
