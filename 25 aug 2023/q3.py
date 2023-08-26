try:
    file_path = input("Enter the path to the file: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The specified file was not found.")
except UnicodeDecodeError as e:
    print(f"Error: Unicode decode issue - {e}")





