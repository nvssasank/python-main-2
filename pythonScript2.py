import os

def extract_and_process_text(source_folder='data_input'):
    results = {}
    file_metrics = {}

    for file in os.listdir(source_folder):
        if file.endswith('.txt'):
            filepath = os.path.join(source_folder, file)
            cleaned_content = []
            lines_count = 0
            words_count = 0

            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('#'):
                        continue
                    lines_count += 1
                    words_count += len(line.split())
                    updated_line = line.replace("temp", "permanent")
                    cleaned_content.append(updated_line)

            results[file] = cleaned_content
            file_metrics[file] = (lines_count, words_count)

    return results, file_metrics

if __name__ == "__main__":
    content, metrics = extract_and_process_text()
    print(f"{len(content)} file(s) successfully processed.")
