"""
Formula 
step -1
    calulate semi-perimeter 
    s = a + b + c / 2
    where a, b, c are side of trangle
    
step - 2
    calculate area of trangle 
    area =  (s * (s-a) * (s-b)* (s-c) ) ** 0.5 

"""

a = 10
b = 10
c = 10

s = a + b + c / 2
area =  (s * (s-a) * (s-b)* (s-c) ) ** 0.5 

print("area of trangle :", int(area))


x = 10
y = 20

x, y = y,x

print("value of x",x)
print("value of y",y)