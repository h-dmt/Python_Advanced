# ===================================================================================================== #
# You should take the last box with materials and the first magic level value to craft a toy.           #
# Their multiplication calculates the total magic level. If the result equals one of the levels         #
# described in the table above, you craft the present and remove both materials and magic value.        #
# Otherwise:                                                                                            #
#     • If the product of the operation is a negative number, you should sum the values together,       #
#     remove them both from their positions, and add the result to the materials.                       #
#     • If the product doesn't equal one of the magic levels in the table and is a positive number,     #
#     remove only the magic value and increase the material value by 15.                                #
#     • If the magic or material (or both) equals 0, remove it (or both) and continue crafting the      #
#     presents.                                                                                         #
# Stop crafting presents when you run out of boxes of materials or magic level values.                  #
# Your task is considered done if you manage to craft either one of the pairs:                          #
#     • a doll and a train                                                                              #
#     • a teddy bear and a bicycle                                                                      #
# ===================================================================================================== #

from collections import deque

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

material_boxes = deque(int(x) for x in input().split())  # Start from last
magic_values = deque(int(x) for x in input().split())  # Start from first
crafted = {}
while material_boxes and magic_values:
    material = material_boxes.pop()
    magic = magic_values.popleft()
    if material == 0 and magic == 0:
        continue
    elif material == 0:
        magic_values.appendleft(magic)
        continue
    elif magic == 0:
        material_boxes.append(material)
        continue

    product = material * magic

    if product in presents:
        if presents[product] in crafted:
            crafted[presents[product]] += 1
        else:
            crafted[presents[product]] = 1
    elif product < 0:
        product = material + magic
        material_boxes.append(product)

    elif product > 0:
        material_boxes.append(material + 15)

if 'Doll' in crafted and 'Wooden train' in crafted \
        or 'Teddy bear' in crafted and 'Bicycle' in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    material_boxes.reverse()
    material_left = list(map(str, material_boxes))
    print(f"Materials left: {', '.join(material_left)}")
if magic_values:
    magic_left = list(map(str, magic_values))
    print(f"Magic left: {', '.join(magic_left)}")

crafted = dict(sorted(crafted.items()))
[print(f"{toy}: {crafted[toy]}", sep='\n') for toy in crafted]
