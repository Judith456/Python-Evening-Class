x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])
#Qn 2
print(x[-2])

#Qn 3
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)

#Qn 4
y = list(x)
y.append("Huawei")
x = tuple(y)
print(x)

#Qn 5
for a in x:
    print(a)
    
#Qn 6
y = list(x)
y.pop(0)
x = tuple(y)
print(x)

#Qn 7
cities = tuple(("Kampala", "Jinja", "Nansana", "Entebbe"))
print(type(cities))

#Qn 8
(green, *blue, red) = cities
print(green)
print(blue)
print(red)

#Qn 9
print(cities[1:5])

#Qn 10
firstnames = ("Judith", "Mary")
secondnames = ("Kemirembe",)
print(type(secondnames))
print(firstnames + secondnames)

#Qn 11
colors = ("red", "yellow", "green")
colors = colors*3
print(colors)

#Qn 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple.count('8')  #answer is wrong
print(thistuple)