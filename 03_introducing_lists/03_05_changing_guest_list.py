guests = ["joe", "bob", "sally"]

for count in range (0,3):
    message = f"Hello {guests[count].title()}! You are invited to dinner tonight."
    print(message)

print("Joe said cannot make the dinner, we should invite Steve instead.")

guests[0] = "steve"

for count in range (0,3):
    message = f"Hello {guests[count].title()}! You are invited to dinner tonight."
    print(message)

