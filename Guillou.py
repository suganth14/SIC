import random
import sympy
import math

p = sympy.randprime(1,2**10)
q = sympy.randprime(1,2**10)
n = p * q
phi = (p-1) * (q-1)

print("P : ", p)
print("Q : ", q)
print("n : ", n)
print("phi : ", phi)

e = random.randrange(2,n-2)

while(math.gcd(e,phi)!=1):
    e = random.randrange(2,n-2)
    
print("E : ",e)
s = random.randrange(2,n-2)
v = None
while(v == None):
    try:
        s = random.randrange(2,n-2)
        t = s**e
        v = pow(t, -1, n)
        print(v)
    except ValueError:
        v = None
 
print("V", v)        
r = random.randrange(2,n-2) 
x = r**e % n
print("x", x)
c = random.randrange(1,e)
y = (r*(s**c)) % n
print("y", y)

check = (y**e) * (v**c) % n

print("Check value:", check)
if check == x:
    print("Probable")
else:
    print("Improbable")


