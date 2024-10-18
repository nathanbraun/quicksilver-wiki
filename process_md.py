import os
import re

# Directories for raw and clean markdown files
raw_directory = './raw'
clean_directory = './clean'

# Ensure the output directory exists
os.makedirs(clean_directory, exist_ok=True)

def process_markdown(file_content):
    # Split content by lines for processing
    lines = file_content.split('\n')

    # Find start position after the front-matter
    start_index = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start_index:
                # We've found the end of the header
                start_index = i + 1
                break
            else:
                # We assume front matter starts at first occurrence
                start_index = i

    # Remove header by slicing lines after the second '---'
    lines = lines[start_index:]

    processed_lines = []

    internal_link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

    # Process each line
    for line in lines:
        # Modify internal links by appending a slash
        modified_line = internal_link_pattern.sub(
            lambda match: f"[{match.group(1)}]({match.group(2).strip('/')}/)",
            line
        )
        processed_lines.append(modified_line)

    # Join lines together, ignoring trailing empty lines
    while processed_lines and not processed_lines[-1].strip():
        processed_lines.pop()
    
    return '\n'.join(processed_lines) + '\n'  # Ensure EOF newline

def main():
    for filename in os.listdir(raw_directory):
        if filename.endswith('.md'):
            with open(os.path.join(raw_directory, filename), 'r', encoding='utf-8') as file:
                file_content = file.read()

            # Process the markdown content
            processed_content = process_markdown(file_content)

            # Write the processed content to the clean output directory
            with open(os.path.join(clean_directory, filename), 'w', encoding='utf-8') as file:
                file.write(processed_content)

if __name__ == '__main__':
    main()
