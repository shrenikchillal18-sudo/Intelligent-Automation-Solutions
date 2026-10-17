# Invoice Document Processor

## About the Project

This project is a Python-based invoice processing script that reads invoice PDFs and extracts important details such as the invoice number, supplier name, and invoice amount.

I built it to practise automating a common business process: processing incoming invoices, checking whether the extracted data is valid, identifying duplicates, and deciding which invoices can be processed automatically and which need further review.

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

## Technologies Used

* Python
* `pypdf` for PDF text extraction
* `re` for regular expressions
* `pathlib` for file handling

## Project Structure

```text
03_Invoice_Document_Processor/
├── invoices/
├── invoice_document_processor.py
└── README.md
```

The `invoices` folder contains sample PDFs used to test the script, including a duplicate invoice and an invalid document.

## How to Run

Install the required Python package:

```bash
python -m pip install pypdf
```

Run the script from the project directory:

```bash
python invoice_document_processor.py
```

The extracted invoice details and processing results will be displayed in the terminal.

## What I Learned

While building this project, I worked with PDF text extraction, regular expressions, exception handling, data validation, and duplicate detection. I also practised organising invoice data using Python functions, lists, and dictionaries.

One important part was handling documents that don't contain the expected information, instead of assuming every invoice will be valid.

## Next Steps

* Improve extraction for invoices with different layouts.
* Add OCR support for scanned PDFs.
* Export the results to CSV or Excel.
* Add automated tests and more robust validation.
* Explore AI-based document processing solutions.
