# We want to determine the height of a building of n floors, knowing that the ground floor has a height of 6 meters and
# that the other floors each have a height of 4 meters.

floor = int(input("Number of floors: "))
print("The building is: "+str(6+(floor*4))+str("m tall."))