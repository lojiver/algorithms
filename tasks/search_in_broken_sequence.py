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

# успешная попытка на контесте 82864769


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
