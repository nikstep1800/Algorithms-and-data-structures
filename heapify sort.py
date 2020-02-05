# Пирамидальная сортировка

# Также известна как сортировка кучей. Этот популярный алгоритм,
# как и сортировки вставками или выборкой, сегментирует список на две части:
# отсортированную и неотсортированную. Алгоритм преобразует второй сегмент
# списка в структуру данных «куча» (heap), чтобы можно было эффективно
# определить самый большой элемент.

# Время сортировки O(n*log(n))

# Сначала преобразуем список в Max Heap — бинарное дерево,
# где самый большой элемент является вершиной дерева.
# Затем помещаем этот элемент в конец списка.
# После перестраиваем Max Heap и снова помещаем новый наибольший элемент
# уже перед последним элементом в списке.
#
# Этот процесс построения кучи повторяется, пока все вершины дерева
# не будут удалены.

def heapify(nums, heap_size, root_index):
    # индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2*root_index) + 1
    right_child = (2*root_index) + 2

    # если левый потомок корня - допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # аналогично для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # если наибольший элемент больше не корневой, то они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # создаем Max Heap из списка
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

list_of_nums = [5, 1, 2, 7, 10, 14, -23, 23, 51, 12]
heap_sort(list_of_nums)
print(list_of_nums)