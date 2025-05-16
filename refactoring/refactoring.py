def S(d):return sum(d)
def P(n):
 if n<2:return False
 for i in range(2,n):
  if n%i==0:return False
 return True
class A:
 def __init__(s,x,y):s.x=x;s.y=y
 def D(s):return s.x*s.y
 def __str__(s):return f"{s.x},{s.y}"

def X(a):
 b=[]
 for i in a:
  if i%2==0:b.append(i)
 return b

def Y(s):
 w=0
 for c in s:
  if c.isupper():w+=1
 return w

def Z(l):
 m=l[0]
 for v in l:
  if v>m:m=v
 return m

def Q(a,b):
 c=0
 while b>0:
  a,b=b,a%b
 return a

def R(s):
 return s[::-1]

def T(n):
 if n==0:return 1
 else:return n*T(n-1)

def U(lst):
 r=[]
 for i in lst:
  if i not in r:r.append(i)
 return r

def V(s):
 d={}
 for c in s:
  if c in d:d[c]+=1
  else:d[c]=1
 return d

def W(a,b):
 return [x for x in a if x in b]

def J(n):
 f=1
 for i in range(1,n+1):f*=i
 return f

def K(s):
 return s.lower().replace(" ","")

def L(n):
 return [i for i in range(n) if i%2!=0]

def M(m):
 return [[0]*m for _ in range(m)]

def N(lst):
 return [x for x in lst if x>0]

def O(s):
 return sum(1 for c in s if c.isdigit())

def G(a,b):
 return a if a>b else b

def H(s):
 return s==s[::-1]

def I(n):
 return str(n)==str(n)[::-1]

def C(temp):
 return (temp*9/5)+32

def D(f):
 return (f-32)*5/9

def E(s):
 v=['a','e','i','o','u']
 return sum(1 for c in s.lower() if c in v)

def F(s):
 return ''.join(c for c in s if c.isalnum())

def _():
 print("Это пустая функция")

x1=10
x2=20
x3=x1+x2
print(x3)

lst1=[1,2,3,4,5]
lst2=[x*2 for x in lst1]
print(lst2)

dct={'a':1,'b':2}
print(dct.get('a'))

s="HeLLo WoRLd"
print(Y(s))






a=5
b=10
print(G(a,b))
s="racecar"
print(H(s))
n=12321
print(I(n))
temp=25
print(C(temp))
s="Python is cool!"
print(E(s))
pt=A(3,4)
print(pt.D())
print(pt)


x=42
y=7
print(Q(x,y))

s="abcba"
print(R(s))

num=5
print(T(num))

lst=[1,2,2,3,3,3]
print(U(lst))

s="hello"
print(V(s))

a=[1,2,3]
b=[3,4,5]
print(W(a,b))

n=4
print(J(n))

s="  HELLO  "
print(K(s))

n=10
print(L(n))

m=3
print(M(m))

lst=[-1,0,1,2]
print(N(lst))

s="a1b2c3"
print(O(s))

_()
