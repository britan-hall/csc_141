guests = ["steve", "bob", "sally", "donald", "ryan", "louis"]

print("I can now only invite 2 people to dinner, so 4 people have to go.")

for number in range (0,4):
    popped_guests = guests.pop(0)
    print(f"Sorry {popped_guests.title()}, you are no longer invitied.")

for number in range (0,2):
    print(f"Don't worry {guests[number].title()}, you can still come to dinner.")
    
guests.remove("ryan")
guests.remove("louis")
print(guests)