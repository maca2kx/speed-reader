import tkinter as tk
from tkinter import messagebox
import time
#from sample_quotes import quotes
from random import randint

class GUI(tk.Canvas):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.winfo_toplevel().title('Speed Reader')
        self.intro = '''This is a test sentence'''
        self.instructions = 'Have you ever wondered how fast you read? Or how fast you can read? On average, adults can read between 200-300 '
        self.instructions += 'words per minute but this can be massively increased by focusing on one word at a time. Paste your own text into '
        self.instructions += 'the text box or just click submit for a sample quote to try it out!'
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
        if self.txt_input.get('1.0', 'end') != '\n': # use entered text
            words = self.txt_input.get('1.0', 'end').split()
        else: # use random default quote
            quotes = self.get_quotes()
            words = quotes[randint(0, len(quotes)-1)].split()

        delay = 1 / (self.get_wpm() / 60)

        self.cont = True
        for word in words:
            if self.cont == False:
                break

            self.outtext.set(word)
            self.update()

            time.sleep(delay)

        time.sleep(0.5)
        self.outtext.set('')

    def get_quotes(self):
        return (
            'I\'m selfish, impatient, and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can\'t handle me at my worst, then you sure as hell don\'t deserve me at my best',
            'Give me a lever long enough and a fulcrum on which to place it, and I shall move the world',
            'Time is too slow for those who wait, too swift for those who fear, too long for those who grieve, too short for those who rejoice,  but for those who love, time is eternity',
            'Do all the good you can, by all the means you can, in all the ways you can, in all the places you can, at all the times you can, to all the people you can, as long as ever you can',
            'Whoever fights monsters should see to it that in the process he does not become a monster. And if you gaze long enough into an abyss, the abyss will gaze back into you',
            'My friend once called a few house painters to his house for some work. He wanted them to paint his porch. After a few hours the house painters came back for payment as their work was complete. Before leaving they told my friend that they had enjoyed painting his car but it\'s not really a Porsche',
            '''The Pope is super early for his flight. On the way to the airport he asks his driver if he could drive around for a while because they have time to kill and he hasn't driven a car since becoming the pope. Naturally he's a bit rusty so he's driving poorly. Suddenly he sees police lights behind him. He pulls over and when the officer comes up to the window his eyes go wide. He says to the pope "Hold on for a minute," and goes back to his car to radio the chief.
            Cop: "Chief we have a situation. I've pulled over an important figure"
            Chief: "How important? A governor or something?"
            Cop: "No sir, bigger than that"
            Chief: "So, what? A celebrity or something?"
            Cop: "More important, sir"
            Chief: "A major politician?"
            Cop: "No sir, he's much more important"
            Chief: "Well who is it?!"
            Cop: "Well actually I'm not sure, but the pope's his driver"''',
            '''We're no strangers to love
            You know the rules and so do I
            A full commitment's what I'm thinking of
            You wouldn't get this from any other guy
            I just wanna tell you how I'm feeling
            Gotta make you understand
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you'''
            )

if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root, width=600, bg='black')
    root.mainloop()
