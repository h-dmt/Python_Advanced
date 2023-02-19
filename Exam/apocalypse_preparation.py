from collections import deque

textiles = deque([int(i) for i in input().split()])  # take FIRST
medicaments = deque([int(i) for i in input().split()])  # take LAST
item_values = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}
items_created = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}
resto = 0
item_created = False
while textiles and medicaments:
    textile = textiles.popleft()
    med = medicaments.pop()
    sum_of = textile + med
    for element, value in item_values.items():
        if sum_of == value:
            items_created[element] += 1
            item_created = True
            break
    if not item_created:
        if sum_of > 100:
            resto = sum_of - 100
            items_created['MedKit'] += 1
            medicaments.append(medicaments.pop() + resto)
        else:
            medicaments.append(med + 10)
    item_created = False

items_created = dict(sorted(items_created.items(), key=lambda x: (-x[1], x[0])))


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")


for k, v in items_created.items():
    if v:
        print(f"{k} - {v}")

if medicaments:
    medicaments.reverse()
    print("Medicaments left:", end=' ')
    print(*medicaments, sep=', ')
if textiles:
    print("Textiles left:", end=' ')
    print(*textiles, sep=', ')
