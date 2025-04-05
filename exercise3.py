hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r=float(rate)

if h <= 40:
    pay = h*r
elif h > 40:
     pay=((h-40)*r*1.5)+r*40

print(pay)

