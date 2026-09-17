a = int(input("Enter your first number (a):"))
b = int(input("Enter your second number (b):"))
c = int(input("Enter your third number (c):"))
if a==b==c:
    print("all of them are equal")
elif a==b and b>c:
    print("a and b are the greatest")
elif a==c and c>b:
    print("a and c are the greatest")
elif c==b and b>a:
    print("c and b are the greatest")
elif a==b and b<c:
    print("c is the greatest")
elif a==c and a<b:
    print("b is the greatest")
elif b==c and a>c:
    print("a is the greatest")
elif a>b>c:
    print("a is the greatest")
elif a>c>b:
    print("a is the greatest")
elif c>b>a:
    print("c is the greatest")
elif c>a>b:
    print("c is the greatest")
elif b>a>c:
    print("b is the greatest")
else:
    print("b is the greatest")
