import os

# Folder containing input text files
folder_path = '../data/FTDs'

# Output file where combined content will be saved
output_file = '../data/FTD.txt'

# Function to combine files
def combine_files_in_folder(folder_path, output_file, encoding='utf-8'):
    with open(output_file, 'w', encoding=encoding, errors='ignore') as outfile:
        # List all text files in the folder
        files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
        
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, 'r', encoding=encoding, errors='ignore') as infile:
                    # Read content of current input file
                    content = infile.read()
                    # Write content to output file
                    outfile.write(content)
                    # Add a newline separator between files
                    outfile.write('\n')
            except UnicodeDecodeError:
                print(f"Unable to decode file '{file_name}' with encoding '{encoding}'. Skipping...")

# Call function to combine files
combine_files_in_folder(folder_path, output_file)

print(f"Files from '{folder_path}' combined and saved to '{output_file}'.")
