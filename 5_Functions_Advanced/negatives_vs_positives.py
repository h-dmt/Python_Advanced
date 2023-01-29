nums = [int(n) for n in input().split()]

positives = 0
negatives = 0

for n in nums:
    if n > 0:
        positives += n
    else:
        negatives += n

print(negatives)
print(positives)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
