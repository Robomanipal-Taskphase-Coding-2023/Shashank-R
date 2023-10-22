def distance(x1, y1, x2, y2): 
    return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
print("Distance Between Two Points!")
  
x1=float(input("Enter the X1 co-ordinate: "))
x2=float(input("Enter the X2 co-ordinate: "))
y1=float(input("Enter the Y1 co-ordinate: "))
y2=float(input("Enter the Y2 co-ordinate: "))
  
print( distance(x1, y1, x2, y2))
