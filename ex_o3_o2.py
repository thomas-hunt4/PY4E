score=input('Enter Score: ')
try:
    s=float(score)
except:
    print("number numbers not letter numbers my friend")    


if s >=0.9:
    print('A')
elif s >=0.8:
    print('B')
elif s >=0.7:
    print('C')
elif s >=0.6:
    print('D')
elif s <0.6:
    print("F")    


