x=int(input('first: '))
x2=int(input('second: '))
x3=int(input('third: '))

if x==x2 and x2==x3:
    print('3')
elif x==x2 or x2==x3 or x3==x:
    print('2')
else:
    print('0')