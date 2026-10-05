import hashlib
import time

# Stores login activity while the program is running
login_logs = []

# User accounts
# Passwords are stored as hashes instead of plain text
users = {
    "admin": hashlib.sha256("Cyber123!".encode()).hexdigest(),
    "marwan": hashlib.sha256("Python456!".encode()).hexdigest()
}

MAX_ATTEMPTS = 3
LOCKOUT_TIME = 10


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(username, password):

    # Check if username exists
    if username not in users:
        return False

    # Hash the password the user entered
    entered_password = hash_password(password)

    # Compare the hashes
    if entered_password == users[username]:
        return True
    else:
        return False


def log_attempt(username, successful):

    if successful:
        login_logs.append(
            f"SUCCESSFUL LOGIN - User: {username}"
        )
    else:
        login_logs.append(
            f"FAILED LOGIN - User: {username}"
        )


def show_logs():

    print("\n----------------------------")
    print("SECURITY LOGIN LOG")
    print("----------------------------")

    if len(login_logs) == 0:
        print("No login attempts recorded.")
    else:
        for log in login_logs:
            print(log)


def login():

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        print("\nLOGIN")
        print("----------------------------")

        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):

            print("\nAccess Granted")
            print(f"Welcome, {username}!")

            log_attempt(username, True)

            return

        else:

            attempts += 1

            log_attempt(username, False)

            remaining = MAX_ATTEMPTS - attempts

            print("\nAccess Denied")

            if remaining > 0:
                print(f"Attempts remaining: {remaining}")

    # User failed 3 times
    print("\nSECURITY ALERT")
    print("Too many failed login attempts.")
    print(f"System locked for {LOCKOUT_TIME} seconds.")

    for seconds in range(LOCKOUT_TIME, 0, -1):
        print(f"Unlocking in {seconds} seconds...")
        time.sleep(1)

    print("\nLockout expired.")
    print("You may try again.")

    # Allow another login attempt after lockout
    login()


def main():

    while True:

        print("\n============================")
        print("SECURE AUTHENTICATION SYSTEM")
        print("============================")

        print("1. Login")
        print("2. View Security Logs")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            login()

        elif choice == "2":
            show_logs()

        elif choice == "3":
            print("\nProgram closed.")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


main()
