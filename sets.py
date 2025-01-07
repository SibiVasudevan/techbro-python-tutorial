#Sets
#These can be modified, but are unordered
founders= {"Elon", "Zuck", "Gates", "Elon"}
print(founders)

founders.add("Tim Apple")
print(founders)

#founders.remove("Bezon") throws error if not found
founders.discard("Bezos") #does not throw an error
print(founders)

#set operations
team_a = {"Elon", "Jobs", "Theil", "Gates"}
team_b = {"Gates", "Zuck", "Pichai"}

print(team_a | team_b) #union
print(team_a & team_b) #intersection
print(team_a - team_b) #difference (elements that are in a but not in b)
print(team_a ^ team_b) #symmetric difference

#cleaning up duplicates in lists by making sets
emails = ["elon@420.com", "zuck@fb.com", "elon@420.com"]
unique_emails = set(emails)
print(emails)
print(unique_emails)