#lists
#you can add and remove features in list, making it 'mutable'
features = ["login", "signup", "dark mode"]
features.append("AI") #gotta stay relevant
print(features)
print(features[0]) #prints the first element of the list
print(features[-1]) #prints the last. Negative indexing ftw

features.remove("signup") #removes that first occurrence of "signup" from the list
print(features)

del features[1] #removes the second element
print(features)

#Slicing
startup_ideas = ["Uber for dogs", "Tinder for cats", "AI Powered food delivery", "Robinhood for NFCs"]
print(startup_ideas)

feasible_ideas = startup_ideas[1:3] #elements from indeces 1 to 2
print(feasible_ideas)

#iterating through the list
for idea in startup_ideas:
    print(f"Pitching {idea}")

#another example of using lists

essential_gadgets = ["samsung watch", "pixel pro phone", "3D Printer", "EBooks"] #initializing a list
print(essential_gadgets)
#adding elements:
essential_gadgets.append("Tesla")
essential_gadgets.append("Humanoid")
print(essential_gadgets)

#deleting at a particular index
del essential_gadgets[1]
print(essential_gadgets)

#print the first 3 gadgets in the list
print(essential_gadgets[0:3])

essential_gadgets.append("Tesla")
print(essential_gadgets)

#remove all occurrences of "Tesla"
while "Tesla" in essential_gadgets:
    essential_gadgets.remove("Tesla")

print(essential_gadgets)

#tuples
#these are immutable, meaning you can't add, remove, or modify the elements.
investors = ("A16z", "YC", "Soft Bank")

prog_langs = ("Python", "Java", "Julia")
print(prog_langs[1])

#listOfTuples
snacks_with_prices = [("lays",10), ("parleG", 15), ("boomer", 5)]
#we can now make this into a dictionary, with key-value pairs
snacks = dict(snacks_with_prices)
print(snacks)

snacks['cake']= 25 #adding a new key-value pair to the dictionary
print(snacks)