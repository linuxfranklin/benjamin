import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lengthOfNames=len(names)
print(lengthOfNames)
r=random.randint(0,lengthOfNames-1)
print(f"Today {names[r]} have to buy meals")