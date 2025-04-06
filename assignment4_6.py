def computepay(x):
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r=float(rate)
    if h <= 40:
        x = h*r
    elif h > 40:
        x =((h-40)*r*1.5)+r*40
    return x

p = computepay(1)  
     
print("Pay", p)