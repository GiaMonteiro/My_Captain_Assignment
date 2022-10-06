# Write in NB.
# Whenever dealing with elements, we use the first method.
# Whenever we are dealing with indexes, we use the second method.

n=int(input("How many terms: "))
a=0
b=1
c=1
print(a,b,c,end=" ")
for i in range(4,n+1):
    d=a+b+c
    print(d,end=" ")
    a=b
    b=c
    c=d

