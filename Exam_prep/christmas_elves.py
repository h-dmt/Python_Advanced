# https://judge.softuni.org/Contests/Practice/Index/3306#0
#
# the first elf takes the last box of materials and tries to create the toy:
#     • Usually, the elf needs energy equal to the number of materials.
#     If he has enough energy, he makes the toy. His energy decreases by the used energy,
#     and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1,
#     and goes to the end of the line, preparing for the upcoming boxes.
#     • Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as
#     much energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases;
#     he eats a cookie reward and goes to the end of the line, similar to the first bullet.
#     • Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy
#     when he just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward.
#     However, his energy is already spent, and it needs to be added to the total elves' energy.
#         ◦ If an elf creates 2 toys, but he is clumsy, he breaks them.
#     • If an elf does not have enough energy, he leaves the box of materials to the next elf.
#     Instead of making the toy, the elf drinks a hot chocolate which doubles his energy,
#     and goes to the end of the line, preparing for the upcoming boxes.
# Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units,
# he does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.

from collections import deque

elv_energy = deque(int(elv) for elv in input().split())  # from first
materials = deque(int(el) for el in input().split())  # from last
tot_energy = 0
toys = 0
THIRD = False
FIFTH = False
i = 0

while materials and any(elv_energy):

    elv = elv_energy.popleft()
    box = materials.pop()
    if elv < 5:
        materials.append(box)
        continue
    i += 1
    THIRD = True if i % 3 == 0 else False
    FIFTH = True if i % 5 == 0 else False

    if THIRD:
        if elv >= box * 2:
            tot_energy += box * 2
            elv -= box * 2
            if not FIFTH:
                toys += 2
                elv_energy.append(elv + 1)
            else:
                elv_energy.append(elv)
        else:
            elv_energy.append(elv * 2)
            materials.append(box)

    else:
        if elv >= box:
            tot_energy += box
            elv -= box
            if not FIFTH:
                toys += 1
                elv_energy.append(elv + 1)
            else:
                elv_energy.append(elv)
        else:
            elv_energy.append(elv * 2)
            materials.append(box)

print(f"Toys: {toys}")
print(f"Energy: {tot_energy}")
if elv_energy:
    print(f"Elves left:", end=' ')
    print(*elv_energy, sep=', ')
if materials:
    print("Boxes left:", end=' ')
    print(*materials, sep=', ')
