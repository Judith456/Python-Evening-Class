"""
           WHILE Loop
i = 1
while i < 10:
    print(i)
    if i == 4:
        break   
    i += 3

    
#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
"""

                  #FOR LOOP
"""
fruits = ["apples", "oranges", "lemons"]                
for i in fruits:
    print(i)


for x in "banana":
    print(x)

    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":     #exit the loop when x is equal to banana 
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  int(x)

 
for x in range(1, 10, 2):
    print(x)
else:
    print("Number nolonger in the range")

    
for x in range(6):
  
  if x == 4:
      continue
  print(x)
else:
  print("Finally finished!")

  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
"""

while True:
    try:
        # Ask user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Try division
        result = num1 / num2

    except ValueError:
        # Handles non-numeric input
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        # Handles division by zero
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        # If no exceptions occur
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit the loop if successful

  
