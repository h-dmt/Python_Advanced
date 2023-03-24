def reverse_text(text: str):
    txt = reversed(text)
    for char in txt:
        yield char


for char in reverse_text("step"):
    print(char, end='')
