def rectangle(length, width):

    def area(l, w):
        return l*w

    def perimeter(l, w):
        return l * 2 + w * 2

    if isinstance(length, int) and isinstance(width, int):
        return f"Rectangle area: {area(length, width)}\n\
Rectangle perimeter: {perimeter(length, width)}"
    else:
        return "Enter valid values!"

print(rectangle(2, 10))