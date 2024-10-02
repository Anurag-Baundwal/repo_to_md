import os
from datetime import datetime

def process_folder(folder_path):
    if not os.path.isdir(folder_path):  # Check if the provided path is a valid directory
        return 'Invalid directory. Please enter a valid folder path.'

    folder_name = os.path.basename(folder_path)  # Get the folder name from the path
    md_content = f'# Code Files in Folder {folder_name}\n\n'  # Include the folder name in the header

    # Define a list of file extensions for various programming languages
    valid_extensions = (
        '.py', '.js', '.java', '.c', '.cpp', '.cc', '.h',  # Python, JavaScript, Java, C/C++
        '.rb', '.go', '.php', '.cs', '.ts',                # Ruby, Go, PHP, C#, TypeScript
        '.html', '.css', '.scss', '.xml',                  # HTML, CSS, SCSS, XML
        '.kt', '.swift', '.m', '.mm',                      # Kotlin, Swift, Objective-C
        '.sh', '.bat', '.ps1', '.r',                       # Shell, Batch, PowerShell, R
        '.pl', '.pm', '.asp', '.jsp', '.sql',              # Perl, ASP, JSP, SQL
        '.lua', '.dart', '.erl', '.ex', '.jsx', '.tsx',    # Lua, Dart, Erlang, Elixir, React JSX/TSX
        '.scala', '.rs', '.vb', '.f90', '.for', '.s',      # Scala, Rust, Visual Basic, Fortran, Assembly
        '.ini', '.toml', '.yaml', '.yml', '.json',         # Config files (INI, TOML, YAML, JSON)
        '.md', '.rst'                                      # Markdown, reStructuredText
    )

    # Only process files in the root directory
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.endswith(valid_extensions):  # Only process specified code file types
            md_content += f'## {file}\n\n'  # Add file title to markdown
            try:
                with open(file_path, 'r', encoding='utf-8') as code_file:  # Ensure encoding compatibility
                    code = code_file.read()  # Read the content
                md_content += f'\n```\n{code}\n```\n\n'  # Add code block to markdown
            except Exception as e:
                md_content += f'\n**Error reading file {file}: {str(e)}**\n\n'

    # Generate a filename with a timestamp if 'code_summary.md' already exists
    output_filename = 'code_summary.md'
    output_path = os.path.join(folder_path, output_filename)

    if os.path.exists(output_path):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Get current timestamp
        output_filename = f'code_summary_{timestamp}.md'
        output_path = os.path.join(folder_path, output_filename)

    try:
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(md_content)  # Save the markdown file
        return f'Markdown file created at: {output_path}'
    except Exception as e:
        return f'Error writing markdown file: {str(e)}'

if __name__ == "__main__":
    # Automatically handle Windows paths
    folder_path = input("Enter the path of the folder to process: ").strip()
    result = process_folder(folder_path)  # Process the folder
    print(result)  # Print the result message
