
# CodebaseConjunction
> Consolidate your entire codebase into a single text file for seamless integration with advanced AI models.

**CodebaseConjunction** is a Python tool designed to merge all files within a codebase into a single text file. This approach facilitates the processing of complex projects by advanced language models and AI systems that may struggle with multiple files or lack the capability to handle them individually.

## Installing / Getting Started

### Prerequisites

Ensure you have the following installed on your system:

1. **Python** (version 3.6 or higher)

### Steps to Set Up

To get CodebaseConjunction up and running locally:

```bash
# Clone the repository
git clone https://github.com/hillmatt7/CodebaseConjunction.git
cd CodebaseConjunction

# Install required dependencies
pip install -r requirements.txt

# Run the script
python codebase_conjunction.py /path/to/your/codebase /path/to/output/file.txt
```

Replace `/path/to/your/codebase` with the path to the directory containing your codebase, and `/path/to/output/file.txt` with the desired path for the consolidated output file.

## Features

- **Comprehensive Merging**: Recursively traverses directories to include all files in the codebase.
- **Customizable File Inclusion**: Allows specification of file extensions to include or exclude certain file types.
- **Preservation of File Structure**: Inserts headers indicating the original file paths to maintain context within the merged file.

## Usage

The primary script, `codebase_conjunction.py`, accepts the following command-line arguments:

- `input_directory`: The root directory of the codebase to be merged.
- `output_file`: The path to the output file where the merged content will be saved.
- `--include-extensions`: (Optional) A comma-separated list of file extensions to include (e.g., `.py,.txt`).
- `--exclude-extensions`: (Optional) A comma-separated list of file extensions to exclude.

Example usage:

```bash
python codebase_conjunction.py /path/to/codebase /path/to/output.txt --include-extensions .py,.md
```

This command will merge all `.py` and `.md` files from the specified codebase into a single text file.

## File Structure

- **`codebase_conjunction.py`**: The main script responsible for merging the codebase files.
- **`README.md`**: Documentation for the project.
- **`LICENSE`**: License information for the project.

## Known Issues

- **Large Codebases**: Merging very large codebases may result in significant memory usage.
- **Binary Files**: The script is designed for text-based files; including binary files may lead to unexpected behavior.

## Links

- **Project Homepage**: [CodebaseConjunction](https://github.com/hillmatt7/CodebaseConjunction)
- **Issue Tracker**: [CodebaseConjunction Issues](https://github.com/hillmatt7/CodebaseConjunction/issues)
- **Repository**: [CodebaseConjunction Repository](https://github.com/hillmatt7/CodebaseConjunction)

## Licensing

The code in this project is licensed under the MIT License. See the [LICENSE](https://github.com/hillmatt7/CodebaseConjunction/blob/main/LICENSE) file for details.

