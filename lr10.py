'''
Требуется разработать компьютерную игру «крестики-нолики».
Минимальные требования:
1.Графичекский интерфейс (использовать внутреннюю библиотеку питона  tkinter).
2.Игра с приложением (приложение не должно проигрывать)
3. Минимальный комплект программной документации в соответствии с ГОСТ 19 группы:
1.1.Техническое задание
1.2.Пояснительная записка
1.3.Руководство программиста
4. Тестовая документация:
2.1. Mind map
2.2. Чек-лист
2.3. Набор тест-кейсов  
'''
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master  
        self.master.title("Крестики-нолики")  
        self.current_player = "X"  
        self.board = [" " for _ in range(9)] 
        self.buttons = []  
        for i in range(3):
            row = []  
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")  
                row.append(button)  
            self.buttons.append(row) 
        self.reset_button = tk.Button(self.master, text="Новая игра", command=self.reset_game)  
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")  
        
    def on_button_click(self, i, j):
        if self.board[i * 3 + j] == " ": 
            self.board[i * 3 + j] = self.current_player  
            self.buttons[i][j].config(text=self.current_player)  
            if self.check_winner(i, j):  
                messagebox.showinfo("Победа", f"Игрок {self.current_player} выиграл!")  
                self.reset_game()  
            elif " " not in self.board:  
                messagebox.showinfo("Ничья", "Ничья!")  
                self.reset_game()  
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  

    def check_winner(self, i, j):
        row = all(self.board[i*3 + col] == self.current_player for col in range(3))  
        col = all(self.board[row*3 + j] == self.current_player for row in range(3))  
        diag1 = all(self.board[i*3 + i] == self.current_player for i in range(3))  
        diag2 = all(self.board[i*3 + 2-i] == self.current_player for i in range(3))  
        return any([row, col, diag1, diag2])  

    def reset_game(self):
        self.current_player = "X"  
        self.board = [" " for _ in range(9)] 
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")  
                
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
