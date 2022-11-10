# Authors: Bryan Hoang, Jarrod Rodgers, and Samuel Williams
# Date: 11/7/22
# Version 1.3
# Project: Software Engineering: Assignment 7 part 2
import time
import unittest
from SoftwareEngineeringProject import *
import datetime
import random


class TestRetirementCalculator(unittest.TestCase):

    def setUp(self):
        self.rc = RetirementCalculator()

    # SUPPORTS REQUIREMENT Non-Functional 1
    # This ensures that the program is written in Python3.
    # The user will check to see if the program is executable by a Python3 interpreter.

    # SUPPORTS REQUIREMENT Non-Functional 2
    # This test checks to ensure the program has been distributed as an .exe file most likely through PyInstaller.
    # The user must look at the type of file being executed, if it's not .exe the test fails.

    # SUPPORTS REQUIREMENT Nonfunctional 3:
    # This tests that the source code is available to users.
    # The user should ensure that "RetirementCalculator.py" is downloaded to their computer.
    # Source code can also serve as documentation due to simplicity of the program.

    # SUPPORTS REQUIREMENT Non-Functional 4.
    # This test checks that the file getCustomerData() method has the sufficient permissions to read the customer data.
    def test_filePermissions(self):
        self.assertEquals(self.rc.getEmployeeData()['status'], True)

    # SUPPORTS REQUIREMENT Non-Functional 5
    # This tests that the program is free.
    # The user shall be able to download the program without paying a
    # fee; it's free and budget constraints were not encountered.

    # SUPPORTS REQUIREMENT Non-Functional 6
    # This tests that there are not any errors during a typical run.
    def test_typicalUseCase(self):
        try:
            self.rc.dataDirectory = '/data'
            self.rc.retirementPlanList = self.rc.readPlans()
            date1 = datetime.date.today()
            date2 = datetime.date(date1.year + random.randint(1, 100), date1.month, date1.day)
            self.rc.planListSelection = random.choice(self.rc.planListSelection)
            self.rc.employee.plan = self.rc.retirementPlanList[self.rc.planListSelection]
            self.rc.employee.CalculateOverInterval(date1, date2)
            self.rc.employee.toString()
        except:
            self.fail()

    # SUPPORTS REQUIREMENT Non-Functional 7
    # This tests that the program is not overly secure.
    # The user shall attempt to access the information generated by the program without authorization and be successful

    # SUPPORTS REQUIREMENT Storage 1:
    # This tests that the user has enough storage to install Python 3
    # The user shall check the amount of free space on their machine before attempting the download and ensure it's
    # greater than 105MB. This information can be found in the storage page of the system settings menu on your machine.

    # SUPPORTS REQUIREMENT Storage Requirement 2
    # This tests that the user downloaded Python 3 from the official site.
    # The user of the program shall download and install Python 3 from https://www.python.org/

    # SUPPORTS REQUIREMENT Storage Requirements 3 & 4
    # This tests that Python 3 was installed on an HDD or SSD drive.
    # The user of the program shall determine the installation location of Python and then check their device's
    # properties the drive that Python is installed on shall either be an SSD or an HDD.

    # SUPPORTS REQUIREMENT Performance 1
    # This tests that the program can execute a typical use case in less than a second.
    def test_calculationSpeed(self):
        time_start = datetime.datetime.now()
        self.test_typicalUseCase()
        time_end = datetime.datetime.now()
        self.assertLessEqual((time_end - time_start).total_seconds(), 1)

    # SUPPORTS REQUIREMENT Performance 2
    # This tests that the user's computer meets the minimum requirements for Python3.
    # The user must make program using at least the minimum requirements to run the program.
    # in PYTHON3, Windows 7 or 10 is required.
    # 2GB or 4GB of RAM is required.

    # SUPPORTS REQUIREMENT System Architecture:
    # This tests that the user's computer has 64-bit architecture.
    # The user should confirm their machine specifications by referencing the system information
    # page in the settings menu.

    # SUPPORTS REQUIREMENT Functional 1
    # This tests that the program accepts input and displays output using the Window's command-line.
    # The user checks that they are interacting with the program through Microsoft's CMD program.

    # SUPPORTS REQUIREMENT Functional 2
    # The program shall allow users to navigate through various options by entering a number
    # which corresponds to a command from a presented list of commands. This will allow
    # the user to choose between different commands intuitively.
    # This tests that the input provided by the user is valid for selecting an option
    # in the start menu of the program.
    def test_startMenu(self):
        self.assertTrue(int(self.rc.startSelection))
        self.assertTrue(self.rc.startSelection in self.rc.startMenuOptions, "The start menu selection was invalid.")

    # SUPPORTS REQUIREMENT Functional 3
    # The user will be able to enter an employee's name into the program.
    # This tests that the input was given and is valid.
    def test_employeeName(self):
        self.assertTrue(str(self.rc.employeeName), "The provided employee name is invalid.")
        self.assertNotEqual(self.rc.employeeName, "", "An employee name was not provided")

    # SUPPORTS REQUIREMENT Functional 4
    # The user will be able to enter the hourly rate at which that employee works in
    # dollars per hour. This tests that the input is a valid number greater than zero.
    def test_hourlyRate(self):
        self.assertTrue(float(self.rc.hourlyRate), "The provided rate is invalid.")
        self.assertTrue(self.rc.hourlyRate > 0, "The pay rate must be greater than zero.")

    # SUPPORTS REQUIREMENT Functional 5
    # The user may select a retirement plan for an employee from a given list. The list shall
    # store three factors: the name of the plan, the percentage of the employee's pay
    # contributed by the company, and the percentage of the employee's pay that they
    # will contribute. This tests that the input for the retirement plan menu is a valid selection.
    def test_retirementPlan(self):
        self.assertTrue(self.rc.planListSelection in self.rc.retirementPlanList,
                        "The retirement plan menu selection was invalid.")

    # SUPPORTS REQUIREMENT Functional 6
    # The user can enter the amount of time worked. This tests that the input is a valid number
    # greater than or equal to zero.
    def test_hoursWorked(self):
        self.assertTrue(float(self.rc.hoursWorked), "A valid number for hours worked was not provided.")
        self.assertTrue(self.rc.hoursWorked >= 0, "The number of hours worked cannot be negative.")

    # SUPPORTS REQUIREMENT Functional 7
    # The user will enter the percentage of the hourly pay the employee puts upon their retirement.
    # This tests that the percentage is a valid number greater than or equal to zero.
    def test_hourlyPercentage(self):
        self.assertTrue(float(self.rc.hourlyPercentage), "The percentage must be entered in numbers.")
        self.assertTrue(self.rc.hourlyPercentage >= 0, "the percentage must NOT be negative.")

    # SUPPORTS REQUIREMENT Functional Requirement 8.a
    # This test ensures that the total monies paid to the employee data point is correctly generated and
    # that it is a valid value.
    def test_paidToEmployee(self):
        self.assertTrue(float(self.rc.paidToEmployee), "paidToEmployee is not a valid number!")
        self.assertTrue((self.rc.paidToEmployee >= 0), "paidToEmployee cannot be negative!")

    # SUPPORTS REQUIREMENT Functional Requirement 8.b
    # This test ensures that the employee contributions data point is correctly generated and that it is a valid value.
    def test_employeeContribution(self):
        self.assertTrue(float(self.rc.employeeContribution), "employeeContribution is not a valid number!")
        self.assertTrue((self.rc.employeeContribution >= 0), "employeeContribution cannot be negative!")

    # SUPPORTS REQUIREMENT Functional Requirement 8.c
    # This test ensures that the company's contributions data point is correctly generated and that it is a valid value.
    def test_companyContributions(self):
        self.assertTrue(float(self.rc.companyContribution), "companyContributions is not a valid number!")
        self.assertTrue(self.rc.companyContribution >= 0, "companyContributions cannot be negative!")

    # SUPPORTS REQUIREMENT Functional Requirement 8.d
    # This test ensures that the total contributions data point is correctly generated and that it is being correctly
    # calculated.
    def test_totalContributions(self):
        self.assertEqual(self.rc.totalContributions, (self.rc.employeeContribution + self.rc.companyContribution),
                         "Total contributions is not equal to sum of employee and company contributions!")

    # SUPPORTS REQUIREMENT Functional Requirement 9
    # Tests that the string to be displayed for a data point correctly contains the value to be displayed.
    def test_display(self):
        self.assertTrue(self.rc.totalContributions.display(1).find(f'{0}', self.rc.paidToEmployee) != -1,
                        'The display output must contain the amount paid to the employee!')
        self.assertTrue(self.rc.totalContributions.display(2).find(f'{0}', self.rc.employeeContribution) != -1,
                        'The display output must contain the amount the employee contributed!')
        self.assertTrue(self.rc.totalContributions.display(3).find(f'{0}', self.rc.companyContribution) != -1,
                        'The display output must contain the amount the company contributed!')
        self.assertTrue(self.rc.totalContributions.display(4).find(f'{0}', self.rc.companyContribution) != -1,
                        'The display output must contain the amount the total contributions!')


if __name__ == '__main__':
    unittest.main()
