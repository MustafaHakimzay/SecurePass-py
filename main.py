from src.password_strength import analyse_password, print_analysis
from src.password_generator import generate_password

def show_menu():
    print('\n=== Password Manager ===')
    print('1 - Generate a secure password')
    print('2 - Analyse password strength')
    print('3 - Exit')

    user_choice = input('Enter your choice: ')

    if not user_choice.isdigit():
        print('Please enter a valid option.')
        return True
    
    user_choice = int(user_choice)

    if user_choice == 1:
        length = input('Enter the length for the password, or 0 to use default length (16): ')
        if not length.isdigit():
            print('That is not a valid integer. Using default length value')
            password = generate_password()
        else:
            length = int(length)
            if length == 0:
                password = generate_password()
            if length < 8:
                print('Passwords shorter than 8 characters are very insecure. Using default length (16)')
                password = generate_password()
            else:
                password = generate_password(length)
        print(f'\nGenerated password: {password}')

    elif user_choice == 2:
        password = input(f'Enter password to analsye: ')
        analysis = analyse_password(password)
        print_analysis(analysis)  

    elif user_choice == 3:
        print('Exited')
        return False
    
    else:
        print('Not a valid option. Please enter only 1, 2 or 3.')  

    return True

if __name__ == '__main__':
    while show_menu():
        pass