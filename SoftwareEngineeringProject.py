# Main Controlling Class for the system.
import os


class RetirementCalculator:
    def __init__(self):
        self.employee = self.makeEmployee({})
        self.totalContributions = None
        self.companyContribution = None
        self.employeeContribution = None
        self.paidToEmployee = None
        self.hourlyPercentage = None
        self.hoursWorked = None
        self.dataDirectory = "/data"
        self.planListSelection = 0
        self.employeeName = None
        self.hourlyRate = None
        self.startMenuOptions = None
        self.startSelection = None
        self.retirementPlanList = []
        self.absoluteDataDirectory = os.path.dirname(__file__)
        self.retirementPlanList = self.readPlans()

    # Gets the data for the currently set employee.
    # Returns true if the
    def getEmployeeData(self):
        """Get the data associated with the current employee and return a dictionary with keys data and status."""
        return_value = {"data": [], "status": False}

        try:
            self.retirementPlanList = self.readPlans()
        except IOError:
            return_value["status"] = False

        if self.employee.plan not in self.retirementPlanList:
            return_value["status"] = False
        else:
            return_value["data"] = self.employee.toString()
            return_value["status"] = True

        return return_value

    def makeEmployee(self, param):
        return Employee(param)
        pass

    def readPlans(self):
        # Gets the plans from the retirement_plans text file which stores plans with attributes split by :
        # Example retirement plan would be planName:benefits
        plans = []
        testing = ''
        # Replace forward slashes with backslashes in the data directory string.
        data_dir = self.absoluteDataDirectory + '\\' + "".join([i.replace('/', '\\') for i in self.dataDirectory])
        data_path = data_dir + "\\retirement_plans.txt"
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
            print("The data file couldn't be found!"
                  "\n\nPlease create a list of retirement plans and put it in the /data directory. ")
            exit(-1)
        elif not os.path.exists(data_path):
            print(f"The data file {data_path} couldn't be found!"
                  "\n\nPlease create a list of retirement plans and put it in the /data directory. ")
            exit(-1)
        else:
            with open(data_path) as file:
                for i in file.readlines():
                    plans.append(i.split(':'))
        return plans
    
    def startMenu():
        startMenuOptions = [1, 2, 3, 4]
        # This is the main menu for the application. User will make selections from this menu to
        # run the program.
        print("Welcome to the Retirement Calculator!\nMake a selection from the following list to get started.\nTo make a selection, enter the number that corresponds to your intended selection and press enter.")
        print("1. View Retirement Plans\n2. Make a Selection\n3. View employee data\n 4. Exit")
        # This gets the menu selection input from the user
        startSelection = input("Please enter the number of your selection: ")
        # The following code checks the input for the start menu and calls functions for various menu selections
        if startSelection in startMenuOptions:
            if startSelection == 1:
                RetirementCalculator.readPlans()
            elif startSelection == 2:
                RetirementCalculator.getEmployeeName()
                RetirementCalculator.getPlanListSelection()
            elif startSelection == 3:
                RetirementCalculator.getEmployeeData()
            elif startSelection == 4:
                quit()
            else:
                print("Your selection was invalid. Make sure you enter a valid number.")
                RetirementCalculator.startMenu()
        else:
            print("Your selection was invalid. Make sure you enter a valid number.")
            RetirementCalculator.startMenu()
class Employee:
    def __init__(self, param):
        self.plan = None

    def calculateOverInterval(self, date1, date2):
        pass

    def toString(self):
        pass
