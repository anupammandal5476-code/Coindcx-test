import random
from datetime import datetime
import os
import json

def main():
    filename = "random_numbers_list.txt"
    
    # Generate random two-digit number (10-99)
    random_number = random.randint(10, 99)
    
    # Get current date and time
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare the entry as a dictionary
    entry = {
        "number": random_number,
        "timestamp": timestamp
    }
    
    # Check if file exists
    if os.path.exists(filename):
        # Read existing data
        with open(filename, 'r') as file:
            content = file.read().strip()
        
        if content:
            # Remove the closing bracket and add new entry
            if content.endswith(']'):
                content = content[:-1]
            new_content = content + ',\n    ' + json.dumps(entry) + '\n]'
        else:
            new_content = '[\n    ' + json.dumps(entry) + '\n]'
    else:
        # Create new file with first entry
        new_content = '[\n    ' + json.dumps(entry) + '\n]'
        print(f"File '{filename}' created")
    
    # Write the updated content back to file
    with open(filename, 'w') as file:
        file.write(new_content)
    
    print(f"Entry added: {random_number} at {timestamp}")

if __name__ == "__main__":
    main()
