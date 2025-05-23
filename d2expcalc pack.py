import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Калькулятор опыта Dota 2")
root.configure(bg='#2e2e2e')

# Labels
label_result = tk.Label(root, text="", font=("Arial", 14), fg='ivory', bg='#2e2e2e')
label_allpick_title = tk.Label(root, text="Allpick награда", font=("Arial", 12), fg='ivory', bg='#2e2e2e')
label_allpick = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')
label_turbo_title = tk.Label(root, text="Turbo награда", font=("Arial", 12), fg='ivory', bg='#2e2e2e')
label_turbo = tk.Label(root, text="", justify=tk.LEFT, fg='ivory', bg='#2e2e2e')

# Function to show the calculator interface
def show_calculator():
    # Level input
    label_level = tk.Label(root, text="Введите уровень героя (1-30):", fg='ivory', bg='#2e2e2e')
    label_level.pack(pady=(10, 0))  # Use pack for layout
    entry_level = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_level.insert(0, "1")
    entry_level.pack()

    # Experience input
    label_exp = tk.Label(root, text="Введите оставшийся опыт (если уровень не равен 30):", fg='ivory', bg='#2e2e2e')
    label_exp.pack(pady=(10, 0))
    entry_exp = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_exp.insert(0, "0")
    entry_exp.pack()

    # Kill streak input
    label_streak_input = tk.Label(root, text="Введите серию убийств (от 3 до 10):", fg='ivory', bg='#2e2e2e')
    label_streak_input.pack(pady=(10, 0))
    entry_streak = tk.Entry(root, bg='#1f1f1f', fg='ivory', insertbackground='ivory')
    entry_streak.insert(0, "0")
    entry_streak.pack()

    # Calculate button
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
                exp = 0

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
            elif streak_num_input == 6:
                streak_num_input = 40
            elif streak_num_input == 7:
                streak_num_input = 53.75
            elif streak_num_input == 8:
                streak_num_input = 70
            elif streak_num_input == 9:
                streak_num_input = 88.75
            elif streak_num_input == 10:
                streak_num_input = 110

            # Расчет значения серии убийств * уровень героя
            streak_value = streak_num_input * lvl

            # Уровни (примерные)
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

            total_exp = levels.get(lvl, 0) + exp + streak_value

            base_reward = math.floor(100 + total_exp * 0.13 + streak_value)

            allpick_rewards = []
            reward_for_1_player = base_reward
            allpick_rewards.append(f"1 игроку - {reward_for_1_player:.1f}")
            for i in range(2, 6):
                reward_value = base_reward / i
                allpick_rewards.append(f"между {i} - {reward_value:.1f}")

            turbo_rewards = []
            reward_for_1_player_turbo = base_reward * 2
            turbo_rewards.append(f"1 игроку - {reward_for_1_player_turbo:.1f}")
            for i in range(2, 6):
                reward_value = (base_reward * 2) / i
                turbo_rewards.append(f"между {i} - {reward_value:.1f}")

            # Update labels and show them
            label_result.config(text=f"Общий опыт: {total_exp}")

            label_allpick.config(text="\n".join(allpick_rewards))
            label_turbo.config(text="\n".join(turbo_rewards))

            # Show labels
            label_result.pack(pady=(10, 2))

            label_allpick_title.pack(pady=(10, 2))
            label_allpick.pack(pady=(2, 10))

            label_turbo_title.pack(pady=(10, 2))
            label_turbo.pack(pady=(2, 10))

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    btn_calc = tk.Button(root, text="Рассчитать", command=calculate, bg='#2e2e2e', fg='ivory', activebackground='#3a3a3a', activeforeground='ivory')
    btn_calc.pack(pady=10)

# Call the calculator display function without a start button
show_calculator()

root.mainloop()