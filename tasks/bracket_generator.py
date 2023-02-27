'''
Рита по поручению Тимофея наводит порядок
в правильных скобочных последовательностях (ПСП),
состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —–
алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.
Помогите Рите —– напишите программу,
которая по заданному n выведет все ПСП в нужном порядке.
Рассмотрим второй пример. Надо вывести ПСП из четырёх символов.
Таких всего две:
(())
()()
(()) идёт раньше ()(), так как первый символ у них одинаковый,
а на второй позиции у первой ПСП стоит (, который идёт раньше ).
'''


def generate_bracket_sequence(i, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            generate_bracket_sequence(i + 1, n1 - 1, n2, prefix + '(')
        if (i > 0 and n2 > 0):
            generate_bracket_sequence(i - 1, n1, n2 - 1, prefix + ')')


def read_input() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    n = read_input()
    generate_bracket_sequence(1, n - 1, n, '(')