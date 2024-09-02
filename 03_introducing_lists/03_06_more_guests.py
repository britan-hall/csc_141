guests = ["steve", "bob", "sally"]

for count in range (0,3):
    message = f"Hello {guests[count].title()}! You are invited to dinner tonight."
    print(message)

print("A bigger table has been found, we can invite 3 more guests!")

guests.insert(0, "donald")
guests.insert(3, "ryan")
guests.append("louis")

for count in range (0,6):
    message = f"Hello {guests[count].title()}! You are invited to dinner tonight."
    print(message)