"""
camply __main__.py CLI Wrapper
"""

import sys

from camply.cli import cli

def process_input(user_input):
    # Your existing application logic here
    # Process the user_input and return the result
    return f"Processed: {user_input}"

def main(user_input=None):
    if user_input is None:
        # This part will only run when executed from command line
        if len(sys.argv) > 1:
            user_input = sys.argv[1]
        else:
            return "No input provided. Please provide input as a command-line argument or through the web interface."
    
    return process_input(user_input)

if __name__ == "__main__":
    result = main()
    print(result)