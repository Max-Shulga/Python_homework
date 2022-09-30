# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# Коментарий: я по всей видимости сам себе сильно усложнил задачу, но какое задание такое и решение.
# Откуда должны появляться позиции в файле txt никто не сказал:(
# А как нормально их от туда нормально извлекать я пока что понять не смог, поэтому получилось что получилось :)
# Получилось действие с file.txt ради действия, без него программа занимала бы в раз 5 меньше:)

def get_list(n):
    n_list = []
    for i in range(-n, n+1):
        n_list.append(i)
    return n_list


def file_completion(n=[]):
    file = open('file.txt', 'w')
    for i in range(len(n)):
        file.write(f'{i}')
        file.write('\n')
    file.close()
    return file


def get_copy():
    file_copy = open('file.txt', 'r')
    copy_file = '0\n'
    # Я проиграл этот бой, не понимаю почему он не хочет сам считывать 0 как первую строчку файла.
    for i in file_copy:
        copy_file += file_copy.read()
    index_list = copy_file.split()
    file_copy.close()
    return index_list


def get_multiplication(num_1, num_2, array_1, array_2):
    num_1 = int(array_1[num_1])
    num_2 = int(array_1[num_2])
    multi = int(array_2[num_1]) * int(array_2[num_2])
    return multi


print(f"{'-' * 100}\n START\n")

number = int(input('Input number: '))
number_list = get_list(number)
print(f'(-N, N )list: {number_list}')
copy_file = file_completion(get_list(number))
print(f'indexes from file.txt: {get_copy()}')
index_list= get_copy()
first_index = int(input('Enter the index of the first number: '))
second_index = int(input('Enter the index of the second number: '))
print(f'Multiplication of numbers by position {first_index}({number_list[first_index]}) * {second_index}({number_list[second_index]}) = {get_multiplication(first_index,second_index,index_list,number_list)}')
print(f"\n END \n {'-' * 100}")
