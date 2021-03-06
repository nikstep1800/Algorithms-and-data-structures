# Сортиовка вставками

# Как и сортировка выборкой, этот алгоритм сегментирует список на две части:
# отсортированную и неотсортированную.
# Алгоритм перебирает второй сегмент и вставляет текущий элемент в
# правильную позицию первого сегмента.

# Время сортировки O(n^2)

# Предполагается, что первый элемент списка отсортирован.
# Переходим к следующему элементу, обозначим его х.
# Если х больше первого, оставляем его на своём месте.
# Если он меньше, копируем его на вторую позицию, а х устанавливаем
# как первый элемент.
#
# Переходя к другим элементам несортированного сегмента,
# перемещаем более крупные элементы в отсортированном сегменте вверх по
# списку, пока не встретим элемент меньше x или не дойдём до конца списка.
# В первом случае x помещается на правильную позицию.

def insertion_sort(nums):
# сортировку начинаем со второго элемента,
# т.к. считаем, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # элементы отсортированного сегмента перемещаем вперед, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        # вставляем элемент
        nums[j+1] = item_to_insert

list_of_nums = [5, 1, 2, 7, 10, 14, -23, 23, 51, 12]
insertion_sort(list_of_nums)
print(list_of_nums)

