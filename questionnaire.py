print('Вітаю в анкеті ІПЗ-24')
name=input('Введіть ваше ім\'я: ')
age=input('Введіть ваш вік: ')
hobby=input('Яке ваше хобі? ')

print(f'\n=====\nІнформація зібрана.\n=====\nІм\'я: {name}\nВік: {age}\nПовнолітній: {"Так" if int(age) >= 18 else "Ні"}\nХобі: {hobby}')
