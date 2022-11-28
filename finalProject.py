    
def main():
    print("Please enter the amount of time worked in minutes.")
    timeInput = input("Amount of time worked in minutes:")
    print("Your amount of time worked is " + timeInput + " minutes.")
    
    print("Please enter the percentage of hourly pay.")
    percentInput = input("percentage of hourly pay:")
    num = percentInput
    percentage = "{:.0%}". format(float(num))
    print("your hourly pay is " + percentage)
    
main()

