# File Handling Assignment

# File Creation and Writing
try:
    # Create a new file and open it in write mode
    with open("my_file.txt", "w") as file:
        # Write three lines of text, including strings and numbers
        file.write("Hello, this is line 1.\n")
        file.write("Here is line 2 with a number: 1234.\n")
        file.write("Final line, line 3.\n")
    print("File created and text written successfully.")

except PermissionError:
    print("Permission denied: Unable to write to file.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# File Reading and Displaying Contents
try:
    # Open the file in read mode and display contents
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)

except FileNotFoundError:
    print("File not found: Please make sure 'my_file.txt' exists.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode and add more lines
    with open("my_file.txt", "a") as file:
        file.write("Appending this new line 4.\n")
        file.write("Another appended line, line 5, with a number: 5678.\n")
        file.write("Final appended line, line 6.\n")
    print("\nText successfully appended to the file.")

except PermissionError:
    print("Permission denied: Unable to append to file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final Confirmation - Display Updated File Contents
try:
    # Read and display the updated content
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\n--- Updated File Contents ---")
        print(updated_content)

except FileNotFoundError:
    print("File not found: Please make sure 'my_file.txt' exists.")
except Exception as e:
    print(f"An error occurred while reading the updated file: {e}")

    