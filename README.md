# pdfMerge

A simple python script to treat pdf files

## Functionalities
- Join pdf files
- Convert jpg, png and jpeg to pdf
- Join pdf and image files into a single pdf
- Add a custom name to the merged file

## Usage
```
pdfmerge file1.pdf/jpg <file2.pdf/jpg> ... <-o output.pdf>
```

## Installation
1. Clone the repository
2. Run `install.sh`
3. Add the alias in your `.zshrc` file
```
alias pdfmerge="<path_to_project>/venv/bin/python && <path_to_project>/main.py"
```