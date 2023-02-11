"""
First, you will be given a sequence of numbers, representing the quantities of the daily portions of food supplies in
his backpack.
Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he
will have at his disposal for the next seven days.
You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina.
He will start climbing from the first peak in the table below to the last one.
    • If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below,
    it means that the peak is conquered. In this case, you should remove both quantities from the sequences and
    continue with the next ones towards the next peak.
    • If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below,
    the peak remains unconquered. You should remove both quantities from the sequences.
    Alex will have to sleep in his tent. On the next day, he will try the same peak once again.
"""
from collections import deque

peaks_list = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
food = deque(input().split(', '))  # sum from last
stamina = deque(input().split(', '))  # sum from first
conquered_peaks = []

for peak in peaks_list:
    conquered = False
    while not conquered and food and stamina:
        energy_level = int(food.pop()) + int(stamina.popleft())
        if energy_level >= peaks_list[peak]:
            conquered = True
            conquered_peaks.append(peak)

if len(peaks_list) == len(conquered_peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)
