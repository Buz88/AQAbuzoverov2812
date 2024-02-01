'''add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
Exit - вихід'''


note_string = []

while True:
    new_note_string = (input('Enter your note: '))
    if new_note_string.startswith('add'):
        note_string.append(new_note_string.replace('add', ''))
    elif new_note_string == 'earliest':
        reversed_note_string = reversed(note_string)
        print('Від найновішої до найпізнішої: ', list(reversed_note_string))
    elif new_note_string == 'latest':
        print('Від найпізнішої до найновішої: ', note_string)
    elif new_note_string == 'longest':
        print('Від найдовшої до найкоротшоЇ: ', sorted(note_string, key=len, reverse=True))
    elif new_note_string == 'shortest':
        print('Від найкоротшої до найдовшої: ', sorted(note_string, key=len))
    elif new_note_string == 'Exit':
        print('Thanks for')
    else:
        print('Not a valid')



