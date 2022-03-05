def f(x, y):
    return (x**2 - 4*x + y**2 - y - x*y)

a1 = 2.5
b1 = 3.5
a2 = 1.5
b2 = 2.5
ep = 0.000001
tau = (5**0.5-1)/2

k = 0
x1= a1+(1-tau)*( b1- a1)
x2= a1+(tau)*( b1- a1)
y1= a2+(1-tau)*( b2- a2)
y2= a2+(tau)*( b2- a2);

ek=[x1,y1]
fk=[x1,y2]
hk=[x2,y1]
gk=[x2,y2]

fek=f(x1,y1)
ffk=f(x1,y2)
fhk=f(x2,y1)
fgk=f(x2,y2); 


while ((b1-a1)**2 + (b2-a2)**2)**0.5 > ep:
    k=k+1
    min1=min([fek,fhk,ffk,fgk])
    if min1==fek:
        b1=x2
        b2=y2
    elif min1==ffk:
        b1=x2
        a2=y1
    elif min1==fgk:
        a1 =x1
        a2 =y1
    elif min1==fhk:
        a1=x1
        b2 =y2
    x1= a1+(1-tau)*( b1- a1)
    x2= a1+(tau)*( b1- a1)
    y1= a2+(1-tau)*( b2- a2)
    y2= a2+(tau)*( b2- a2)
    fek=f(x1,y1)
    ffk=f(x1,y2)
    fhk=f(x2,y1)
    fgk=f(x2,y2)
    min1=min([fek,fhk,ffk,fgk])
        
if min1==fek:
    print(f'minimum at the point {x1}, {y1}')
elif min1==ffk:
    print(f'minimum at the point {x1}, {y2}')
elif min1==fhk:
    print(f'minimum at the point {x2}, {y1}')
elif min1==fgk:
    print(f'minimum at the point {x2}, {y2}')
print(f'minimum value {min1}')
print(f'number of iterations {k}')