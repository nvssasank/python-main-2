import os
from pythonScript2 import extract_and_process_text

def create_summary_file(output_folder='data_output'):
    _, stats = extract_and_process_text()

    summary_file_path = os.path.join(output_folder, 'summary.txt')
    with open(summary_file_path, 'w', encoding='utf-8') as summary:
        summary.write("File Processing Summary\n")
        summary.write("Filename\tLines\tWords\n")
        for name, (lines, words) in stats.items():
            summary.write(f"{name}\t{lines}\t{words}\n")

    print("Summary has been created in the output folder.")

if __name__ == "__main__":
    create_summary_file()
