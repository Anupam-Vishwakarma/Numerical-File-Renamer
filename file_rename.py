import os

# Define the directory where you want to create the files
directory = 'C:/Users/Anupam/OneDrive/Documents/pyfolder'

# Define the file extension
file_extension = '.txt'

# Get a list of files in the directory with the specified file extension
file_names = [f for f in os.listdir(directory) if f.endswith(file_extension)]

# Rename the files with a numerical sequence
for i, file_name in enumerate(file_names, 1):
    new_file_name = f"{i}{file_extension}"
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(os.path.join(directory, file_name), new_file_path)

# Print the names of the renamed files
print(f"Renamed {len(file_names)} files with numerical sequence:")
for i in range(1, len(file_names) + 1):
    file_name = f"{i}{file_extension}"
    print(file_name)