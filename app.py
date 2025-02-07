import os
from datetime import datetime

def process_folder(folder_path):
    if not os.path.isdir(folder_path):
        return 'Invalid directory. Please enter a valid folder path.'

    folder_name = os.path.basename(folder_path)
    md_content = f'# Code Files in Folder {folder_name}\n\n'

    valid_extensions = (
        '.py', '.js', '.java', '.c', '.cpp', '.cc', '.h',
        '.rb', '.go', '.php', '.cs', '.ts',
        '.html', '.css', '.scss', '.xml',
        '.kt', '.swift', '.m', '.mm',
        '.sh', '.bat', '.ps1', '.r',
        '.pl', '.pm', '.asp', '.jsp', '.sql',
        '.lua', '.dart', '.erl', '.ex', '.jsx', '.tsx',
        '.scala', '.rs', '.vb', '.f90', '.for', '.s',
        '.ini', '.toml', '.yaml', '.yml', '.json',
        '.md', '.rst'
    )

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        # Skip files starting with 'code_summary' and ending with '.md'
        if (os.path.isfile(file_path) and 
            file.endswith(valid_extensions) and 
            not (file.startswith('code_summary') and file.endswith('.md'))):
            md_content += f'## {file}\n\n'
            try:
                with open(file_path, 'r', encoding='utf-8') as code_file:
                    code = code_file.read()
                md_content += f'\n```\n{code}\n```\n\n'
            except Exception as e:
                md_content += f'\n**Error reading file {file}: {str(e)}**\n\n'

    output_filename = 'code_summary.md'
    output_path = os.path.join(folder_path, output_filename)

    if os.path.exists(output_path):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f'code_summary_{timestamp}.md'
        output_path = os.path.join(folder_path, output_filename)

    try:
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(md_content)
        return f'Markdown file created at: {output_path}'
    except Exception as e:
        return f'Error writing markdown file: {str(e)}'

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to process: ").strip().strip('"')
    result = process_folder(folder_path)
    print(result)