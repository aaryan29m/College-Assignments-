#lists--lists are ordered,mutable,duplicate allowing data set in python
students = ["Abhiraj","Sumedh","Kushagra","Vaidic","Naman","Aadidev","Sehajveer"]
#adds "not a student" to the end of the list
students.append("not a student")
print(students)
"""removes the specified index very simalar to del keyword however del uses [] insead of ()
also similar to the remove keyword but instead of specifying index we specify the item name itself"""
students.pop()
print(students)
#sorts the list in alphanumeric order,the default is ascending order
students.sort()
print(students)
#sorts the list in descending order
students.reverse()
print(students)
#copies the list
classmates = students.copy()
print(classmates)


#tuples--tuples are ordered ,immutable,duplicate allowing data set in python
car_brand = ("Mercedes","Audi","Volvo","BMW","Maserati","Porsche","BMW","Honda","Mercedes","Maserati","Bugatti","Honda","Honda")
#gives the output of no. of times the item is in tuple
print(car_brand.count("Honda"))
#gives the output of the least index the item is occupying
print(car_brand.index("Maserati"))
#length of the tuple
print(len(car_brand))
#unpacking a tuple
(green,yellow,red,violet,blue,orange,indigo,pistacio,pink,brown,black,purple,hotpink) = car_brand
print(green)
print(yellow)
print(red)
print(violet)
print(blue)
print(orange)
print(indigo)
print(pistacio)
print(pink)
print(brown)
print(black)
print(purple)
print(hotpink)
#joining a tuple using an addition operator
tyres = ("Michelin","Pirelli","Bridgestone","Continental","MRF")
tyres_shop = car_brand + tyres
print(tyres_shop)


#dictionary -Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates

car_shop = {"Car_Model":"M5","Brand":"BMW","tires":"pirelli","color":"blue"}
#this will display all the keys
print((car_shop).keys())
#this will get all the values
print((car_shop).values())
#this will get all the items
print((car_shop).items())
#this will overwrite the color, we can also write car_shop.update({"color":"black"}) to get the same output
car_shop["color"]="black"
print(car_shop)
