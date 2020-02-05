# Сортировка выборкой

# Этот алгоритм сегментирует список на две части: отсортированную и
# неотсортированную. Наименьший элемент удаляется из второго списка
# и добавляется в первый.

# Время сортировки O(n^2)

# На практике не нужно создавать новый список для отсортированных элементов.
# В качестве него используется крайняя левая часть списка.
# Находится наименьший элемент и меняется с первым местами.

# Теперь, когда нам известно, что первый элемент списка отсортирован,
# находим наименьший элемент из оставшихся и меняем местами со вторым.
# Повторяем это до тех пор, пока не останется последний элемент в списке.

def selection_sort(nums):
    # значение i соответсвует кол-ву отсортированных значений
    for i in range(len(nums)):
        # исходно считаем наименьший первый элемент
        lowest_value_index = i
        # цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        # самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

list_of_nums = [5, 1, 2, 7, 10, 14, -23, 23, 51, 12]
selection_sort(list_of_nums)
print(list_of_nums)
