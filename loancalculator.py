from tkinter import *

class LoanCalculator:
    def __init__(self): # a method in python class constructor
        window = Tk() # used to create the interface/window to house the calculator
        window.title("Loan Calculator")
        window.configure(background = "light blue") # background color for the application window
        
        # adding all the labels (Label function creates display box to take input and
        # the grid method gives it a table like structure)
        Label(window, font='Helvetica 12 bold', bg="light green",
        text="Annual Interest Rate").grid(row=1, column=1, sticky=W) # we want the label to appear in table=like structure
        Label(window, font='Helvetica 12 bold', bg="light green",
        text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green",
        text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green",
        text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green",
        text="Total Payment").grid(row=5, column=1, sticky=W)

        # creating objects:
        # 'self' is used to represent an instance of a variable. When we put a 'self' in front of a variable,
        # it means we can reference that instance anywhere within the code
        self.annualInterestRateVar = StringVar() # object
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2) # accepting inputs using Entry function
        self.numberofYearsVar = StringVar() # object
        Entry(window, textvariable=self.numberofYearsVar, justify=RIGHT).grid(row=2, column=2) # accepting inputs
        self.loanAmountVar = StringVar() # object
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2) # accepting inputs
        # Display values:
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font='Helvetica 12 bold', bg="light green",
        textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg="light green",
        textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        # creating buttons that compute and erase inputs
        btnComputePayment = Button(window, text="Compute Payment", bg="red", fg="white", font='Helvetica 14 bold',
        command=self.computePayment).grid(row=6, column = 2, sticky=E)
        btnClear = Button(window, text="Clear", bg="blue", fg="white", font='Helvetica 14 bold',
        command=self.delete_all).grid(row=7, column = 8, padx=20, pady=20, sticky=E)

        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200 ,
            int(self.numberofYearsVar.get())
        )
        
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberofYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1 + monthlyInterestRate)** (numberofYears * 12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")

LoanCalculator()