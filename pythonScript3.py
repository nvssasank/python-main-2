import os
from pythonScript2 import extract_and_process_text

def export_cleaned_data(destination='data_output'):
    if not os.path.exists(destination):
        os.makedirs(destination)

    processed_files, _ = extract_and_process_text()

    for name, content in processed_files.items():
        target_path = os.path.join(destination, name)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.writelines(content)

    print(f"Files written to '{destination}'.")

if __name__ == "__main__":
    export_cleaned_data()
