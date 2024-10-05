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

def main(user_input):
    return process_input(user_input)

if __name__ == "__main__":
    print("This script is not meant to be run directly in a web environment.")
    print("Please use the Flask app to interact with the application.")