# Password Generator 3.2
# Librarys
import PySimpleGUI as sg
import random as r
import pyperclip
import datetime

sg.theme('DarkGray12')
uni_font = "Arial", 13


# Vars
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_small = letters.lower()
numbers = '0123456789'
symbols = '!@$%-*&'
password_mix = ''
templates = ['Шаблон #1', 'Шаблон #2', 'Шаблон #3']
numb = ['1','2','3','4','5','6','7','8','9','0']
Blet_ch = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Slet_ch = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','y','v','w','x','y','z']
sym_ch = ['!','@','$','%','-','*','&']
alright = False
alright_1 = False
alright_2 = False
alright_3 = False
alright_4 = False
mix_menu = 'Данная кнопка объединяет все 4 сгенерированных пароля \nв единое целое и копирует их. После, вы можете поместить \nэти пароли в таблицы, и он будут добавлены в отдельные ячейки'
trustworthy = 'Данный чекбокс предотвращает генерацию простых паролей из компонентов, \nкоторые  включены в генерацию.'
trustworthy_tmp = 'Данный чекбокс предотвращает генерацию простых паролей в шаблонах из компонентов, \nкоторые  включены в генерацию.'


# UI Components
components_left = [
    [sg.Text('Количество символов')],
    [sg.Slider(range=(4, 40), default_value=12, orientation='h', key='-PASS_LEN-')],
    [sg.Checkbox('123', key='-NUMB_BOX-', default=True)],
    [sg.Checkbox('ABC', key='-BIG_L_BOX-')],
    [sg.Checkbox('abc', key='-SMALL_L_BOX-', default=True)],
    [sg.Checkbox('!@%', key='-SYM_BOX-')],
]

# components_left = [
#     [sg.Frame('Компоненты', [[sg.Column(components_leftt)]])]
#     ]
copy_size = 6, 1
components_right = [
    [sg.InputText('', size=(37,1), key='-OUTPUT1-'), sg.Button('Копир.', size=copy_size, key='-COPY_PASS_1-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT2-'), sg.Button('Копир.', size=copy_size, key='-COPY_PASS_2-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT3-'), sg.Button('Копир.', size=copy_size, key='-COPY_PASS_3-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT4-'), sg.Button('Копир.', size=copy_size, key='-COPY_PASS_4-')],
    [sg.Text()],
    [sg.Checkbox('Автокопирование первой строки', size=(26,1), default=True, key='-AUTOCOPY_BOX-'), sg.Button('Сгенерировать', focus=True, size=(14,1), key='-GEN-')],
    [sg.Checkbox('Надёжный', tooltip=trustworthy, default=True, key='-GOOD_GEN-'), sg.Checkbox('Надёжные шаблоны', tooltip=trustworthy_tmp, default=False, key='-GOOD_TMP-'), sg.Button('Объединить', tooltip=mix_menu, size=(10,1),key= '-MIX-')]
]

components_templ = [
    [sg.Button('Шаблон #1', k='-TEMP_1-'),sg.Button('!', k='-!_TMP_1-'),sg.Button('Шаблон #2', k='-TEMP_2-'),sg.Button('!', k='-!_TMP_2-'),sg.Button('Шаблон #3',k='-TEMP_3-'),sg.Button('!', k='-!_TMP_3-'),sg.T(' '*32), sg.Button('Настройки', k='-TMP_OPTIONS-')],
]

# Components packing
layout = [
    [
        sg.Column(components_left), sg.VSeparator(), sg.Column(components_right),
    ],
    [sg.HSeparator()],
    [sg.Column(components_templ)],
]

# Functions
def numb_add():
    global password
    password += numbers
def s_let_add():
    global password
    password += letters_small
def b_let_add():
    global password
    password += letters
def sym_add():
    global password
    password += symbols
def gen():
    global length, i, password_out
    for i in range(length):
        password_out += r.choice(password)
def mix_all():
    global password_mix
    password_mix += values['-OUTPUT1-'] + '\n'
    password_mix += values['-OUTPUT2-'] + '\n'
    password_mix += values['-OUTPUT3-'] + '\n'
    password_mix += values['-OUTPUT4-']
    pyperclip.copy(password_mix)
    password_mix = ''
