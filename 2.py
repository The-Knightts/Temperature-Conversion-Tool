'''
    Temperature Conversion Tool
    Task: Write a program to convert temperatures between Celsius and Fahrenheit. Users should be able to input a temperature and choose the conversion type.
    Steps:
    - Use functions to convert Celsius to Fahrenheit and vice versa.
    - Use a while loop to continuously prompt the user for actions (input temperature, choose conversion, display result, exit).
    - Use arithmetic operators for the conversion calculations.
    - Use conditional statements to handle different user inputs and errors.

    Example interaction:
    1. Input temperature (100)
    2. Choose conversion (Celsius to Fahrenheit)
    3. Display result
    4. Exit
    Expected output: Converted temperature
'''

def cel_to_far(Celsius):
    return (9/5 * Celsius) + 32

def far_to_cel(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

print("\nTemperature Conversion Tool")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Exit")

choice = 0
while choice != 3:
    choice = int(input('Enter the choice between 1 - 3 : '))

    if choice in [1, 2]:
        temp = float(input('Enter the Temperature : '))
        if choice == 1:
            print(f'{temp}C is {(cel_to_far(temp))} F')
        elif choice == 2:
            print(f'{temp}F is {(far_to_cel(temp))} C')
    elif choice == 3:
        print('Exit.')
    else:
        print('Invalid input. Please enter a number between 1 and 3')