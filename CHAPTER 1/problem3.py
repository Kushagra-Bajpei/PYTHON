# write a python program to print the contents of a directory using the os module, search online for the function which does that

# import os

# def print_directory_contents(path):
#     try:
#         entries = os.listdir(path)  # returns a list of names in the directory
#         print(f"Contents of directory '{path}':")
#         for entry in entries:
#             print(entry)
#     except FileNotFoundError:
#         print(f"Error: The directory '{path}' does not exist.")
#     except PermissionError:
#         print(f"Error: Permission denied to access '{path}'.")
#     except Exception as e:
#         print("An error occurred:", e)

# if __name__ == "__main__":
#     # You can change this to any directory you want
#     directory_path = "/"  # current working directory
#     print_directory_contents(directory_path)





# import os

# print(os.listdir("/"))   # "." means current folder







# import os

# for item in os.listdir("."):
#     print(item)

