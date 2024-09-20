names = ["lewis", "mark", "jarred"]

def message(count):
    phrase = f"Hey {names[count].title()}!"
    print(phrase)

for count in range (0,3):
    message(count)
