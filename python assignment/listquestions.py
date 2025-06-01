#Qn 1
mylist = ["John", "Edrine", "Godfrey", "Edna", "Joyce"]
print(mylist[1])

#Qn 2
mylist[0] = "Leticia"
print(mylist)

#Qn 3
mylist.append("Baily")
print(mylist)

#Qn 4
mylist.insert(2, "Bathel")
print(mylist)

#Qn 5
mylist.pop(3)
print(mylist)

#Qn 6
mylist = mylist[-1]
print(mylist)

#Qn 7
newlist = [1, 2, 7, 5, 9, 10, 6] 
print(newlist[2:5])

#Qn 8
countries = ["Uganda", "Kenya", "Rwanda"]
newlist = countries.copy()
print(newlist)

#Qn 9
for x in countries:
    print(x)

    
#Qn 10
names = ["dog", "cat", "rabbit", "cow"]

names.sort()
print(names)  #ascending

names.sort(reverse = True)  #descending
print(names) 


#Qn 11
newlist = []
for x in names:
    if "a" in x:
        newlist.append(x) 
print(newlist)


#Qn 12
firstnames = ["Judith", "Mary"]
secondnames = ["Kemirembe"]
print(firstnames + secondnames)
