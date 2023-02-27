'''
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо
оценить сложность статьи.
Он придумал такой метод оценки:
берётся случайное предложение из текста и в нём ищется самое длинное слово.
Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.
'''


def get_longest_word(line: list) -> str:
    longest_length = 0
    longest_word = ''
    for word in line:
        length = len(word)
        if length > longest_length:
            longest_length = length
            longest_word = word
    return longest_word


def read_input() -> list:
    _ = input()
    line = list(map(str, input().strip().split()))
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


if __name__ == '__main__':
    print_result(get_longest_word(read_input()))
