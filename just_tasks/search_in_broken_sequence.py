'''
Алла ошиблась при копировании из одной структуры данных в другую.
Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию, и в нём можно было найти элемент
за логарифмическое время.
Алла скопировала данные из кольцевого буфера в обычный массив,
но сдвинула данные исходной отсортированной последовательности.
Теперь массив не является отсортированным.
Тем не менее, нужно обеспечить возможность находить в нем элемент за O(log n).
Можно предполагать, что в массиве только уникальные элементы.
От вас требуется реализовать функцию, осуществляющую поиск в
сломанном массиве.
'''

# успешная попытка на контесте 82825072


def binary_search(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального,
        # значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binary_search(arr, x, mid + 1, right)


def search_begining(arr, last, left, right, max_position=-1, max=0):
    if right <= left:
        return max_position + 1
    mid = (left + right) // 2
    if arr[mid] - last > max:
        max = arr[mid] - last
        max_position = mid
        return search_begining(arr, last, mid + 1, right, max_position, max)
    elif arr[mid] - last < max:
        return search_begining(arr, last, left, mid, max_position, max)


def broken_search(nums, target) -> int:
    if len(nums) > 2:
        begining = search_begining(nums, nums[-1], 0, len(nums))
        if target <= nums[-1]:
            return binary_search(nums, target, begining, len(nums))
        elif target < nums[begining - 1]:
            return binary_search(nums, target, 0, begining)
        else:
            return -1
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
