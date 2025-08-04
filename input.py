def process_file():
    try:
        # Step 1: Read contents of input.txt
        with open("input.txt", "r") as file:
            content = file.read()
        
        # Step 2: Count words
        word_count = len(content.split())
        
        # Step 3: Convert to uppercase
        content_upper = content.upper()
        
        # Step 4: Write to output.txt
        with open("output.txt", "w") as file:
            file.write("PROCESSED TEXT:\n")
            file.write(content_upper)
            file.write("\n\nWORD COUNT: " + str(word_count))
        
        # Step 5: Success message
        print("File 'output.txt' created successfully with processed content.")
    
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Call the function
process_file()
