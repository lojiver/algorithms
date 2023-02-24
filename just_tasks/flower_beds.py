'''
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными
 отрезками, лежащими на одной прямой.
Для ландшафтных работ было нанято n садовников.
Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок
или его часть могли быть обработаны сразу несколькими садовниками.
Таким образом, отрезки, обрабатываемые двумя разными садовниками,
сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.
Рассмотрим примеры.
Пример 1:
Два одинаковых отрезка [7, 8] и [7, 8] сливаются в один,
но потом их накрывает отрезок [6, 10].
Таким образом, имеем две клумбы с координатами [2, 3] и [6, 10].

Пример 2
Отрезки [2, 3], [3, 4] и [3, 4] сольются в один отрезок
[2, 4]. Отрезок [5, 6] ни с кем не объединяется,
добавляем его в ответ.
'''


def count_flowerbads(arr):
    if len(arr) == 1:  # базовый случай рекурсии
        return arr

    # запускаем сортировку рекурсивно на левой половине
    mid = len(arr)//2
    left = count_flowerbads(arr[:mid])

    # запускаем сортировку рекурсивно на правой половине
    right = count_flowerbads(arr[mid:])

    # заводим массив для результата сортировки
    # result = [] * len(array)

    # сливаем результаты
    i = j = k = 0
    while i < len(left) and j < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[i][1] >= right[j][0]:
            arr[k][0] = min(left[i][0], right[j][0])
            arr[k][1] = max(left[i][1], right[j][1])
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while i < len(left):
        arr[k] = left[i]  # перенеси оставшиеся элементы left в result
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]  # перенеси оставшиеся элементы right в result
        j += 1
        k += 1

    return arr


def read_input():
    n = int(input())
    result = []
    i = 0
    while i < n:
        result.append(list(map(int, input().split())))
        i += 1
    return result


if __name__ == '__main__':
    print(read_input())
