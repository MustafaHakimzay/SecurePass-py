from zxcvbn import zxcvbn

def analyse_password(password: str) -> dict:
    return zxcvbn(password)

def print_analysis(analysis: dict) -> None:
    strength_labels = {0: 'Very Weak', 1: 'Weak', 2: 'Fair', 3: 'Strong', 4: 'Very Strong'}
    strength = strength_labels.get(analysis['score'], 'Unknown')

    output = f"""
Password: {analysis['password']}
Human Strength: {strength} ({analysis['score']}/4)
Guesses: {analysis['guesses']}
Fast Offline Crack Time: {analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']}
Offline Crack Time: {analysis['crack_times_display']['offline_slow_hashing_1e4_per_second']}
Online Crack Time: {analysis['crack_times_display']['online_no_throttling_10_per_second']}
Throttled Online Crack Time: {analysis['crack_times_display']['online_throttling_100_per_hour']}
"""

    warning = analysis['feedback'].get('warning', '')
    suggestions = analysis['feedback'].get('suggestions', [])

    if warning:
        output += f"Warning: {warning}\n"

    if suggestions:
        output += "Suggestions:\n"
        for s in suggestions:
            output += f" - {s}\n"

    print(output)
