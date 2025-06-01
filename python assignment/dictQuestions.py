#Qn 1
Shoes = {
	"brand" : "Nick",
	"color" : "black",
	"size" : 40
	}
print(Shoes["size"])

#Qn 2
Shoes["brand"] = "Adidas"
print(Shoes)

#Qn 3
Shoes["type"] = "sneakers"
print(Shoes)

#Qn 4
x = Shoes.keys()
print(x)

#Qn 5
y = Shoes.values()
print(y)

#Qn 6
print("size" in Shoes)

#Qn 7
for z in Shoes.items():
    print(z)

#Qn 8
Shoes.pop("color")
print(Shoes)

#Qn 9
Shoes.clear()
print(Shoes)

#Qn 10
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964} 
newdict = mydict.copy()
print(newdict)

#Qn 11
myfamily = {
    "child1" : {
        "name" : "Alice",
        "age" : 34
    },
    "child2 ": {
        "name" : "Janet",
        "age" : 45
    },
    "child3" : {
        "name" : "Bob",
        "age" : 24
    }
}
