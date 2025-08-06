import os

def setup_input_directory():
    directory_name = 'data_input'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' has been created.")
        print("Please insert your .txt files into this folder before proceeding.")
        return False
    return True

if __name__ == "__main__":
    if setup_input_directory():
        print("Input directory is ready. Continue with the next step.")
