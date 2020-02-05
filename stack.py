def stack(s):

    global last
    global size

    if str(s).startswith('push'):
        value = s[5:]
        if size == 0:
            item = [value, None]
            last = item
        else:
            item = [value, None]
            item[1] = last
            last = item
        size += 1
        print('ok')

    if str(s).startswith('pop'):
        print(last[0])
        if size == 1:
            item = None
            last = item
            size = 0
        else:
            item = [last[1][0], last[1][1]]
            last = item
            size -= 1

    if str(s).startswith('back'):
        print(last[0])

    if str(s).startswith('size'):
        print(size)

    if str(s).startswith('clear'):
        item = None
        last = item
        size = 0
        print('ok')

last = None
size = 0

command = input()
while command != 'exit':
    stack(command)
    command = input()
print('bye')