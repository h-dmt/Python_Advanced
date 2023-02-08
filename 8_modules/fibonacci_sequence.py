from fibonacci import *

while True:
    command = input('Create sequence or locate number in sequence?\n')
    if command.startswith('Stop'):
        break
    elif command.startswith('Create'):
        n = int(command.split()[-1])
        create_sequence(n)
    elif command.startswith('Locate'):
        n = int(command.split()[-1])
        try:
            print(locate(n))
        except NameError("sequence not initialized"):
            pass
