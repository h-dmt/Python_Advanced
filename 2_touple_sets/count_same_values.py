
values = tuple(float(n) for n in input().split(' '))
# count occurrences of each element in the tuple

tuple_elements = {e: values.count(e) for e in values}

for k, v in tuple_elements.items():
    print(f"{k:.1f} - {v} times", end='\n')
