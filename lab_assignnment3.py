def my_function(a,b,c):
    list = [a,b,c]
    list.sort()
    side1=list[0]
    side2=list[1]
    side3=list[2]
    if side1<=0 or side1+side2==side3:
        print("not a valid triangle")
    elif side1**2+side2**2 == side3**2:
        print("right angled triangle")
    else:
        print("not a valid triangle")
my_function(3,4,5)
my_function(0,0,2)
my_function(4,5,5)
my_function(3,1,2)

