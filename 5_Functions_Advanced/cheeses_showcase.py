def sorting_cheeses(**cheeses):

    cheeses = dict(sorted(cheeses.items(), key=lambda c: (-len(c[1]), c[0])))

    result = []
    for cheese, q in cheeses.items():
        result.append(cheese)
        quantity = sorted(q, reverse=True)
        quantity = list(map(str, quantity))
        #result.append(', '.join(quantity))
        result += quantity
    #return result
    return '\n'.join([el for el in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
