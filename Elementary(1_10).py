# Lesson #1 (multiplication)
def multiplication(a: int, b: int) -> int:
   return a * b
print(multiplication(2, 5))


# Lesson #2 (First Word)
def first_word(word: str):
    words: list = word.split()
    return words[0]
print(first_word("Hey go"))


# Lesson #3 (Password)
def acc_password(word: str):
    list(word)
    i: int = 0
    for x in word:
        i += 1
    if i <= 6:
        return False
    else:
        return True
print(acc_password("short"))


# Lesson #4 (Number Length)
def number_length(number: int):
   s_number = str(number)
   list(s_number)
   i: int = 0
   for x in s_number:
       i += 1
   return i
print(number_length(123456))


# Lesson #5 (End Zeros)
def end_zeros(number: int):
    s_number = str(number)
    list(s_number)
    rev = reversed(s_number)
    i: int = 0
    z: int = 0
    for x in list(rev):
        if z < 1:
            y: int = int(x)
            if y <= 0:
                i += 1
            else:
                z += 1
    return i
print(end_zeros(1000001000100000010000))


# Lesson #6 (Backward String)
def backward_string(string: str):
    list(string)
    rev = reversed(string)
    return ''.join(rev)
print(backward_string('Hello'))


# Lesson #7 (Remove All Before)
def remove_all_before(mass: list, border: int):
    if len(mass) == 0:
        print('List is empty!')
    if len(mass) <= 2:
        print('List contains 2 elements!')
    else:
        try:
            index = mass.index(border)
            del mass[0:index]
        except:
            print('List is not border')
    return mass
print(list(remove_all_before([1, 1, 5, 6, 7], 5)))


# Lesson #8 (All Upper I)
def is_all_upper(my_string: str):
    my_string = my_string.replace(' ', '')
    if my_string == '':
        return True
    if my_string.isdigit():
        return True
    else:
        return my_string.isupper()
print(is_all_upper("55 55 5 "))


# Lesson #9 (Replace First)
def replace_first(mass: list):
    if len(mass) <= 1:
        return mass
    else:
        index = mass[-1]
        mass.append(index)
        mass[-1] = mass[0]
        del mass[0]
        return mass
print(replace_first([1]))


# Lesson #10 (Max Digit)
def max_digit(number: int):
    num_string = str(number)
    max_num = max(num_string)
    return int(max_num)
print(max_digit(124))
