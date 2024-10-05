"""
camply __main__.py CLI Wrapper
"""

from camply.cli import cli

if __name__ == "__main__":
    cli()

def process_input(user_input):
    # Your existing application logic here
    # Process the user_input and return the result
    return f"Processed: {user_input}"

# Keep your main() function for command-line usage
def main():
    while True:
        user_input = input("Enter your input: ")
        if user_input.lower() == 'quit':
            break
        print(process_input(user_input))

if __name__ == "__main__":
    main()