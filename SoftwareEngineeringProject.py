# Main Controlling Class for the system.
import os
import unittest
import datetime
import random


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
        self.startMenuOptions = [1, 2, 3]
        self.startSelection = 1

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
            self._makeDefaultPlans(data_path, "DIRECTORY")
            exit(-1)
        elif not os.path.exists(data_path):
            print(f"The data file {data_path} couldn't be found!"
                  "\n\nPlease create a list of retirement plans and put it in the /data directory. ")
            self._makeDefaultPlans(data_path, "FILE")
            exit(-1)
        else:
            with open(data_path) as file:
                for i in file.readlines():
                    plans.append(i.split(':'))
        if not plans:
            self._makeDefaultPlans(data_path, "FILE")
        return plans

    def startMenu(self):
        startMenuOptions = [1, 2, 3, 4]
        # This is the main menu for the application. User will make selections from this menu to
        # run the program.
        print(
            "Welcome to the Retirement Calculator!\nMake a selection from the following list to get started.\nTo make a selection, enter the number that corresponds to your intended selection and press enter.")
        print("1. View Retirement Plans\n2. Make a Selection\n3. View employee data\n 4. Exit")
        # This gets the menu selection input from the user
        startSelection = input(int("Please enter the number of your selection: "))
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
        return startSelection

    def getEmployeeName(self):
        # This code gets input for employee name from the user
        employeeName = input("Please enter the employee name: ")
        # This checks that a name was actually given and that it is not too long. 
        # If these tests pass, input is converted to string.
        if employeeName == "":
            print("An employee name was not given.")
            RetirementCalculator.getEmployeeName()
        elif len(employeeName) <= 30:
            print("The provided employee name was too long. Please shorten your input.")
            RetirementCalculator.getEmployeeName()
        else:
            str(employeeName)
        return employeeName

    def getHourlyRate(self):
        # This function gets the hourly rate input from the user
        hourlyRate = input(float("Enter the amount you earn per hour ($ is not necessary): "))
        if hourlyRate <= 0:
            print("The provided hourly rate was invalid. The rate must be a positive number greater than zero.")
            RetirementCalculator.getHourlyRate()
        return hourlyRate

    def getPlanListSelection(self):
        # This function gets the user's selection for retirement plan
        print("Please choose from the following options: ")
        print("1. Basic Plan\n2. Plus Plan\n3. Premium Plan\n4. Platinum Plan")
        planListSelection = input(int("Enter your selection: "))
        if planListSelection == 1:
            return self.retirementPlanList[0]
        elif planListSelection == 2:
            return self.retirementPlanList[1]
        elif planListSelection == 3:
            return self.retirementPlanList[2]
        elif planListSelection == 4:
            return self.planListSelection[3]
        else:
            print("Your input was invalid. Please enter a valid number for your selection.")
            RetirementCalculator.getPlanListSelection()

    def _makeDefaultPlans(self, data_path, error):
        print(data_path)
        if error == 'DIRECTORY':
            os.makedirs(data_path)
        with open(data_path, 'w') as file:
            file.writelines("TestingPlan:84665.141")


class Employee:
    def __init__(self, data):
        self.data = data

        self.plan = None

    def calculateOverInterval(self, date1, date2):
        pass

    def toString(self):
        return f'{self.data}'



class Controller:
    def __init__(self):
        # Current Employee

        self.emp = None
        while True:
            selection = input("enter a value 1-3. \n\n1. Create Employee, \n2. Read Employee Data, \n3. Quit\n\n")

            if selection == '2':
                if self.emp is None:
                    print("You need to create an employee first!")
                    continue
                else:
                    print("Please enter the amount of time worked in minutes.")
                    timeInput = input("Amount of time worked in minutes:")
                    print("Your amount of time worked is " + timeInput + " minutes.")
                    print("Please enter the percentage of hourly pay.")
                    percentInput = input("percentage of hourly pay:")
                    num = percentInput
                    percentage = "{:.0%}".format(float(num))
                    print("your hourly pay is " + percentage)
                    print(self.emp.toString())
                    continue

            if selection == '1':
                data = {'name': input("Please enter the employee's name."),
                        'age': int(input("Please enter the employee's age."))}

                self.emp = Employee(data)

            # print("Please enter the amount of time worked in minutes.")
            # timeInput = input("Amount of time worked in minutes:")
            # print("Your amount of time worked is " + timeInput + " minutes.")
            # print("Please enter the percentage of hourly pay.")
            # percentInput = input("percentage of hourly pay:")
            # num = percentInput
            # percentage = "{:.0%}".format(float(num))
            # print("your hourly pay is " + percentage)


def main():
    Controller()


if __name__ == "__main__":
    main()
