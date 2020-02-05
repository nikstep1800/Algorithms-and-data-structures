def queue1(command):
    global first1
    global last1
    global size1
    if command.startswith('push'):
        value = int(command[5:])
        if size1 == 0:
            first1 = [value, None, None]
            last1 = first1
        elif size1 == 1:
            item = [value, first1, None]
            first1[2] = item
            last1 = item
        else:
            item = [value, last1, None]
            last1[2] = item
            last1 = item
        size1 += 1
    if command.startswith('pop'):
        if size1 == 1:
            item = None
            first1 = item
            last1 = item
            size1 = 0
        elif size1 == 2:
            first1[2][1] = None
            first1 = first1[2]
            last1 = first1
            size1 = 1
        else:
            first1[2][1] = None
            first1 = first1[2]
            size1 -= 1
    if command.startswith('front'):
        return first1[0]

def queue2(command):
    global first2
    global last2
    global size2
    if command.startswith('push'):
        value = int(command[5:])
        if size2 == 0:
            first2 = [value, None, None]
            last2 = first2
        elif size2 == 1:
            item = [value, first2, None]
            first2[2] = item
            last2 = item
        else:
            item = [value, last2, None]
            last2[2] = item
            last2 = item
        size2 += 1
    if command.startswith('pop'):
        if size2 == 1:
            item = None
            first2 = item
            last2 = item
            size2 = 0
        elif size2 == 2:
            first2[2][1] = None
            first2 = first2[2]
            last2 = first2
            size2 = 1
        else:
            first2[2][1] = None
            first2 = first2[2]
            size2 -= 1
    if command.startswith('front'):
        return first2[0]

first1 = None
last1 = None
size1 = 0
first2 = None
last2 = None
size2 = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)):
    queue1('push ' + str(a[i]))
for j in range(len(b)):
    queue2('push ' + str(b[j]))
k = 0
while size1 != 0 and size2 != 0:
    k += 1
    x = queue1('front')
    y = queue2('front')
    queue1('pop')
    queue2('pop')
    if x > y and (y, x) != (0, 9) or (x, y) == (0, 9):
        queue1('push ' + str(x))
        queue1('push ' + str(y))
    else:
        queue2('push ' + str(x))
        queue2('push ' + str(y))
    if k == 1000000:
        print('botva')
        break

if size1 != 0 and size2 == 0:
    print('first', k)
if size2 != 0 and size1 == 0:
    print('second', k)