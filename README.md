# repo_to_md

## Overview

`repo_to_md` is a simple Python script that processes the files in a specified folder and generates a Markdown summary of the code files it finds. The generated Markdown file contains the names of the code files along with their contents in code blocks.

## Features

- Processes only the root folder (no subfolders).
- Supports a wide range of file extensions across multiple programming languages.
- Automatically includes the folder name in the header of the generated Markdown file.
- Ensures that existing markdown files are not overwritten by appending a timestamp to the output file if a file with the name `code_summary.md` already exists.
- Excludes previously generated `code_summary.md` files from being included in subsequent runs.

## Supported File Types

The script currently supports the following file types:

- Python (`.py`)
- JavaScript (`.js`)
- Java (`.java`)
- C/C++ (`.c`, `.cpp`, `.cc`, `.h`)
- Ruby (`.rb`)
- Go (`.go`)
- PHP (`.php`)
- TypeScript (`.ts`)
- HTML/CSS/SCSS (`.html`, `.css`, `.scss`)
- XML (`.xml`)
- Kotlin (`.kt`)
- Swift (`.swift`)
- Shell/Batch (`.sh`, `.bat`)
- PowerShell (`.ps1`)
- Perl (`.pl`, `.pm`)
- ASP/JSP (`.asp`, `.jsp`)
- SQL (`.sql`)
- Lua (`.lua`)
- Dart (`.dart`)
- Erlang (`.erl`)
- Elixir (`.ex`)
- React JSX/TSX (`.jsx`, `.tsx`)
- Scala (`.scala`)
- Rust (`.rs`)
- Visual Basic (`.vb`)
- Fortran (`.f90`, `.for`)
- Assembly (`.s`)
- Config files (`.ini`, `.toml`, `.yaml`, `.yml`, `.json`)
- Documentation (`.md`, `.rst`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repo_to_md.git
   cd repo_to_md
   ```
2. Ensure you have Python 3.x installed.

## Usage

1. Navigate to the folder where the script is located.

2. Run the script:

   ```bash
   python app.py
   ```

3. Enter the folder path you want to process when prompted. The script will create a Markdown file summarizing all the code files in the root directory.

## Example

For a folder named `my_project`, running the script will generate a file named `code_summary.md` (or `code_summary_YYYYMMDD_HHMMSS.md` if a file already exists). The first line of the markdown file will look like this:

```
# Code Files in Folder my_project
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
