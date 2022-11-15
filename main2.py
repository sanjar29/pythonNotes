def calculate_income(rate, annualOrQuarterly):
    if annualOrQuarterly == 1:
        return rate
    return rate*4

def nameFormatter(firstName, lastName):
    return f'{lastName},{firstName}\n'

def employee_info(firstName, lastName, department, email, rate, annulaOrQuarterly):
    return f'Full Name: {nameFormatter(firstName, lastName)}'\
            f'Wage: ${calculate_income(rate, annulaOrQuarterly)}\n'\
            f'Department: {department}\nEmail Address: {email}\n'

def isEvenOrOdd(number):
    if number % 2 == 0:
        return "even"
    return "odd"

def isPrime(number):
    if number <2:
        return "NO"
    notPrime = False
    halfOftheNumber = int(number/2)
    for i in range(2, halfOftheNumber):
        if int(number%i) == 0:
            return "NO"
        else: continue
    return "YES"
def menu():
    return int(input("1) Program to get user info:\n2)Program to check if a number is prime\n3) Program to check if a number is even or odd\nEnter your choice: "))
def __init__():
    print("\n********LET'S GET STARTED*******\n")
    userChoice = menu()
    if userChoice == 1:
        employeeFirstName = input("Enter employee's first name: ")
        employeeLastName = input("Enter employee's last name: ")
        department = input("Enter employee's department: ")
        while (True):
            employeeEmail = input("Enter employee's email address: ")
            if employeeEmail.find('@') == -1 and employeeEmail.find('.')== -1:
                print("INVALID EMAIL ADDRESS, MUST INCLUDE @ character or a DOT")
                continue
            else: break
        while (True):
            employeeWage = float(input("Enter employee's wage: "))
            if employeeWage < 0:
                print("Wage can't be less than 0")
                continue
            else: break
        while (True):
          isQuarterlyOfAnnually = int(input("Is the wage given annually or quarterly (1-Annually: 4-Quarterly): "))
          if isQuarterlyOfAnnually == 1 or isQuarterlyOfAnnually == 4:
              break
          else:
              print("You have not input either 1 (A) or 4 (Q).")
              continue
        print("\n\nBased on the Information Given\n\n"+employee_info(employeeFirstName,employeeLastName, department, employeeEmail,employeeWage,isQuarterlyOfAnnually))
    elif userChoice == 2:
        number = int(input("Enter a number: "))
        print(f"The {number} is {isPrime(number)} prime")
    elif userChoice == 3:
        number = int(input("Enter a number: "))
        print(f"This number, {number} is {isEvenOrOdd(number)}")


while (True):
    __init__()
    again = input("Would you like to see it again (Y or N): ")
    if again[0].lower() == 'y':
        continue
    else:
        print("See you around :)")
        break