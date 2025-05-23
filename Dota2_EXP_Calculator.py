import tkinter as tk
import sys
import os
from tkinter import messagebox
import math
levels = {
    1 :    0,  2 :  240,  3 :  640,  4 : 1160,  5 : 1760,
    6 : 2440,  7 : 3200,  8 : 4000,  9 : 4900,  10: 5900,
    11: 7000,  12: 8200,  13: 9500,  14:10900,  15:12400,
    16:14000,  17:15700,  18:17500,  19:19400,  20:21400,
    21:23600,  22:26000,  23:28600,  24:31400,  25:34400,
    26:38400,  27:43400,  28:49400,  29:56400,  30:63900,
}
       
# --- Start Menu Functions ---
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def start_dif():
    show_calculator_dif()

def start_exp():
    show_calculator()

def show_calculator():
    calculator = tk.Toplevel(root)

def show_calculator_diff():
    calculator = tk.Toplevel(root)

def show_calculator_dif():

    root = None
    root = tk.Tk()
    root.title("Калькулятор разности опыта Dota 2")
    root.configure(bg='#2e2e2e')

    label_result1 = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
    label_result2 = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
    label_difference = tk.Label(root, text="", font=("Arial",14,"bold"), fg='ivory', bg='#2e2e2e')

    entry_bg_color = '#1f1f1f'
    text_color = 'ivory'
    button_bg_color = '#2e2e2e'

    # Первая группа ввода (исходный уровень)
    label_level1 = tk.Label(root, text="Введите исходный уровень героя (1-30):", fg=text_color, bg='#2e2e2e')
    label_level1.grid(row=0, column=0, padx=10, sticky='w')
    entry_level1 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_level1.insert(0, "1")
    entry_level1.grid(row=0, column=1)

    label_exp1 = tk.Label(root, text="Введите исходный опыт:", fg=text_color, bg='#2e2e2e')
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

    label_exp2 = tk.Label(root, text="Введите оставшийся опыт:", fg=text_color, bg='#2e2e2e')
    label_exp2.grid(row=3, column=0, padx=10, sticky='w')
    entry_exp2 = tk.Entry(root, bg=entry_bg_color, fg=text_color, insertbackground=text_color)
    entry_exp2.insert(0,"0")
    entry_exp2.grid(row=3, column=1)

    def calculate_dif():
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

    btn_calc = tk.Button(root,text="Рассчитать", command=calculate_dif,bg=button_bg_color ,fg=text_color ,activebackground=button_bg_color ,activeforeground=text_color )
    btn_calc.grid(row=4,columnspan=2,pady=10)

