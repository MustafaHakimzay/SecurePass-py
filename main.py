from src.password_strength import analyse_password, print_analysis
from src.password_generator import generate_password

def option():
    try:
        user_choice = int(input('Enter 1 to generate a secure password, or 2 to analyse your password strength: '))
        if user_choice == 1:
            print(generate_password())
        elif user_choice == 2:
            password = input('\nEnter password: ')
            analysis = analyse_password(password)
            print_analysis(analysis)     
        else:
            print('Not a valid option.')
    except ValueError:
        print('Please only enter 1 or 2.')

if __name__ == '__main__':
    while True:
        option()