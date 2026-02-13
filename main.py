from src.password_strength import analyse_password, print_analysis

if __name__ == '__main__':
    while True:
        password = input('Enter password: ')
        analysis = analyse_password(password)
        print_analysis(analysis)