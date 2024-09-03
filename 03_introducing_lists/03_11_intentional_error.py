businesses = ["samsung", "microsoft", "apple", "microsoft", "sony"]

#This would cause an error because there is no element in the 5th index of the list.
#This is becaues every list's index starts at 0 instead of 1
print(businesses[5])

#To print the final element of a list you can figure out its index by counting
print(businesses[4])
#Or using the index "-1" to go to the last element of a list
print(businesses[-1])