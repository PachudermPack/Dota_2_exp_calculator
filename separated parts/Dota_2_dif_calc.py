import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Калькулятор разности опыта Dota 2")
root.configure(bg='#2e2e2e')

# Метки для результатов
label_result1 = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
label_result2 = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
label_difference = tk.Label(root, text="", font=("Arial",14,"bold"), fg='ivory', bg='#2e2e2e')

def main():
    print("Запуск Dota_2_dif_calc")

if __name__ == "__main__":
    main()

def show_calculator():
    # Общие параметры для полей и кнопок
    entry_bg_color = '#1f1f1f'  # Цвет фона для полей ввода
    text_color = 'ivory'        # Цвет текста
    button_bg_color = '#2e2e2e' # Цвет фона для кнопки

    # Первая группа ввода (исходный уровень)
    label_level1 = tk.Label(root, text="Введите исходный уровень героя (1-30):", fg=text_color, bg='#2e2e2e')
    label_level1.grid(row=0, column=0, padx=10, sticky='w')
    entry_level1 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_level1.insert(0, "1")
    entry_level1.grid(row=0, column=1)

    label_exp1 = tk.Label(root, text="Введите исходный опыт (если уровень не равен 30):", fg=text_color, bg='#2e2e2e')
    label_exp1.grid(row=1, column=0, padx=10, sticky='w')
    entry_exp1 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_exp1.insert(0,"0")
    entry_exp1.grid(row=1, column=1)

    # Вторая группа ввода (новый уровень)
    label_level2 = tk.Label(root, text="Введите новый уровень героя (1-30):", fg=text_color, bg='#2e2e2e')
    label_level2.grid(row=2, column=0, padx=10, sticky='w')
    entry_level2 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_level2.insert(0, "1")
    entry_level2.grid(row=2, column=1)

    label_exp2 = tk.Label(root, text="Введите оставшийся опыт (если уровень не равен 30):", fg=text_color, bg='#2e2e2e')
    label_exp2.grid(row=3, column=0, padx=10, sticky='w')
    entry_exp2 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_exp2.insert(0,"0")
    entry_exp2.grid(row=3, column=1)

    def calculate():
        try:
            # Исходные данные
            lvl_str_1 = entry_level1.get()
            exp_str_1 = entry_exp1.get()

            # Новые данные
            lvl_str_2 = entry_level2.get()
            exp_str_2 = entry_exp2.get()

            # Проверка и преобразование исходных данных
            if not lvl_str_1.isdigit() or not lvl_str_2.isdigit():
                raise ValueError("Введите целое число для уровней.")
            lvl_1 = int(lvl_str_1)
            lvl_2 = int(lvl_str_2)
            if not exp_str_1.isdigit() or not exp_str_2.isdigit():
                raise ValueError("Введите целое число для опыта.")
            exp_1 = int(exp_str_1)
            exp_2 = int(exp_str_2)

            if not (1 <= lvl_1 <= 30) or not (1 <= lvl_2 <= 30):
                messagebox.showerror("Ошибка", "Уровень должен быть от 1 до 30")
                return

            # Таблица уровней
            levels = {
                1:     0,
                2:   240,
                3:   640,
                4:  1160,
                5:  1760,
                6:  2440,
                7:  3200,
                8:  4000,
                9:  4900,
                10: 5900,
                11: 7000,
                12: 8200,
                13: 9500,
                14:10900,
                15:12400,
                16:14000,
                17:15700,
                18:17500,
                19:19400,
                20:21400,
                21:23600,
                22:26000,
                23:28600,
                24:31400,
                25:34400,
                26:38400,
                27:43400,
                28:49400,
                29:56400,
                30:63900
            }

            # Расчет общего опыта для каждого набора данных с учетом условия
            total_exp_initial = levels.get(lvl_1 ,0) + (0 if lvl_1 ==30 else exp_1)
            total_exp_new = levels.get(lvl_2 ,0) + (0 if lvl_2 ==30 else exp_2)

            # Вывод результатов в отдельные метки
            label_result1.config(text=f"Общий опыт исходного уровня {total_exp_initial}")
            label_result2.config(text=f"Общий опыт нового уровня {total_exp_new}")

            # Расчет разницы
            difference = total_exp_new - total_exp_initial

            # Обновляем и показываем метку разницы
            label_difference.config(text=f"Разница {difference}")
            
            # Размещаем метки на экране
            label_result1.grid(row=5,columnspan=2,pady=(10 ,5))
            label_result2.grid(row=6,columnspan=2,pady=(5 ,5))
            
            # Метка разницы под ними
            label_difference.grid(row=7,columnspan=2,pady=(5 ,10))

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    btn_calc = tk.Button(root,text="Рассчитать", command=calculate,bg=button_bg_color ,fg=text_color ,activebackground=button_bg_color ,activeforeground=text_color )
    btn_calc.grid(row=4,columnspan=2,pady=10)

# Изначально скрываем метки с результатами и разницей
label_result1.grid_remove()
label_result2.grid_remove()
label_difference.grid_remove()

# Вызываем сразу функцию отображения калькулятора без стартового меню
show_calculator()

root.mainloop()