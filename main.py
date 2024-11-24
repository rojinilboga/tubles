# Creating tuples
my_tuple = ("basketball","football","hockey")
print(my_tuple)

# Packing in tuples
sport_tuple = ("I","love","ice","skating")
for sport in sport_tuple:
    print(sport,end=" ")

# Unpacking in tuples
names = ("Rojin","Max","Mathew","Ivy","Rose")
name1, name2, name3, name4, name5 = names
print()
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)

# Tuple without brakets
tuple_names = "max", "banit", "louie"
print(tuple_names)