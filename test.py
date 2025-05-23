python
import tkinter as tk
from tkinter import messagebox

levels = {
    1: 0, 2: 240, 3: 640, 4: 1160, 5: 1760,
    6: 2440, 7: 3200, 8: 4000, 9: 4900, 10: 5900,
    11: 7000, 12: 8200, 13: 9500, 14: 10900, 15: 12400,
    16: 14000, 17: 15700, 18: 17500, 19: 19400, 20: 21400,
    21: 23600, 22: 26000, 23: 28600, 24: 31400, 25: 34400,
    26: 38400, 27: 43400, 28: 49400, 29: 56400, 30: 63900,
}

# Start Menu Functions
def start_dif():
    show_calculator_dif()

def start_exp():
    show_calculator()

def show_calculator():
    calculator = tk.Toplevel(root)
    calculator.title("Калькулятор опыта Dota 2") 
    calculator.configure(bg='#2e2e2e')

    # Ввод уровня
    label_level = tk.Label(calculator, text="Введите уровень героя (1-30):", fg='ivory', bg='#2e2e2e')
    label_level.grid(row=0, column=0, padx=10, sticky='w')
    entry_level = tk.Entry(calculator, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_level.insert(0, "1")
    entry_level.grid(row=0, column=1)

    # Ввод опыта
    label_exp = tk.Label(calculator, text="Введите оставшийся опыт (если уровень не равен 30):", fg='ivory', bg='#2e2e2e')
    label_exp.grid(row=1, column=0, padx=10, sticky='w')
    entry_exp = tk.Entry(calculator, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_exp.insert(0,"0")
    entry_exp.grid(row=1, column=1)

    # Ввод серии убийств
    label_streak_input = tk.Label(calculator, text="Введите серию убийств (от 3 до 10):", fg='ivory', bg='#2e2e2e')
    label_streak_input.grid(row=2, column=0, padx=10, sticky='w')
    entry_streak = tk.Entry(calculator, bg='#1f1f1f', fg='ivory', insertbackground='ivery')
    entry_streak.insert(0,"0")
    entry_streak.grid(row=2, column=1)

    # Метки для результатов
    label_result = tk.Label(calculator, text="", font=("Arial",14), fg='ivory', bg='#2e2e2e')
    label_allpick_title = tk.Label(calculator, text="Allpick награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
    label_allpick = tk.Label(calculator, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')
    label_turbo_title = tk.Label(calculator, text="Turbo награда", font=("Arial",12), fg='ivory', bg='#2e2e2e')
    label_turbo = tk.Label(calculator, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')

    # Функция для расчетов
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

            # Обработка серии убийств
            if not streak_str.isdigit():
                raise ValueError("Введите целое число для серии убийств.")
            streak_num_input = int(streak_str)
            if streak_num_input < 3 or streak_num_input > 10:
                messagebox.showerror("Ошибка", "Серия убийств должна быть от 3 до 10")
                return

            # Добавление опыта из серии убийств
            total_exp = levels.get(lvl,0) + exp + (streak_num_input * lvl)
            base_reward = math.floor(100 + total_exp *0.13 + (streak_num_input * lvl))

            allpick_rewards=[]
            reward_for_1_player=base_reward
            for i in range(1,6):
                if i == 1:
                    allpick_rewards.append(f"1 игроку - {reward_for_1_player:.1f}")
                else:
                    reward_value = base_reward / i
                    allpick_rewards.append(f"между {i} - {reward_value:.1f}")

            turbo_rewards=[]
            for i in range(1,6):
                if i == 1:
                    reward_value = (base_reward * 2)
                    turbo_rewards.append(f"1 игроку - {reward_value:.1f}")
                else:
                    reward_value = (base_reward * 2) / i
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