# distance between two co-ordinate points
print("point1")
x1 = eval(input("Enter co-ordinate point x1:"))
y1 = eval(input("Enter co-ordinate point y1:"))
print('---------------------------------------------------------------------------------------------------------------')
print('point2')
x2 = eval(input("Enter co-ordinate point x2:"))
y2 = eval(input("Enter co-ordinate point y2:"))
print('---------------------------------------------------------------------------------------------------------------')
Distance = ((x2-x1)**2 - (y2-y1)**2)**0.5
print('(',x1,y1,')','(',x2,y2,')=',Distance)