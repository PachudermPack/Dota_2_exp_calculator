import tkinter as tk
import sys
import os
import subprocess

# Создаем главное окно
root = tk.Tk()
root.title("Стартовое меню")
root.geometry("400x150")
root.configure(bg='#2e2e2e')

def resource_path(relative_path):
    """Получение абсолютного пути к файлу внутри сборки или в режиме разработки."""
    if hasattr(sys, '_MEIPASS'):
        # В случае PyInstaller
        base_path = sys._MEIPASS
    else:
        # В режиме разработки
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def start_dif():
    # Путь к исполняемому файлу Dota_2_dif_calc.exe
    dif_exe = resource_path("dota_2_dif_calc.exe")
    print(f"Запуск: {dif_exe}")  # Для отладки
    subprocess.Popen([dif_exe])  # Запуск .exe файла

def start_exp():
    # Путь к исполняемому файлу Dota_2_exp_calc.exe
    exp_exe = resource_path("dota_2_exp_calc.exe")
    print(f"Запуск: {exp_exe}")  # Для отладки
    subprocess.Popen([exp_exe])  # Запуск .exe файла

# Создаем кнопки для запуска этих программ
btn_dif = tk.Button(root, text="Калькулятор разности в опыте", bg='#2e2e2e', fg='ivory', command=start_dif, width=50, height=2)
btn_exp = tk.Button(root, text="Калькулятор опыта и награды", bg='#2e2e2e', fg='ivory', command=start_exp, width=50, height=2)

btn_dif.pack(pady=10)
btn_exp.pack(pady=10)

root.mainloop()