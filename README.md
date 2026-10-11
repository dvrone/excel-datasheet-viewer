# Excel DataSheet Viewer

A lightweight desktop application built with Python and Tkinter for opening and viewing Excel spreadsheets in a tabular interface.

## Features

- Open and read `.xlsx` Excel files
- Display spreadsheet data in a table
- Automatically generate column headings
- Scroll vertically and horizontally through data
- Handle file-opening errors with dialog messages
- Simple graphical user interface

## Technologies

- **Python** — core programming language
- **Tkinter** — graphical user interface
- **Pandas** — spreadsheet data processing
- **OpenPyXL** — Excel file support

## Project Structure

```
excel-datasheet-viewer/
├── excel-file.ico
├── excel-file.png
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── test.xlsx
```

## Installation

Clone the repository:

```
git clone https://github.com/dvrone/excel-datasheet-viewer.git
cd excel-datasheet-viewer
```

Create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the application:

```
python main.py
```

Click **Open Excel File**, select an `.xlsx` file, and view its contents in the table.

## License

This project is distributed under the license included in the repository.

## Icon Attribution

Excel file icon by [yoorie on Flaticon](https://www.flaticon.com/free-icons/excel-files).