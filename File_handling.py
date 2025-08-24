def read_and_write_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            modified_content = content.upper()  # Modify the content (e.g., convert to uppercase)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_and_write_file()
