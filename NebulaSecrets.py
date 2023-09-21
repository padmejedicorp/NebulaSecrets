import random
import string

class NebulaSecrets:
    def __init__(self):
        self.secrets = []

    def generate_secret(self, length=16):
        secret = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        self.secrets.append(secret)
        return secret

    def get_secrets(self):
        return self.secrets

if __name__ == "__main__":
    nebula_secrets = NebulaSecrets()

    print("Welcome to NebulaSecrets!")
    while True:
        print("\n1. Generate a new secret")
        print("2. View secrets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            secret = nebula_secrets.generate_secret()
            print(f"Generated Secret: {secret}")
        elif choice == '2':
            secrets = nebula_secrets.get_secrets()
            if secrets:
                print("Stored Secrets:")
                for idx, secret in enumerate(secrets, 1):
                    print(f"{idx}. {secret}")
            else:
                print("No secrets generated yet.")
        elif choice == '3':
            print("Exiting NebulaSecrets. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
