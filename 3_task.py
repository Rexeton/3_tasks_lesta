#На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует
# данный ей массив чисел.
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
# Объяснить, почему вы считаете, что функция соответствует заданным критериям.


""" Выбрал быструю сортировку, так как она имеет наибольшую скорость выполнения. Наихудший вариант будет в это происходит, только когда элементы массива правильно восходят или нисходят.
В этих случаях можно делать праверку на такое поведение"""

def quick_sort(self, unsorted, start, end):
    """ быстрая сортировка """
    if start >= end:
        return
    i_pivot = partition(unsorted, start, end - 1)
    quick_sort(unsorted, start, i_pivot)
    quick_sort(unsorted, i_pivot + 1, end)


def partition(unsorted, start, end):
    """ arrange (left array < pivot) and (right array > pivot) """
    pivot = unsorted[end]
    i_pivot = start
    for i in range(start, end):
        if unsorted[i].value <= pivot.value:
            swap(unsorted, i, i_pivot)
            i_pivot += 1
    swap(unsorted, i_pivot, end)

    return i_pivot

def swap(arr, a, b):
    """ переставляем элементы a и b в массиве """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp