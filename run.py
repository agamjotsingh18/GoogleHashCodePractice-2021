def process_input(processedInput):
    totalPizza, twoMembers, threeMembers, fourMembers = tuple(int(value) for value in processedInput[:4])
    pizzaTypes = processedInput[4]
    print(totalPizza, twoMembers, threeMembers, fourMembers, pizzaTypes)

def fetch_input():
    pizzaTypes = []
    firstLine = input().strip()
    if firstLine:
        totalPizza, twoMembers, threeMembers, fourMembers = firstLine.split(' ')
    for line in iter(input, ''):
        pizzaTypes.append(line)
    return (totalPizza, twoMembers, threeMembers, fourMembers, pizzaTypes)
    
if __name__ == "__main__":
    processedInput = fetch_input()
    process_input(processedInput)