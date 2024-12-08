# импортируем библиотеки
from tkinter import *
from tkinter import filedialog, messagebox
# импортируем модуль для работы с диалогом выбора файлов
import webbrowser
# импортируем модуль для работы с веб-браузером
import requests
# импортируем библиотеку для работы с HTTP-запросами
from bs4 import BeautifulSoup


# импортируем библиотеку для парсинга HTML
# Главное окно приложения
window = Tk()
# Заголовок окна
window.title('Авторизация')
# Размер окна
window.geometry('2000x1400')
# Можно ли изменять размер окна - нет
window.resizable(True, True)

# Кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# Переменная для чекбокса
remember_var = BooleanVar()

selected_option = StringVar(value="выберите вариант")




def increase_font_size():
    global font_header, font_entry, label_font

    font_header = ('Arial', font_header[1] + 2)
    font_entry = ('Arial', font_entry[1] + 2)
    label_font = ('Arial', label_font[1] + 2)

    main_label.config(font=font_header)
    username_label.config(font=label_font)
    password_label.config(font=label_font)
    phone_label.config(font=label_font)
    remember_me_checkbox.config(font=label_font)
    send_btn.config(font=label_font)


# Обработчик нажатия на кнопку 'Войти'
def clicked():
    # Получаем имя пользователя, пароль и телефон
    username = username_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()
    remember_me = remember_var.get()  # Получаем состояние чекбокса
    option_menu = selected_option.get()

    # Записываем данные в текстовый файл с поддержкой русских символов
    with open('user_data.txt', 'a', encoding='utf-8') as file:
        file.write(f'Имя: {username}, Пароль: {password}, Телефон: {phone}, Запомнить меня: {remember_me}n')

    # Выводим в диалоговое окно сообщение об успешной записи
    messagebox.showinfo('Успех', 'Данные успешно сохранены!')


# Обработчик для смены фона
def change_background():
    window.config(bg='black')
    main_label.config(bg='black', fg='white')
    username_label.config(bg='black', fg='white')
    password_label.config(bg='black', fg='white')
    phone_label.config(bg='black', fg='white')
    remember_me_checkbox.config(bg='black', fg='white')
    send_btn.config(bg='gray')







image_label = Label(window)
image_label.pack(pady=(10, 0))

# Заголовок формы
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# Метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()

# Поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# Метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()

# Поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry, show='*')  # show='*' скрывает вводимые символы
password_entry.pack()

# Метка для поля ввода телефона
phone_label = Label(window, text='Телефон', font=label_font, **base_padding)
phone_label.pack()

# Поле ввода телефона
phone_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
phone_entry.pack()

# Чекбокс "Запомнить меня"
remember_me_checkbox = Checkbutton(window, text='Запомнить меня', variable=remember_var, font=label_font)
remember_me_checkbox.pack(**base_padding)

increase_font_btn = Button(window, text='Увеличить размер шрифта', command=increase_font_size)
increase_font_btn.pack(**base_padding)

# Кнопка "Войти"
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Новое окно")
    new_window.geometry("1500x1600")

    label = Label(new_window, text="Добро пожаловать!", font=('Arial', 14))
    label.pack(pady=20)


def open_website():
    webbrowser.open("https://www.example.com")

parse_btn = Button(window, text="Парсить сайт", command=parse_website)
parse_btn.pack(**base_padding)

def parse_website():
    url = "https://www.exampie.com"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.txet,"html.parser")

        headers = soup.find_all("h1")

        for header in headers:
            print(header.text)

# Запуск основного цикла приложения
window.mainloop()