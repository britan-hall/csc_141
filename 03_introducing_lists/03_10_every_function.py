businesses = ["samsung", "microsoft", "apple", "microsoft", "sony"]

#Using a list item in a sentence
print(f"I enjoy using {businesses[0].title()} products.")
#or setting an element to a variable 
name = businesses[0]
print(f"I enjoy using {name.title()} products.")

#Appending an element to the end of a list
businesses.append("lenovo")
print(businesses)

#Inserting an element to anywhere in the list
businesses.insert(2, "nvidia")
print(businesses)

#Using a the "pop" function to take items off of a list they can still be used elsewhere
popped_list = businesses.pop()
print(businesses)
print(popped_list)

#Sorting a list temporarily alphabetically 
print(sorted(businesses))
print(businesses)

#Sorting a list temporarily reverse alphabetically 
print(sorted(businesses, reverse=True))
print(businesses)

#Permanently reversing a list
businesses.reverse()
print(businesses)

#Permanently reversing the reversed list back to its original state
businesses.reverse()
print(businesses)

#Permanently sorting a list alphabetically
businesses.sort()
print(businesses)

#Permanently reverse sorting a list alphabetically
businesses.sort(reverse=True)
print(businesses)

#Prints the number of elements in the list
print(len(businesses))

