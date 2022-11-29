# Main Controlling Class for the system.
import os
from sys import exit

def _makeDefaultPlans(data_path, error):
    print(error)
    if error == 'DIRECTORY':
        os.makedirs(data_path)
        return
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
        self.retirementPlanList = [0, 1, 2, 3]
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
        # Replace forward slashes with backslashes in the data directory string.
        data_dir = self.absoluteDataDirectory + "\\data\\"
        data_path = data_dir + "retirement_plans.txt"
        if not os.path.exists(data_dir):
            _makeDefaultPlans(data_dir, "DIRECTORY")
        if not os.path.exists(data_path):
            _makeDefaultPlans(data_path, "FILE")
        with open(data_path) as file:
            for i in file.readlines():
                plans.append(i.split(':'))
        return plans

    def getEmployeeName(self):
        # This code gets input for employee name from the user
        employeeName = input("Please enter the employee name: ")
        # This checks that a name was actually given and that it is not too long. 
        # If these tests pass, input is converted to string.
        if employeeName == "":
            print("An employee name was not given.")
            self.getEmployeeName()
        elif len(employeeName) >= 30:
            print("The provided employee name was too long. Please shorten your input.")
            self.getEmployeeName()
        else:
            str(employeeName)
        return employeeName

    def getHourlyRate(self):
        hourlyRate = 0
        # This function gets the hourly rate input from the user
        try:
            hourlyRate = float(input("Enter the amount you earn per hour ($ is not necessary): "))
            if hourlyRate <= 0:
                print("Please provide an hourly rate greater than zero.")
            else:
                return hourlyRate 
        except ValueError:
            print("Please provide a valid number for hourly rate.")
            self.getHourlyRate()

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
        rc.employeeName = rc.getEmployeeName()
        emp_salary = rc.getHourlyRate()
        plans = rc.readPlans()
        emp_plan = plans[0]
        emp_time = 0
        for acc, i in enumerate(plans):
            i.append(i.pop().replace("\n", ""))
            print(f'{acc} {i} Name, Employee Contribution %, Company Contribution %')
        while True:
            try:
                target_plan = int(input("Please choose a plan:"))
            except ValueError:
                continue
            if target_plan in rc.retirementPlanList:
                emp_plan = plans[target_plan]
                break
        while True:
            try:
                emp_time = float(input("How many hours did the employee work?"))
                break
            except ValueError:
                continue

        while True:
            emp_add = input("Additional salary percentage contributed? y/n?")
            if emp_add.lower() == 'y':
                while True:
                    try:
                        emp_add = float(input("Enter the additional salary percentage:"))
                        break
                    except ValueError:
                        continue
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
            emp_cont = (float(emp_salary) * (float(emp_plan[1]) + 1) * float(emp_time)) + float(emp_add) * float(
                emp_salary)
            payout = (float(emp_salary) * (float(emp_plan[2]) + 1) * emp_time) + float(emp_salary) * float(
                emp_time)
            company_cont = float(emp_salary) * (float(emp_plan[2]) + 1) * float(emp_time)
            total_cont = emp_cont + emp_cont
            if datapoint == "1":

                print(f'Total Amount Paid to Employee by Company: ${payout}')
            elif datapoint == "2":

                print(f'Amount Contributed by Employee: ${emp_cont}')
            elif datapoint == "3":

                print(f'Amount Contributed by Company: ${company_cont}')
            elif datapoint == "4":

                # (float(emp_salary) * (float(emp_plan[2]) + 1) * float(emp_time)) + (
                #                        float(emp_salary) * (float(emp_plan[1]) + 1) * float(emp_time))
                print(f'Total Amount Saved by {rc.employeeName} after {emp_time} hours: ${total_cont}')


def main():
    Controller()


if __name__ == "__main__":
    main()
