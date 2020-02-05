def queue(command):
    global first
    global last
    global size

    if command.startswith('push'):

        value = command[5:]

        if size == 0:
            first = [value, None, None]
            last = first
        elif size == 1:
            item = [value, first, None]
            first[2] = item    # говорю, что за первым элементом появился элемент first = [1, N, [2, [1, N, N], N]]
            last = item        # говорю, что перед последнимэлементом стоит первый, а за ним никого last = item = [2, [1, N, N], N]
        else:
            item = [value, last, None]
            last[2] = item
            last = item
        size += 1
        print('ok')

    if command.startswith('pop'):
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

    if command.startswith('front'):
        print(first[0])

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
    queue(command)
    command = input()
print('bye')