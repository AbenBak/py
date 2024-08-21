import tkinter as tk
import requests
from tkinter import messagebox

# Функция для выполнения запроса к jsonplaceholder
def make_request():
    try:
        user_id = entry.get()  # Получаем ID из поля ввода
        if not user_id.isdigit():
            raise ValueError("ID должно быть числом.")
        
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        
        if response.status_code == 200:
            data = response.json()
            result_text.delete(1.0, tk.END)  # Очищаем текстовое поле перед выводом нового результата
            result_text.insert(tk.END, f"Name: {data['name']}\nEmail: {data['email']}\nCompany: {data['company']['name']}")
            with open(f'user_{user_id}.txt','w') as file:
                file.write(f"Name: {data['name']}\nEmail: {data['email']}\nCompany: {data['company']['name']}")
        else:
            raise ValueError(f"Ошибка: Пользователь с ID {user_id} не найден.")
    
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание основного окна
root = tk.Tk()
root.title("Запрос данных по ID")

# Поле для ввода ID
label = tk.Label(root, text="Введите ID:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для выполнения запроса
button = tk.Button(root, text="Отправить запрос", command=make_request)
button.pack(pady=10)

# Поле для вывода результата
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=10)

# Запуск основного цикла программы
root.mainloop()
