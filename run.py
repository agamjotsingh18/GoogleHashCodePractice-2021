def distribute_pizza(pizzaPriorty, processedInput):
    result = []
    pizzaPriortyPointer = 0
    totalPizza, twoMembers, threeMembers, fourMembers = tuple(int(value) for value in processedInput[:4])
    for _ in range(fourMembers):
        if ( pizzaPriortyPointer+4 <= totalPizza):
            result.append(('4', pizzaPriorty[pizzaPriortyPointer][0],
                            pizzaPriorty[pizzaPriortyPointer+1][0],
                            pizzaPriorty[pizzaPriortyPointer+2][0],
                            pizzaPriorty[pizzaPriortyPointer+3][0]))
            pizzaPriortyPointer = pizzaPriortyPointer + 4
    for _ in range(threeMembers):
        if ( pizzaPriortyPointer+3 <= totalPizza):
            result.append(('3', pizzaPriorty[pizzaPriortyPointer][0],
                            pizzaPriorty[pizzaPriortyPointer+1][0],
                            pizzaPriorty[pizzaPriortyPointer+2][0]))
            pizzaPriortyPointer = pizzaPriortyPointer + 3
    for _ in range(twoMembers):
        if ( pizzaPriortyPointer+2 <= totalPizza):
            result.append(('2', pizzaPriorty[pizzaPriortyPointer][0],
                            pizzaPriorty[pizzaPriortyPointer+1][0]))
            pizzaPriortyPointer = pizzaPriortyPointer + 2

    return result
def process_input(totalPizza, pizzaTypes):
    ingredientMap = {}
    for pizzaType in pizzaTypes:
        for ingredient in pizzaType.split(' ')[1:]:
                ingredientMap[ingredient] = ingredientMap.get(ingredient, 0) + 1
    pizzaPriorty = []
    for index, pizzaType in enumerate(pizzaTypes):
        ingredients = pizzaType.split(' ')[1:]
        result = 1
        for ingredient in ingredients:
            result = result * (ingredientMap.get(ingredient)/totalPizza)
        pizzaPriorty.append((str(index), result, ingredients))

    pizzaPriorty = sorted(pizzaPriorty,key=lambda x: x[1])
    return pizzaPriorty

def fetch_input(fileName):
    pizzaTypes = []
    file = open(f'./inputs/{fileName}', 'r')
    lines = file.readlines()
    firstLine = lines[0].strip()
    if firstLine:
        totalPizza, twoMembers, threeMembers, fourMembers = firstLine.split(' ')
    for line in lines[1:]:
        pizzaTypes.append(line)
    return (totalPizza, twoMembers, threeMembers, fourMembers, pizzaTypes)
    
if __name__ == '__main__':
    fileName = 'e_many_teams.in'
    processedInput = fetch_input(fileName)
    pizzaPriorty = process_input(int(processedInput[0]), processedInput[4])
    result = distribute_pizza(pizzaPriorty, processedInput)
    out = open(f'./outputs/{fileName}', 'w')
    out.write(str(len(result)) + "\n")
    for line in result:
        out.write(" ".join(line)  + "\n")
    out.close()