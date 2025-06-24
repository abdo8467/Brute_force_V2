import itertools
import string

def brute_force(target, charset=string.ascii_lowercase + string.digits, max_length=6):
    """
    Attempts to brute-force the target string using the given charset and max_length.
    Returns the found string or None if not found.
    """
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            guess = ''.join(attempt)
            if guess == target:
                print(f"Found: {guess}")
                return guess
    print("Target not found.")
    return None

if __name__ == "__main__":
    # Example usage
    target_password = "abc12"
    brute_force(target_password, charset=string.ascii_lowercase + string.digits, max_length=5)