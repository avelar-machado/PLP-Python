def read_and_modify_file():
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

    try:
        # Step 1: Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 2: Modify content (e.g., uppercase)
        modified_content = content.upper()

        # Step 3: Create new filename
        new_filename = "modified_" + filename

        # Step 4: Write the modified content to new file
        with open(new_filename, "w") as file:
            file.write(modified_content)

        # Step 5: Print success message
        print(f"Success! Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
