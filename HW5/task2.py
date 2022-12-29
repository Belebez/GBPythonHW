# Создайте программу для игры в ""Крестики-нолики"".


from tkinter import *
from tkinter import messagebox
import random

# создадим окно
root = Tk()
root.title('Python Game')
root.geometry('337x479')
root.resizable(False, False)
label = Label(width=20, text="Игра 'крестики-нолики'", font=('Gabriola', 20, 'bold'))

# функция отключения кнопок
def buttons_disabled():
    global game_left, buttons
    for item in game_left:
        buttons[item].config(state='disabled')


# функция определения победителя
def win(n):
    global game, buttons
    if (game[0] == n and game[1] == n and game[2] == n):
        buttons[0].config(bg='#099E1B')
        buttons[1].config(bg='#099E1B')
        buttons[2].config(bg='#099E1B')
        return True
    elif (game[3] == n and game[4] == n and game[5] == n):
        buttons[3].config(bg='#099E1B')
        buttons[4].config(bg='#099E1B')
        buttons[5].config(bg='#099E1B')
        return True
    elif (game[6] == n and game[7] == n and game[8] == n):
        buttons[6].config(bg='#099E1B')
        buttons[7].config(bg='#099E1B')
        buttons[8].config(bg='#099E1B')
        return True
    elif (game[0] == n and game[3] == n and game[6] == n):
        buttons[0].config(bg='#099E1B')
        buttons[3].config(bg='#099E1B')
        buttons[6].config(bg='#099E1B')
        return True
    elif (game[1] == n and game[4] and game[7] == n):
        buttons[1].config(bg='#099E1B')
        buttons[4].config(bg='#099E1B')
        buttons[7].config(bg='#099E1B')
        return True
    elif (game[2] == n and game[5] == n and game[8] == n):
        buttons[2].config(bg='#099E1B')
        buttons[5].config(bg='#099E1B')
        buttons[8].config(bg='#099E1B')
        return True
    elif (game[0] == n and game[4] == n and game[8] == n):
        buttons[0].config(bg='#099E1B')
        buttons[4].config(bg='#099E1B')
        buttons[8].config(bg='#099E1B')
        return True
    elif (game[2] == n and game[4] == n and game[6] == n):
        buttons[2].config(bg='#099E1B')
        buttons[4].config(bg='#099E1B')
        buttons[6].config(bg='#099E1B')
        return True


# функция нажатия кнопки
def push_button(human):
    global game, game_left, turn, buttons

    game[human] = 'X'
    buttons[human].config(text='X', bg='#DAEBF5', state='disabled')
    game_left.remove(human)

    if human == 4 and turn == 0:
        bot = random.choice(game_left)
    elif human != 4 and turn == 0:
        bot = 4
    if turn > 0:
        if game[6] == 'X' and game[7] == 'X':
            bot = 8
        elif game[6] == 'X' and game[8] == 'X':
            bot = 7
        elif game[6] == 'X' and game[3] == 'X':
            bot = 0
        elif game[6] == 'X' and game[0] == 'X':
            bot = 3
        elif game[0] == 'X' and game[3] == 'X':
            bot = 6
        elif game[0] == 'X' and game[1] == 'X':
            bot = 2
        elif game[0] == 'X' and game[2] == 'X':
            bot = 1
        elif game[2] == 'X' and game[1] == 'X':
            bot = 0
        elif game[2] == 'X' and game[5] == 'X':
            bot = 8
        elif game[8] == 'X' and game[2] == 'X':
            bot = 5
        elif game[8] == 'X' and game[5] == 'X':
            bot = 2
        elif game[8] == 'X' and game[7] == 'X':
            bot = 6
        elif game[3] == 'X' and game[4] == 'X':
            bot = 5
        elif game[5] == 'X' and game[4] == 'X':
            bot = 3
        elif game[1] == 'X' and game[4] == 'X':
            bot = 7
        elif game[7] == 'X' and game[4] == 'X':
            bot = 1
        elif game[4] == 'X' and game[6] == 'X':
            bot = 2
        elif game[4] == 'X' and game[2] == 'X':
            bot = 6
        elif game[4] == 'X' and game[0] == 'X':
            bot = 8
        elif game[4] == 'X' and game[8] == 'X':
            bot = 0
        else:
            bot = 8 - human
    if bot not in game_left:
        try:
            bot = random.choice(game_left)
        except IndexError:
            buttons_disabled()

    game[bot] = 'O'
    buttons[bot].config(text='O', bg='#F5DADA', state='disabled')
    if win('X'):
        messagebox.showinfo('Крестики-нолики', 'Вы выиграли')
        buttons_disabled()
    elif win('O'):
        messagebox.showinfo('Крестики-нолики', 'Вы проиграли')
        buttons_disabled()
    else:
        if len(game_left) > 0:
            game_left.remove(bot)
        else:
            messagebox.showinfo('Крестики-нолики', 'Ничья')
            buttons_disabled()
        turn += 1


# создание кнопок
def reset():
    global game, game_left, turn, buttons

    game = [None] * 9
    game_left = list(range(9))
    turn = 0

    buttons = [Button(width=6, height=1, font=('Gabriola', 30, 'bold'), bg='#4A4D4C', command=lambda x=i: push_button(x) ) for i in range(9)]
    row = 1
    col = 0
    for i in range(9):
        buttons[i].grid(row=row, column=col)
        col += 1
        if col == 3:
            row += 1
            col = 0

# распологаем кнопки
label.grid(row=0, column=0, columnspan=3)

#
b_reset = Button(root, text='Начать заново', command=reset)
b_reset.grid(row=4, column=1, ipadx=2, ipady=2, padx=2, pady=2)

reset()
root.mainloop()

