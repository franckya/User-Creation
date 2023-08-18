import subprocess

def create_user(username, password):
    # Create the new user with a specified shell and home directory
    subprocess.run(["useradd", "-m", "-s", "/bin/bash", username])

    # Set the password for the new user
    subprocess.run(["echo", f"{username}:{password}", "|", "chpasswd"])

    print(f"User '{username}' was successfully created.")

def main():
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    create_user(new_username, new_password)

    switch_user = input("Do you want to switch to the new user account? (y/n): ")
    if switch_user.lower() == "y":
        subprocess.run(["su", "-", new_username])

if __name__ == "__main__":
    main()