def temp_1():
    global password, length, data, f
    try:
        with open('template_1.txt', 'r+', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            password = ''
            if data[1].strip() == 'True':
                numb_add()
            if data[2].strip() == 'True':
                s_let_add()
            if data[3].strip() == 'True':
                b_let_add()
            if data[4].strip() == 'True':
                sym_add()
    except FileNotFoundError:
        length = 12
        password = ''
        numb_add()
        s_let_add()
def temp_2():
    global password, length, data, f
    try:
        with open('template_2.txt', 'r', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            password = ''
            if data[1].strip() == 'True':
                numb_add()
            if data[2].strip() == 'True':
                s_let_add()
            if data[3].strip() == 'True':
                b_let_add()
            if data[4].strip() == 'True':
                sym_add()
    except FileNotFoundError:
        length = 12
        password = ''
        numb_add()
        s_let_add()
        b_let_add()
        sym_add()
def temp_3():
    global password, length, data, f
    try:
        with open('template_3.txt', 'r+', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            password = ''
            if data[1].strip() == 'True':
                numb_add()
            if data[2].strip() == 'True':
                s_let_add()
            if data[3].strip() == 'True':
                b_let_add()
            if data[4].strip() == 'True':
                sym_add()
    except FileNotFoundError:
        length = 20
        password = ''
        numb_add()
        s_let_add()
        b_let_add()
        sym_add()
def tmp_1_inform():
    global password, length, data, f,tmp_1_info
    try:
        with open('template_1.txt', 'r', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            tmp_1_info = 'Длина пароля - ' + str(length) + '\n'
            if data[1].strip() == 'True':
                tmp_1_info += 'Цифры' + '\n'
            if data[2].strip() == 'True':
                tmp_1_info += 'Маленькие буквы' + '\n'
            if data[3].strip() == 'True':
                tmp_1_info += 'Большие буквы' + '\n'
            if data[4].strip() == 'True':
                tmp_1_info += 'Символы' + '\n'
        f.close()
    except FileNotFoundError:
        tmp_1_info = 'Длина пароля - 12' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
    sg.popup(tmp_1_info, font=uni_font)
    tmp_1_info = ''
def tmp_2_info():
    global password, length, data, f, tmp_1_info
    try:
        with open('template_2.txt', 'r+', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            tmp_1_info = 'Длина пароля - ' + str(length) + '\n'
            if data[1].strip() == 'True':
                tmp_1_info += 'Цифры' + '\n'
            if data[2].strip() == 'True':
                tmp_1_info += 'Маленькие буквы' + '\n'
            if data[3].strip() == 'True':
                tmp_1_info += 'Большие буквы' + '\n'
            if data[4].strip() == 'True':
                tmp_1_info += 'Символы' + '\n'
        f.close()
    except FileNotFoundError:
        tmp_1_info = 'Длина пароля - 12' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
        tmp_1_info += 'Большие буквы' + '\n'
        tmp_1_info += 'Символы' + '\n'
    sg.popup(tmp_1_info, font=uni_font)
    tmp_1_info = ''
def tmp_3_info():
    global password, length, data, f, tmp_1_info
    try:
        with open('template_3.txt', 'r', encoding='UTF-8') as f:
            data = f.readlines()
            length = int(data[0])
            tmp_1_info = 'Длина пароля - ' + str(length) + '\n'
            if data[1].strip() == 'True':
                tmp_1_info += 'Цифры' + '\n'
            if data[2].strip() == 'True':
                tmp_1_info += 'Маленькие буквы' + '\n'
            if data[3].strip() == 'True':
                tmp_1_info += 'Большие буквы' + '\n'
            if data[4].strip() == 'True':
                tmp_1_info += 'Символы' + '\n'
        f.close()
    except FileNotFoundError:
        tmp_1_info = 'Длина пароля - 20' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
        tmp_1_info += 'Большие буквы' + '\n'
        tmp_1_info += 'Символы' + '\n'
    sg.popup(tmp_1_info, font=uni_font)
    tmp_1_info = ''
def checker_numb():
    global i, alright, password_out
    if numbers in password and letters_small in password and letters in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright = True
                    break
                else:
                    alright = False
            for i in Slet_ch:
                if i in password_out:
                    alright = True
                    break
                else:
                    alright = False
            for i in Blet_ch:
                if i in password_out:
                    alright = True
                    break
                else:
                    alright = False
def checker():
    global i, alright_1, alright_2, alright_3, alright_4, password_out
    # Small letters, big letters, symbols and numbers check
    if numbers in password and letters_small in password and letters in password and symbols in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright_1 = True
                    break
                else:
                    alright_1 = False
            for i in Slet_ch:
                if i in password_out:
                    alright_2 = True
                    break
                else:
                    alright_2 = False
            for i in Blet_ch:
                if i in password_out:
                    alright_3 = True
                    break
                else:
                    alright_3 = False
            for i in sym_ch:
                if i in password_out:
                    alright_4 = True
                    break
                else:
                    alright_1 = False
            print(password_out)
            if alright_1 == False or alright_2 == False or alright_3 == False or alright_4 == False:
                password_out = ''
                gen()
            else:
                break
    # Small letters, big letters and numbers check
    if numbers in password and letters_small in password and letters in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright_1 = True
                    break
                else:
                    alright_1 = False
            for i in Slet_ch:
                if i in password_out:
                    alright_2 = True
                    break
                else:
                    alright_2 = False
            for i in Blet_ch:
                if i in password_out:
                    alright_3 = True
                    break
                else:
                    alright_3 = False
            if alright_1 == False or alright_2 == False or alright_3 == False:
                password_out = ''
                gen()
            else:
                break
    # Small letters and numbers
    if numbers in password and letters_small in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright_1 = True
                    break
                else:
                    alright_1 = False
            for i in Slet_ch:
                if i in password_out:
                    alright_2 = True
                    break
                else:
                    alright_2 = False
            if alright_1 == False or alright_2 == False:
                password_out = ''
                gen()
            else:
                break
    # Big letters and numbers
    if numbers in password and letters in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright_1 = True
                    break
                else:
                    alright_1 = False
            for i in Blet_ch:
                if i in password_out:
                    alright_2 = True
                    break
                else:
                    alright_2 = False
            if alright_1 == False or alright_2 == False:
                password_out = ''
                gen()
            else:
                break
    else:
        pass
def passinlog():
    global now
    now = datetime.datetime.now()
    with open("logs_passwords.txt", 'a') as f:
        f.write(f"\n{now.strftime('%Y-%m-%d %H:%M:%S')} - {password}")
def passinlog_auto():
    global now
    now = datetime.datetime.now()
    with open("logs_passwords.txt", 'a') as f:
        f.write(f"\n[autocopy] {now.strftime('%Y-%m-%d %H:%M:%S')} - {password_out}")

window = sg.FlexForm('Password generator Standard+ Edition by GANTER',icon='gpgico.ico', grab_anywhere=False, auto_size_text=True,font=uni_font, layout=layout)

# Window functions
while True:
                                                        # Read window
    event, values = window.read()
                                                        # Generate button
    if event == '-GEN-':        #values["NUMB_BOX"] == True:
        password = ''
        password_out = ''
        length = int(values['-PASS_LEN-'])
        if values['-NUMB_BOX-'] == True:
            numb_add()
        if values['-BIG_L_BOX-'] == True:
            b_let_add()
        if values['-SMALL_L_BOX-'] == True:
            s_let_add()
        if values['-SYM_BOX-'] == True:
            sym_add()
        if password != '':
            gen()
            if values['-GOOD_GEN-'] == True:
                checker()
        else:
            sg.popup('Выберите хотя бы один компонент для пароля')
            continue
        window['-OUTPUT1-'].update(password_out)
        if values['-AUTOCOPY_BOX-'] == True:
            pyperclip.copy(password_out)
            passinlog_auto()
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
                                                        # Template button №1
    if event == '-TEMP_1-':
        temp_1()
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
                checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
                                                        # Template button №2
    if event == '-TEMP_2-':
        temp_2()
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
                                                        # Template button №3
    if event == '-TEMP_3-':
        temp_3()
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_TMP-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    if event == '-!_TMP_1-':
        tmp_1_inform()
    if event == '-!_TMP_2-':
        tmp_2_info()
    if event == '-!_TMP_3-':
        tmp_3_info()
                                                        # Copy button №1
    if event == '-COPY_PASS_1-':
        password = values['-OUTPUT1-']
        pyperclip.copy(password)
        passinlog()
        password = ''
                                                        # Copy button №2
    if event == '-COPY_PASS_2-':
        password = values['-OUTPUT2-']
        pyperclip.copy(password)
        passinlog()
        password = ''
                                                        # Copy button №3
    if event == '-COPY_PASS_3-':
        password = values['-OUTPUT3-']
        pyperclip.copy(password)
        passinlog()
        password = ''
                                                        # Copy button №4
    if event == '-COPY_PASS_4-':
        password = values['-OUTPUT4-']
        pyperclip.copy(password)
        passinlog()
        password = ''
                                                        # Mix button
    if event == '-MIX-':
        if values['-OUTPUT1-'] != '' and values['-OUTPUT2-'] != '' and values['-OUTPUT3-'] != '' and values['-OUTPUT4-'] != '':
            mix_all()
        else:
            sg.popup('Невозможно сгенерировать пустые пароли')
                                                        # Close validator
    if event == '-TMP_OPTIONS-':
        layout2 = [
        [sg.Combo(templates, size=(20, 1), default_value=templates[0], readonly=True, k='-CHOOSE_TEMPL-')],
        [sg.Checkbox('123', default=True, k='-NUMB_ADD-')],
        [sg.Checkbox('abc', default=True, k='-SMALL_LETT_ADD-')],
        [sg.Checkbox('ABC', default=False, k='-BIG_LETT_ADD-')],
        [sg.Checkbox('!@%', default=False, k='-SYM_ADD-')],
        [sg.Slider(range=(4, 40), default_value=12, orientation='h', key='-LEN_ADD-')],
        [sg.Submit('Сохранить', k='-SAVE-'), sg.Button('Закрыть', k='-CLOSE-')]
        ]

        helper = sg.FlexForm('Редактор шаблонов by GANTER (только для Standard+)', layout=layout2, font=uni_font)

        while True:
            event, values = helper.read()
            if event == '-CLOSE-' or event == sg.WINDOW_CLOSED:
                break
            if event == '-SAVE-':
                NUMB = False
                SLETTER = False
                BLETTER = False
                SYM = False
                length = int(values['-LEN_ADD-'])
                if values['-NUMB_ADD-'] == True:
                    NUMB = True
                if values['-SMALL_LETT_ADD-'] == True:
                    SLETTER = True
                if values['-BIG_LETT_ADD-'] == True:
                    BLETTER = True
                if values['-SYM_ADD-'] == True:
                    SYM = True
                templ_chsr = values['-CHOOSE_TEMPL-']
                if templ_chsr == templates[0]:
                    with open('template_1.txt', 'w') as f:
                        f.write(f'{length}\n{NUMB}\n{SLETTER}\n{BLETTER}\n{SYM}')
                    sg.Popup(f'{templates[0]} сохранён')
                elif templ_chsr == templates[1]:
                    with open('template_2.txt', 'w') as f:
                        f.write(f'{length}\n{NUMB}\n{SLETTER}\n{BLETTER}\n{SYM}')
                    sg.Popup(f'{templates[1]} сохранён')
                elif templ_chsr == templates[2]:
                    with open('template_3.txt', 'w') as f:
                        f.write(f'{length}\n{NUMB}\n{SLETTER}\n{BLETTER}\n{SYM}')
                    sg.Popup(f'{templates[2]} сохранён')
        helper.close()
        continue
    if event == sg.WINDOW_CLOSED:
        break
