import tkinter as tk
import math

calculator = tk.Tk()

calculator.geometry("450x450")
calculator.title("Calculator")

calculation = ""


def addToCalc(char):
    global calculation
    calculation += str(char)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)


def evalCalc():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        cancelCalc()
        textResult.insert(1.0, "Error!")


def cancelCalc():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


buttonFrame = tk.Frame(calculator)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

button1 = tk.Button(buttonFrame, text="+", font=('Arial', 16), command=lambda: addToCalc("+"))
button1.grid(row=0, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="-", font=('Arial', 16), command=lambda: addToCalc("-"))
button1.grid(row=0, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="*", font=('Arial', 16), command=lambda: addToCalc("*"))
button1.grid(row=0, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="/", font=('Arial', 16), command=lambda: addToCalc("/"))
button1.grid(row=0, column=3, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="^", font=('Arial', 16), command=lambda: addToCalc("**"))
button1.grid(row=1, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="√", font=('Arial', 16), command=lambda: addToCalc("math.sqrt("))
button1.grid(row=1, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="log10", font=('Arial', 16), command=lambda: addToCalc("math.log10("))
button1.grid(row=1, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="(", font=('Arial', 16), command=lambda: addToCalc("("))
button1.grid(row=1, column=3, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="7", font=('Arial', 16), command=lambda: addToCalc("7"))
button1.grid(row=2, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="8", font=('Arial', 16), command=lambda: addToCalc("8"))
button1.grid(row=2, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="9", font=('Arial', 16), command=lambda: addToCalc("9"))
button1.grid(row=2, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text=")", font=('Arial', 16), command=lambda: addToCalc(")"))
button1.grid(row=2, column=3, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="4", font=('Arial', 16), command=lambda: addToCalc("4"))
button1.grid(row=3, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="5", font=('Arial', 16), command=lambda: addToCalc("5"))
button1.grid(row=3, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="6", font=('Arial', 16), command=lambda: addToCalc("6"))
button1.grid(row=3, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="!", font=('Arial', 16), command=lambda: addToCalc("math.factorial("))
button1.grid(row=3, column=3, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="1", font=('Arial', 16), command=lambda: addToCalc("1"))
button1.grid(row=4, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="2", font=('Arial', 16), command=lambda: addToCalc("2"))
button1.grid(row=4, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="3", font=('Arial', 16), command=lambda: addToCalc("3"))
button1.grid(row=4, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="=", font=('Arial', 16), command=evalCalc)
button1.grid(row=4, column=3, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="π", font=('Arial', 16), command=lambda: addToCalc("math.pi"))
button1.grid(row=5, column=0, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="0", font=('Arial', 16), command=lambda: addToCalc("0"))
button1.grid(row=5, column=1, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text=".", font=('Arial', 16), command=lambda: addToCalc("."))
button1.grid(row=5, column=2, sticky=tk.W + tk.E)

button1 = tk.Button(buttonFrame, text="C", font=('Arial', 16), command=cancelCalc)
button1.grid(row=5, column=3, sticky=tk.W + tk.E)

buttonFrame.pack(fill='x')

textResult = tk.Text(calculator)
textResult.pack()

label = tk.Entry(calculator)
label.pack()

calculator.mainloop()
