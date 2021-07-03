import tkinter as tk
import timos_calc_func as tcf


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Multi-Rechner")
        self.geometry("+700+250")

        self.radioVar = tk.IntVar()

        self.eingabeFrame = tk.LabelFrame(self, text="Eingabe")
        self.eingabeFrame.pack(fill=tk.BOTH)
        self.ausgabeFrame = tk.LabelFrame(self, text="Ausgabe")
        self.ausgabeFrame.pack(fill=tk.BOTH)

        self.eingabeLabel = tk.Label(self.eingabeFrame, text="Bitte Zahl eingeben!", font="Courier 16")
        self.eingabeLabel.grid(pady=5, padx=5)

        self.rb1 = tk.Radiobutton(self.eingabeFrame, text="Dezimal zu Binär", variable=self.radioVar, value=0)
        self.rb1.grid()
        self.rb2 = tk.Radiobutton(self.eingabeFrame, text="Binär zu Dezimal", variable=self.radioVar, value=1)
        self.rb2.grid()
        self.rb3 = tk.Radiobutton(self.eingabeFrame, text="Dezimal zu Hexadezimal", variable=self.radioVar, value=2)
        self.rb3.grid()
        self.rb4 = tk.Radiobutton(self.eingabeFrame, text="Hexadezimal zu Dezimal", variable=self.radioVar, value=3)
        self.rb4.grid()

        self.eingabeFeld = tk.Entry(self.eingabeFrame, font="Courier 16", width=16)
        self.eingabeFeld.grid(pady=5, padx=5)
        self.eingabeFeld.focus()

        self.submitButton = tk.Button(self.eingabeFrame, text="Abschicken", command=lambda: self.abschicken())
        self.submitButton.grid(pady=10)

        self.ausgabetextLabel = tk.Label(self.ausgabeFrame, text="Ihr Ergebnis lautet:", font="Arial 16")
        self.ausgabetextLabel.pack(pady=10, padx=10)

        self.ausgabeLabel = tk.Label(self.ausgabeFrame, text="0", font="Arial 18")
        self.ausgabeLabel.pack(pady=10, padx=10)

    def abschicken(self):
        zahl = self.eingabeFeld.get()
        value = self.radioVar.get()
        if value == 0:
            zahl = int(zahl)
            ausgabe = tcf.dezi_to_bin(zahl)
            self.ausgabeLabel.config(text=f"{ausgabe}")
        if value == 1:
            ausgabe = tcf.bin_to_dezi(zahl)
            self.ausgabeLabel.config(text=f"{ausgabe}")
        if value == 2:
            zahl = int(zahl)
            ausgabe = tcf.dezi_to_hex(zahl)
            self.ausgabeLabel.config(text=f"{ausgabe}")
        if value == 3:
            ausgabe = tcf.hex_to_dezi(zahl)
            self.ausgabeLabel.config(text=f"{ausgabe}")


def _main():
    root = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    _main()