def show_calculator():
    root = None
    root = tk.Tk()
    root.title("Калькулятор опыта Dota 2") 
    root.configure(bg='#2e2e2e')

    
    # Ввод уровня
    label_level = tk.Label(root, text="Введите уровень героя (1-30):", fg='ivory', bg='#2e2e2e')
    label_level.grid(row=0, column=0, padx=10, sticky='w')
    entry_level = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_level.insert(0, "1")
    entry_level.grid(row=0, column=1)

    # Ввод опыта
    label_exp = tk.Label(root, text="Введите оставшийся опыт:", fg='ivory', bg='#2e2e2e')
    label_exp.grid(row=1, column=0, padx=10, sticky='w')
    entry_exp = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_exp.insert(0,"0")
    entry_exp.grid(row=1, column=1)

    # Ввод серии убийств
    label_streak_input = tk.Label(root, text="Введите серию убийств (от 3 до 10):", fg='ivory', bg='#2e2e2e')
    label_streak_input.grid(row=2, column=0, padx=10, sticky='w')
    entry_streak = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_streak.insert(0,"0")
    entry_streak.grid(row=2, column=1)
    # Объявляем глобальные переменные для меток
    label_result = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
    label_allpick_title = tk.Label(root, text="Allpick награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
    label_allpick = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')
    label_turbo_title = tk.Label(root, text="Turbo награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
    label_turbo = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')


    # Изначально скрываем метки (чтобы не мешали)
    label_result.grid_remove()
    label_allpick_title.grid_remove()
    label_allpick.grid_remove()
    label_turbo_title.grid_remove()
    label_turbo.grid_remove()

    def calculate():
        try:
            lvl_str = entry_level.get()
            exp_str = entry_exp.get()
            streak_str = entry_streak.get()

            if not lvl_str.isdigit():
                raise ValueError("Введите целое число для уровня.")
            lvl = int(lvl_str)
            if lvl < 1 or lvl > 30:
                messagebox.showerror("Ошибка", "Уровень должен быть от 1 до 30")
                return
            
            if not exp_str.isdigit():
                raise ValueError("Введите целое число для опыта.")
            exp = int(exp_str)
            if lvl != 30:
                if not exp_str.isdigit():
                    raise ValueError("Введите целое число для опыта.")
                exp = int(exp_str)
            else:
                exp=0

            # Обработка серии убийств
            if not streak_str.isdigit():
                raise ValueError("Введите целое число для серии убийств.")
            streak_num_input = int(streak_str)
            if streak_num_input < 3:
                streak_num_input = 0
            if streak_num_input > 10:
                streak_num_input = 110
            elif streak_num_input == 3:
                streak_num_input = 13.75
            elif streak_num_input == 4:
                streak_num_input = 20
            elif streak_num_input == 5:
                streak_num_input = 28.75
            elif streak_num_input ==6:
                streak_num_input=40
            elif streak_num_input ==7:
                streak_num_input=53.75
            elif streak_num_input ==8:
                streak_num_input=70
            elif streak_num_input==9:
                streak_num_input=88.75
            elif streak_num_input==10:
                streak_num_input=110

            streak_value = streak_num_input * lvl

            total_exp = levels.get(lvl,0) + exp + streak_value

            base_reward = math.floor(100 + total_exp *0.13 + streak_value)

            allpick_rewards=[]
            reward_for_1_player=base_reward
            allpick_rewards.append(f"1 игроку - {reward_for_1_player:.1f}")
            for i in range(2,6):
                reward_value=base_reward/i
                allpick_rewards.append(f"между {i} - {reward_value:.1f}")

            turbo_rewards=[]
            reward_for_1_player_turbo=base_reward*2
            turbo_rewards.append(f"1 игроку - {reward_for_1_player_turbo:.1f}")
            for i in range(2,6):
                reward_value=(base_reward*2)/i
                turbo_rewards.append(f"между {i} - {reward_value:.1f}")

            label_result.config(text=f"Общий опыт: {total_exp}")
            
            label_allpick.config(text="\n".join(allpick_rewards))
            label_turbo.config(text="\n".join(turbo_rewards))
            
            label_result.grid(row=4,columnspan=2,pady=(10,2))
            
            label_allpick_title.grid(row=5,columnspan=2,pady=(10,2))
            label_allpick.grid(row=6,columnspan=2,pady=(2,10))
            
            label_turbo_title.grid(row=7,columnspan=2,pady=(10,2))
            label_turbo.grid(row=8,columnspan=2,pady=(2,10))

        except ValueError as e:
           messagebox.showerror("Ошибка", str(e))

    btn_calc = tk.Button(root, text="Рассчитать", command=calculate, bg='#2e2e2e', fg='ivory', activebackground='#3a3a3a', activeforeground='ivory')
    btn_calc.grid(row=3,columnspan=2,pady=10)

#Start Menu
root = tk.Tk()
root.title("Стартовое меню")
root.geometry("360x120")
root.configure(bg='#2e2e2e')

btn_dif = tk.Button(root, text="Калькулятор разности в опыте", bg='#2e2e2e', fg='ivory', command=start_dif, width=50, height=2)
btn_exp = tk.Button(root, text="Калькулятор опыта и награды", bg='#2e2e2e', fg='ivory', command=start_exp, width=50, height=2)

btn_dif.grid(pady=10)
btn_exp.grid(pady=10)

root.mainloop()
root = tk.Tk()
root.title("Калькулятор опыта Dota 2") 
root.configure(bg='#2e2e2e')

label_result = tk.Label(root, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
label_allpick_title = tk.Label(root, text="Allpick награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
label_allpick = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')
label_turbo_title = tk.Label(root, text="Turbo награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
label_turbo = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')

label_result.grid_remove()
label_allpick_title.grid_remove()
label_allpick.grid_remove()
label_turbo_title.grid_remove()
label_turbo.grid_remove()

