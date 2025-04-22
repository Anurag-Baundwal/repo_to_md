import os
from datetime import datetime

def process_folder(folder_path):
    if not os.path.isdir(folder_path):
        return 'Invalid directory. Please enter a valid folder path.'

    folder_name = os.path.basename(folder_path)
    md_content = f'# Code Files in Folder {folder_name}\n\n'

    # List of file extensions to include
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

    # List of specific filenames to always include (case-sensitive)
    # Using a set for efficient lookup
    specific_filenames_to_include = {
        'BUILD',
        '.bazelrc',
        '.gitignore',
        'makefile', # Note: case-sensitive, use 'Makefile' if needed
        'WORKSPACE',
        'gpp_build.sh'
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Check if it's a file first
        if os.path.isfile(file_path):
            # Check if it's the output file we're generating
            is_output_file = file.startswith('code_summary') and file.endswith('.md')
            
            # Check if the file should be included
            # It should be included if:
            # 1. Its extension is in valid_extensions OR
            # 2. Its name is in specific_filenames_to_include
            # AND it's NOT the output file itself
            should_include = (
                file.endswith(valid_extensions) or file in specific_filenames_to_include
            )

            if should_include and not is_output_file:
                md_content += f'## {file}\n\n'
                try:
                    with open(file_path, 'r', encoding='utf-8') as code_file:
                        code = code_file.read()
                    # Add file type hint for syntax highlighting in Markdown
                    # Extract extension or use filename if no extension
                    _, ext = os.path.splitext(file)
                    lang_hint = ext[1:] if ext else file.lower() # Use lowercase filename if no ext
                    # Handle specific cases like '.gitignore' or 'makefile'
                    if file == '.gitignore': lang_hint = 'gitignore'
                    elif file.lower() == 'makefile': lang_hint = 'makefile'
                    elif file == '.bazelrc': lang_hint = 'bazelrc' # Or 'ini' or ''
                    elif file == 'BUILD' or file == 'WORKSPACE': lang_hint = 'bazel' # Starlark/Bazel
                    
                    md_content += f'\n```{lang_hint}\n{code}\n```\n\n'
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