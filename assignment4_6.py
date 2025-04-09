def computepay():
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r=float(rate)
    if h <= 40:
        x = h*r
    else:
        x =((h-40)*r*1.5)+r*40
    
    return x

p = computepay()  
     
print("Pay", p)