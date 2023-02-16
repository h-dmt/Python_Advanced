# https://judge.softuni.org/Contests/Practice/Index/2812#0

from collections import deque

effects = deque(int(effect) for effect in input().split(', ') if int(effect) > 0)
explosive_power = deque(int(power) for power in input().split(', ') if int(power) > 0)
fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

while effects and explosive_power:
    effect = effects.popleft()
    power = explosive_power.pop()
    combo = effect + power

    if combo % 3 == 0 and combo % 5 != 0:
        fireworks["Palm Fireworks"] += 1

    elif combo % 5 == 0 and combo % 3 != 0:
        fireworks["Willow Fireworks"] += 1

    elif combo % 5 == 0 and combo % 3 == 0:
        fireworks["Crossette Fireworks"] += 1

    else:
        if effect - 1 > 0:
            effects.append(effect - 1)
        explosive_power.append(power)

    if all([firework >= 3 for firework in fireworks.values()]):
        print("Congrats! You made the perfect firework show!")
        break

if any([firework < 3 for firework in fireworks.values()]):
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print("Firework Effects left:", end=' ')
    print(*effects, sep=', ')
if explosive_power:
    print("Explosive Power left:", end=' ')
    print(*explosive_power, sep=', ')
for firework in fireworks:
    print(f"{firework}: {fireworks[firework]}")
