# Сортировка слиянием

# Этот алгоритм относится к алгоритмам «разделяй и властвуй».
# Он разбивает список на две части, каждую из них он разбивает ещё на две и т. д.
# Список разбивается пополам, пока не останутся единичные элементы.

# Соседние элементы становятся отсортированными парами.
# Затем эти пары объединяются и сортируются с другими парами.
# Этот процесс продолжается до тех пор, пока не отсортируются все элементы.

# Время сортировки O(n*log(n))

# Список рекурсивно разделяется пополам, пока в итоге не получатся
# списки размером в один элемент. Массив из одного элемента считается
# упорядоченным. Соседние элементы сравниваются и соединяются вместе.
# Это происходит до тех пор, пока не получится полный отсортированный список.

# Сортировка осуществляется путём сравнения наименьших элементов
# каждого подмассива. Первые элементы каждого подмассива сравниваются первыми.
# Наименьший элемент перемещается в результирующий массив.
# Счётчики результирующего массива и подмассива, откуда был взят элемент,
# увеличиваются на 1.

# Функция merge_sort() возвращает новый список, а не сортирует существующий.
# Поэтому такая сортировка требует больше памяти для
# создания списка того же размера, что и входной список

def merge(left_list, right_list):
    sorted_list = []
    left_list_index=right_list_index = 0

    left_list_lenght, right_list_lenght = len(left_list), len(right_list)

    for _ in range(left_list_lenght + right_list_lenght):
        if left_list_index < left_list_lenght and right_list_index < right_list_lenght:
            # Сравниваем первые элементы в начале каждого списка
            # сли первый элемент левого подсписка меньше, добавляем
            # его в остортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # и наоборот
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в отсортированный массив
        elif left_list_index == left_list_lenght:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # и наоборот
        elif right_list_index == right_list_lenght:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    # Для того, чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2
    # сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

list_of_nums = [5, 1, 2, 7, 10, 14, -23, 23, 51, 12]
list_of_nums = merge_sort(list_of_nums)
print(list_of_nums)



