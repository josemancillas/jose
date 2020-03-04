#Lab 5
#Mancill1           and    nbassyon

#import tkinter library
import tkinter as tk

#constants for drop menu
OPTIONS = ["minutes", "hours", "days"]

class SecondsConverterClass():
    def __init__(self):
        #Creates the main window and title
        self.root = tk.Tk()
        root = self.root
        root.title("Seconds Converter")
        root.geometry('400x400')
        root.configure(bg='pink')
        #Limits or enables the ability to resize the window (by default 1)
        root.resizable(1,1)

        #Labels
        self.secondsToConvertLabel = tk.Label(master=root, bg= 'pink', text = 'Seconds to Convert').grid(row = 1, column = 0, sticky='w')
        self.convertToLabel = tk.Label(master=root, bg= 'pink', text = 'Convert to').grid(row = 2, column = 0, sticky='w')
        self.resultLabel = tk.Label(master=root, bg= 'pink', text = 'Result').grid(row = 3, column = 0, sticky='w')

        #Text Box Entries
        self.secondsEntry = tk.Entry(master=root, width=20, bg = 'pink', justify = 'left')
        self.secondsEntry.grid(row = 1, column = 1, sticky = 'w')

        #Creates the drop down menu variable
        self.dropVariable = tk.StringVar()
        dropVariable = self.dropVariable
        dropVariable.set(OPTIONS[0]) #Sets the default value to minutes
        self.optionsMenu = tk.OptionMenu(root,dropVariable,*OPTIONS).grid(row = 2, column = 1, sticky='w')

        #Creating the text variable for the Result label
        self.resultVariable = tk.IntVar()
        resultVariable = self.resultVariable
        #resultVariable.set()
        self.resultDisplayLabel= tk.Label(master=root, bg= 'pink', textvariable = resultVariable).grid(row = 3, column = 1, sticky= 'w')

        #Buttons
        #Convert calls the compute function, while quit destroys the GUI with root.destroy as a command
        self.convertButton= tk.Button(master=root, text = 'Convert', width = 10, fg='pink', command = self.computeFunction).grid(row = 6, column = 0, sticky = 'e')
        self.quitButton= tk.Button(master=root, text = 'Quit', width = 10, fg='pink', command = root.destroy).grid(row = 6, column = 1, sticky = 'e')

    #Functions
    def computeFunction(self):
        self.seconds = self.secondsEntry.get()
        seconds = self.seconds
        self.dropOption = self.dropVariable.get()
        resultVariable = self.resultVariable
        
        self.invalid = self.notNumeric(seconds)
        if self.invalid == False:
            resultVariable.set('Invalid Input')

        elif self.dropOption == 'minutes':
            newMinutes = self.secToMinutes(int(seconds))
            resultVariable.set(int(newMinutes))
            
        elif self.dropOption == 'hours':
            newHours = self.secToHours(int(seconds))
            resultVariable.set(int(self.newHours))
            
        elif self.dropOption == 'days':
            newDays = self.secToDays(int(seconds))
            self.resultVariable.set(int(self.newDays))

    def secToMinutes(self,seconds):
        #This only occurs if the minutes option is chosen
        self.newMinutes = seconds / 60
        return self.newMinutes

    def secToHours(self,seconds):
        #This only occurs if the hours option is chosen
        self.newHours = seconds / 3600
        return self.newHours

    def secToDays(self,seconds):
        #This only occurs if the days option is chosen
        self.newDays = seconds / 86400
        return self.newDays

    def notNumeric(self,seconds):
        #This function checks if theres anything more than just numbers
        seconds = str(seconds)
        if seconds.isnumeric() == False:
            return False
        else:
            return True

if __name__ == '__main__':
    SecondsConverterClass()
