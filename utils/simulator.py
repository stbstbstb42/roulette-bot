import tkinter as tk
import random

class Roulette:
    def __init__(self, master):
        self.master = master
        master.title("Roulette")
        master.geometry("400x400")

        # Crea il frame per i numeri della roulette
        self.numbers_frame = tk.Frame(master)
        self.numbers_frame.pack(pady=20)

        # Crea i pulsanti per i numeri
        self.number_buttons = []
        for i in range(37):
            button = tk.Button(self.numbers_frame, text=str(i), width=2, height=1, command=lambda i=i: self.select_number(i))
            self.number_buttons.append(button)
            button.grid(row=i//4, column=i%4, padx=5, pady=5)

        # Crea gli elementi per le puntate
        self.bet_frame = tk.Frame(master)
        self.bet_frame.pack(pady=20)

        self.bet_label = tk.Label(self.bet_frame, text="Puntata:")
        self.bet_label.pack(side=tk.LEFT, padx=5)

        self.bet_entry = tk.Entry(self.bet_frame, width=10)
        self.bet_entry.pack(side=tk.LEFT, padx=5)

        # Crea il menu a tendina per il tipo di puntata
        self.bet_type = tk.StringVar(value="Numero")
        self.bet_type_dropdown = tk.OptionMenu(self.bet_frame, self.bet_type, "Numero", "Rosso", "Nero", "Pari", "Dispari")
        self.bet_type_dropdown.pack(side=tk.LEFT, padx=5)

        # Crea il pulsante per la conferma della puntata
        self.place_bet_button = tk.Button(self.bet_frame, text="Punta!", command=self.place_bet)
        self.place_bet_button.pack(side=tk.LEFT, padx=5)

        # Crea l'etichetta per il bilancio
        self.balance_label = tk.Label(master, text="Balance: 0")
        self.balance_label.pack(pady=20)

        # Crea il pulsante per far girare la roulette
        self.spin_button = tk.Button(master, text="Gira!", command=self.spin_roulette)
        self.spin_button.pack()

        # Inizializza le variabili di stato del gioco
        self.selected_number = None
        self.bet_amount = 0
        self.balance = 0

    def select_number(self, number):
        self.selected_number = number

    def place_bet(self):
        try:
            self.bet_amount = int(self.bet_entry.get())
            if self.bet_amount <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Errore", "Inserisci una puntata valida.")
        else:
            self.balance -= self.bet_amount
            self.update_balance()

    def spin_roulette(self):
        if self.selected_number is None:
            tk.messagebox.showerror("Errore", "Seleziona un numero.")
            return

        if self.bet_amount <= 0:
            tk.messagebox.showerror("Errore", "Inserisci una puntata valida.")
            return

        result = random.randint(0, 36)
        winnings = 0

        if self.bet_type.get() == "Numero":
            if result == self.selected_number:
                winnings = 36*self.bet_amount
                self.balance += winnings
                tk.messagebox.showinfo("Risultato", f"Hai vinto {winnings}!")
            else:
                self.update_balance()
                tk.messagebox.showinfo("Risultato", "Hai perso.")
        elif self.bet_type.get() == "Rosso":
            if result in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
                winnings = self.bet_amount
                self.balance += winnings
                tk.messagebox.showinfo("Risultato", f"Hai vinto {winnings}!")
            else:
                self.update_balance()
                tk.messagebox.showinfo("Risultato", "Hai perso.")
        elif self.bet_type.get() == "Nero":
            if result in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
                winnings = self.bet_amount
                self.balance += winnings
           



    def update_balance(self):
        self.balance_label.config(text=f"Balance: {self.balance}")

root = tk.Tk()
roulette = Roulette(root)
root.mainloop()