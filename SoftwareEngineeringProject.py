# Main Controlling Class for the system.
import os
import unittest
import datetime
import random


def _makeDefaultPlans(data_path, error):
    print(data_path)
    if error == 'DIRECTORY':
        os.makedirs(data_path)
    with open(data_path, 'w') as file:
        # Plan Name
        # : Percentage of hourly salary that employee contributes
        # : Percentage of hourly salary that company contributes
        file.writelines("Basic Plan:0.05:0.03\nPlus Plan:0.07:0.05\nPremium Plan:0.10:0.08\nPlatinum Plan:0.15:0.10")


class RetirementCalculator:
    def __init__(self):
        self.employee = self.makeEmployee({})
        self.companyContribution = 1
        self.employeeContribution = 1
        self.paidToEmployee = 1
        self.hourlyPercentage = 0.15
        self.hoursWorked = 65
        self.dataDirectory = "/data"
        self.planListSelection = 1
        self.employeeName = "Bob"
        self.hourlyRate = 14
        self.startMenuOptions = None
        self.startSelection = None
        self.retirementPlanList = [1, 2, 3, 4]
        self.absoluteDataDirectory = os.path.dirname(__file__)

        self.startMenuOptions = [1, 2, 3]
        self.startSelection = 1
        self.totalContributions = 2

    # Gets the data for the currently set employee.
    # Returns true if the
    def getEmployeeData(self):
        """Get the data associated with the current employee and return a dictionary with keys data and status."""
        return {"status": True}

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
            _makeDefaultPlans(data_path, "DIRECTORY")
            exit(-1)
        elif not os.path.exists(data_path):
            print(f"The data file {data_path} couldn't be found!"
                  "\n\nPlease create a list of retirement plans and put it in the /data directory. ")
            _makeDefaultPlans(data_path, "FILE")
            exit(-1)
        else:
            with open(data_path) as file:
                for i in file.readlines():
                    plans.append(i.split(':'))
        if not plans:
            _makeDefaultPlans(data_path, "FILE")
        return plans

    def startMenu(self):
        startMenuOptions = [1, 2, 3, 4]
        # This is the main menu for the application. User will make selections from this menu to
        # run the program.
        print(
            "Welcome to the Retirement Calculator!\nMake a selection from the following list to get started.\nTo make "
            "a selection, enter the number that corresponds to your intended selection and press enter.")
        print("1. View Retirement Plans\n2. Make a Selection\n3. View employee data\n 4. Exit")
        # This gets the menu selection input from the user
        startSelection = input(int("Please enter the number of your selection: "))
        # The following code checks the input for the start menu and calls functions for various menu selections
        if startSelection in startMenuOptions:
            if startSelection == 1:
                self.readPlans()
            elif startSelection == 2:
                self.getEmployeeName()
                self.getPlanListSelection()
            elif startSelection == 3:
                self.getEmployeeData()
            elif startSelection == 4:
                quit()
            else:
                print("Your selection was invalid. Make sure you enter a valid number.")
                self.startMenu()
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
        hourlyRate = float(input("Enter the amount you earn per hour ($ is not necessary): "))
        if hourlyRate <= 0:
            print("The provided hourly rate was invalid. The rate must be a positive number greater than zero.")
            self.getHourlyRate()
        return hourlyRate

    def getPlanListSelection(self):
        # This function gets the user's selection for retirement plan
        print("Please choose from the following options: ")
        print("1. Basic Plan"
              "2. Plus Plan"
              "3. Premium Plan"
              "4. Platinum Plan")
        self.retirementPlanList = self.readPlans()
        self.planListSelection = int(input("Enter your selection: "))
        if self.planListSelection == 1:
            return self.retirementPlanList[0]
        elif self.planListSelection == 2:
            return self.retirementPlanList[1]
        elif self.planListSelection == 3:
            return self.retirementPlanList[2]
        elif self.planListSelection == 4:
            return self.retirementPlanList[3]
        else:
            print("Your input was invalid. Please enter a valid number for your selection.")
            self.getPlanListSelection()

    def display(self, param):
        val = ''
        if param == 1:
            val = self.paidToEmployee
        elif param == 2:
            val = self.employeeContribution
        elif param == 3:
            val = self.companyContribution
        elif param == 4:
            val = self.totalContributions
        return val


class Employee:
    def __init__(self, data):
        self.data = data

        self.plan = None

    def calculateOverInterval(self, date1, date2):
        pass

    def toString(self):
        return f'{self.data}'


# Main controlling class.
class Controller:
    def __init__(self):
        rc = RetirementCalculator()
        rc.employeeName = input("Please enter the employee name")
        emp_salary = rc.getHourlyRate()
        plans = rc.readPlans()
        for acc, i in enumerate(plans):
            i.append(i.pop().replace("\n", ""))
            print(f'{acc} {i}')
        emp_plan = plans[int(input("Please choose a plan:"))]
        # Add ability to enter timespan / days / hours
        emp_time = input("How many hours did the employee work?")
        emp_add = input("Additional salary percentage contributed? y/n?")
        while True:
            if emp_add.lower() == 'y':
                emp_add = input("Enter the additional salary percentage:")
                break
            elif emp_add.lower() == 'n':
                emp_add = 0
                break

        while True:
            datapoint = input("What data point would you like to view? \n\n"
                              "1. Total Company payout \n"
                              "2. Employee Contributions \n"
                              "3. Company Contributions \n"
                              "4. Total Contributions \n"
                              "5. Exit")
            if datapoint == "5":
                exit(1)
            if datapoint == "1":
                payout = (float(emp_salary) * (float(emp_plan[2]) + 1) * float(emp_time)) + float(emp_salary) * float(
                    emp_time)
                print(f'Total Amount Paid to Employee by Company: ${payout}')
            elif datapoint == "2":
                emp_cont = (float(emp_salary) * (float(emp_plan[1]) + 1) * float(emp_time)) + float(emp_add) * float(
                    emp_salary)
                print(f'Amount Contributed by Employee: ${emp_cont}')
            elif datapoint == "3":
                company_cont = float(emp_salary) * (float(emp_plan[2]) + 1) * float(emp_time)
                print(f'Amount Contributed by Company: ${company_cont}')
            elif datapoint == "4":
                total_cont = (float(emp_salary) * (float(emp_plan[2]) + 1) * float(emp_time)) + (
                        float(emp_salary) * (float(emp_plan[1]) + 1) * float(emp_time))
                print(f'Total Amount Saved after {emp_time} hours: ${total_cont}')


def main():
    Controller()


if __name__ == "__main__":
    main()
