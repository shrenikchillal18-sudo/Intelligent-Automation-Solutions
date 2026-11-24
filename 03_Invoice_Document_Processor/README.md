# Invoice Document Processor

## About the Project

This project is a Python-based invoice processing script that reads invoice PDFs and extracts important details such as the invoice number, supplier name, and invoice amount.

The idea was to build a small application that reads invoice PDFs, extracts some important information and decides how each invoice should be handled based on predefined business rules.

I used Python for the processing logic and pytest to test the different scenarios.

## What It Does

* Reads PDF invoices from the `invoices` folder.
* Extracts invoice text using `pypdf`.
* Uses regular expressions and string processing to extract invoice details.
* Checks whether the invoice number, supplier name, and amount are valid.
* Identifies duplicate invoices using the invoice number.
* Assigns a processing action based on the invoice amount.
* Sends invalid and duplicate invoices to manual review.
* Displays the processing results in the terminal.

## Processing Rules

| Condition                        | Action                 |
| -------------------------------- | ---------------------- |
| Missing or invalid required data | Manual Review Required |
| Duplicate invoice                | Manual Review Required |
| Amount up to €1,000, if valid    | Auto Process           |
| Amount above €1,000 up to €5,000 | Approval Required      |
| Amount above €5,000              | Management Review      |

These are sample business rules for this project and can be adjusted depending on the requirements of a real invoice processing workflow.

## A few technical decisions

* Working with PDF files: I used PdfReader from the pypdf library to read the invoice PDFs and extract their text. The extracted text is then used to identify the required invoice information.

* Regular expressions: I used regular expressions to extract invoice numbers and supplier names. This works with the structure of the sample invoices used in this project.

* Handling financial values: I initially worked with regular numeric values, but changed the amount handling to Python's Decimal type. This is more suitable for financial calculations because it avoids common floating-point precision problems.

* Validation and duplicate checks: Before assigning a processing status, the application checks whether the required invoice information is available and valid. It also checks previously processed invoices to identify duplicates.

* Testing: I used pytest to test the processing rules, including boundary values, negative amounts, missing values, invalid data types and decimal precision.

## Technologies Used

* Python
* `pypdf` for PDF text extraction
* `re` for regular expressions
* `pathlib` for file handling
* Decimal
* pytest


## How to Run

* Install the required Python package: pip install -r requirements.txt

* Run the script from the project directory: python invoice_document_processor.py

* Run the tests: python -m pytest -v

## What I Learned

While building this project, I worked with PDF text extraction, regular expressions, exception handling, data validation, and duplicate detection. I also practised organising invoice data using Python functions, lists, and dictionaries.

One important part was handling documents that don't contain the expected information, instead of assuming every invoice will be valid.

This project is another step in my journey towards Python-based Intelligent Document Processing and intelligent automation.

