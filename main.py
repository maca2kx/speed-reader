import tkinter as tk
from tkinter import messagebox
import time
from sample_quotes import quotes

class GUI(tk.Canvas):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.winfo_toplevel().title('Speed Reader')
        self.intro = '''This is a test sentence'''
        self.instructions = '''Have you ever wondered how fast you read? Or how fast you can read? On average, adults can read between 200-300 words per minute but this can be massively increased by focusing on one word at a time. Paste your own text into the text box or just click submit for a sample quote to try it out!'''
        self.outtext = tk.StringVar()
        self.wpm = tk.StringVar()
        self.wpm.set('400wpm')
        self.cont = False

        # Title
        self.lbl_title = tk.Label(master=root, text='Speed Reader', font=('Georgia', 22))
        self.lbl_title.pack()

        # Instructions
        self.lbl_instructions = tk.Label(master=root, text=self.instructions, font=('Arial', 12), justify=tk.CENTER, wraplength=580)
        self.lbl_instructions.pack()

        # Output
        self.frm_output_container = tk.Frame(master=root)
        self.frm_output = tk.Frame(master=self.frm_output_container, borderwidth=2, relief='solid')
        self.lbl_output = tk.Label(master=self.frm_output, width=35, font=('Arial', 22), textvariable=self.outtext)

        # WPM
        self.frm_wpm = tk.Frame(master=self.frm_output_container)
        self.txt_wpm = tk.Label(master=self.frm_wpm, textvariable=self.wpm, justify='center')
        self.wpm_decrease = tk.Button(master=self.frm_wpm, text='-', relief='flat', justify='center', width=3, font=('Arial', 16), command=self.decrease)
        self.wpm_increase = tk.Button(master=self.frm_wpm, text='+', relief='flat', justify='center', width=3, font=('Arial', 16), command=self.increase)

        # Grid layout for output frame
        self.frm_output_container.columnconfigure(0, weight=4)
        self.frm_output_container.columnconfigure(1, weight=1)
        self.frm_output_container.pack(fill=tk.X, padx=10)
        self.frm_output.grid(row=0, column=0)
        self.lbl_output.grid(row=0, column=0)
        self.frm_wpm.columnconfigure([0,1], weight=1)
        self.frm_wpm.grid(row=0, column=1, sticky='e')
        self.txt_wpm.grid(row=0, column=0, columnspan=2, sticky='s')
        self.wpm_decrease.grid(row=1, column=0)
        self.wpm_increase.grid(row=1, column=1)

        # Input
        self.txt_input = tk.Text(master=root, height=10, wrap=tk.WORD)
        self.txt_input.pack(padx=10)

        # Submit button
        self.frm_bottom = tk.Frame(master=root)
        self.btn_end = tk.Button(master=self.frm_bottom, command=self.end, text='Cancel', width=10, height=2)
        self.btn_submit = tk.Button(master=self.frm_bottom, command=self.run, text='Submit', bg='black', fg='white', width=10, height=2)

        self.frm_bottom.columnconfigure([0,1], weight=1)
        self.frm_bottom.pack(side=tk.RIGHT, padx=10)
        self.btn_end.grid(row=0, column=0, sticky='w', padx=10)
        self.btn_submit.grid(row=0, column=1, sticky='e', padx=10, pady=5)

    def end(self):
        self.cont = False

    def decrease(self):
        wpm = self.get_wpm() - 50
        if wpm <= 0:
            wpm = 50

        self.wpm.set(f'{wpm}wpm')

    def increase(self):
        wpm = self.get_wpm() + 50
        self.wpm.set(f'{wpm}wpm')

    def get_wpm(self):
        return int(self.wpm.get()[:-3])

    def run(self):
        if self.txt_input.get('1.0', 'end') != '\n':
            words = self.txt_input.get('1.0', 'end').split()
        else:
            words = quotes[0].split()

        delay = 1 / (self.get_wpm() / 60)

        self.cont = True
        for word in words:
            if self.cont == True:
                self.outtext.set(word)
                self.update()

            else:
                break

            time.sleep(delay)
        self.cont = False

        self.outtext.set('')

if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root, width=600, bg='black')
    root.mainloop()
