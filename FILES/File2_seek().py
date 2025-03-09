# using seek()

# Open the file in read mode
with open("test.txt", "r") as file:
    file.seek(10)  # Move to the 10th index (starting from 0)
    data = file.read()  # Read from index 10 onwards
    print("File content from index 10 onwards:")
    print(data)

