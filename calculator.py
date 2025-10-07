def add(firstNumber, secondNumber):
# Returns the sum of firstNumber and secondNumber
    return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
# Returns the subtraction of firsNumber and secondNumber
    return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
# Returns the product of firstNumber and secondNumber
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
# Returns the division of firstNumber and secondNumber
    return firstNumber / secondNumber

def get_valid_choice():
    while True:
        try:
            return int(input("Select an option: "))
        except ValueError:
            print("Option should be a number.")
            continue

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
    
def main():
    print("=" * 45)
    print("                BASIC CALCULATOR")
    print("=" * 45 + "\n")
    operators = {
        1: ("+", add),
        2: ("-", subtract),
        3: ("*", multiply),
        4: ("/", divide),
    }
    while True:
        print("X---Options---X")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = get_valid_choice()  
      
        if choice == 5:  
            print("Exiting...")  
            break  
      
        if choice in operators:  
            firstNumber = get_valid_number("Enter a first number: ")  
          
            secondNumber = get_valid_number("Enter a second number: ")  
            symbol, func = operators[choice]
            
            try:
                result = func(firstNumber, secondNumber)
                print(f"{firstNumber} {symbol} {secondNumber} = {result}")
                
            except ZeroDivisionError:
                print("Math Error: cannot be divided by zero.")
        else:  
            print("Invalid Option.")

if __name__ == "__main__":
    main()
