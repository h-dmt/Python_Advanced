# https://judge.softuni.org/Contests/Practice/Index/3306#2


def naughty_or_nice_list(*args, **kwargs):
    santa_list = args[0]
    numbers = [n[0] for n in santa_list]
    names = [n[1] for n in santa_list]
    final_list = {'Nice': [], 'Naughty': [], 'Not found': []}
    output_print = []
    if len(args) > 1:
        commands = args[1:]
        for command in commands:
            num, move_to = command.split('-')
            if numbers.count(int(num)) == 1:
                ind_kid = numbers.index(int(num))
                kid = names[ind_kid]
                final_list[move_to].append(kid)
                names.pop(ind_kid)
                numbers.pop(ind_kid)
    if kwargs:
        for name in kwargs:
            if names.count(name) == 1:
                final_list[kwargs[name]].append(name)
                index_num = names.index(name)
                n = numbers[index_num]
                names.pop(index_num)
                numbers.pop(index_num)

    final_list['Not found'].extend(names)
    for key in final_list:
        if final_list[key]:
            output_print.append(f"{key}: {', '.join(final_list[key])}")

    return '\n'.join(output_print)


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))