beverages = set({"coffee", "tea", "juice"})
print(type(beverages))
print(beverages)

#Qn 2
beverages.add("coca cola")  #way to simplify this
beverages.add("sprite")
print(beverages)

#Qn 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

#Qn 4
mySet.remove("kettle")
print(mySet)

#Qn 5
for x in mySet:
    print(x)
    
#Qn 6
myset = {1, 2, 3, 4}
mylist = ["apple", "mango"]
myset.update(mylist)
print(myset)

#Qn 7
ages = {12, 35, 56, 78}
firstnames = {"Judith", "Hilda", "Lydia"}
set1 = ages.union(firstnames)
print(set1)