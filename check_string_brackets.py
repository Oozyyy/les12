def check_string_brackets(text):
    counter_1 = 0
    counter_2 = 0
    for word in text:
        if word == '(':
            counter_1 += 1
        if word == ')':
            counter_2 += 1
    if counter_1 == counter_2:
        print('Yes')
    else:
        print('No')
check_string_brackets(input('Введите скобочки'))
