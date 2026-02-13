from zxcvbn import zxcvbn
from colorama import Fore, Style, init

init(autoreset=True) 

def analyse_password(password: str) -> dict:
    return zxcvbn(password)

def print_analysis(analysis: dict) -> None:
    strength_colors = {
        0: Fore.RED,       
        1: Fore.LIGHTRED_EX,
        2: Fore.YELLOW,    
        3: Fore.GREEN,      
        4: Fore.CYAN       
    }

    strength_labels = {0: 'Very Weak', 1: 'Weak', 2: 'Fair', 3: 'Strong', 4: 'Very Strong'}
    score = analysis['score']
    strength = strength_labels.get(score, 'Unknown')
    color = strength_colors.get(score, Fore.WHITE)

    print(f'\nPassword: {Fore.MAGENTA}{analysis['password']}')
    print(f'Human Strength: {color}{strength} ({score}/4))')
    print(f'Guesses: {Fore.BLUE}{analysis['guesses']}')
    print(f'Fast Offline Crack Time: {Fore.YELLOW}{analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']}')
    print(f'Offline Crack Time: {Fore.YELLOW}{analysis['crack_times_display']['offline_slow_hashing_1e4_per_second']}')
    print(f'Online Crack Time: {Fore.YELLOW}{analysis['crack_times_display']['online_no_throttling_10_per_second']}')
    print(f'Throttled Online Crack Time: {Fore.YELLOW}{analysis['crack_times_display']['online_throttling_100_per_hour']}')

    warning = analysis['feedback'].get('warning', '')
    suggestions = analysis['feedback'].get('suggestions', [])

    if warning:
        print(f'{Fore.RED}Warning: {warning}')

    if suggestions:
        print(f'{Fore.CYAN}Suggestions:')
        for s in suggestions:
            print(f' - {s}')
