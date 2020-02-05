def dec(command):
    global first
    global last
    global size

    if command.startswith('push_front'):  # push in stack
        value = command[11:]
        if size == 0:
            last = first = [value, None, None]
        elif size == 1:
            item = [value, None, first]
            first[1] = item
            last = first
            first = item
        else:
            item = [value, None, first]
            first[1] = item
            first = item
        size += 1
        print('ok')

    if command.startswith('push_back'):  # push in queue
        value = command[10:]
        if size == 0:
            last = first = [value, None, None]
        elif size == 1:
            item = [value, first, None]
            first[2] = item
            last = item
        else:
            item = [value, last, None]
            last[2] = item
            last = item
        size += 1
        print('ok')

    if command.startswith('pop_front'):  # pop in queue
        print(first[0])
        if size == 1:
            item = None
            first = item
            last = item
            size = 0
        elif size == 2:
            first[2][1] = None
            first = first[2]
            last = first
            size = 1
        else:
            first[2][1] = None
            first = first[2]
            size -= 1
    if command.startswith('pop_back'):  # pop in stack
        print(last[0])
        if size == 1:
            item = None
            first = last = item
            size = 0
        elif size == 2:
            first[2] = None
            last = first
            size = 1
        else:
            last[1][2] = None
            last = last[1]
            size -= 1

    if command.startswith('front'):
        print(first[0])

    if command.startswith('back'):
        print(last[0])

    if command.startswith('size'):
        print(size)

    if command.startswith('clear'):
        item = None
        first = last = item
        size = 0
        print('ok')

first = None
last = None
size = 0

command = input()
while command != 'exit':
    dec(command)
    command = input()
print('bye')