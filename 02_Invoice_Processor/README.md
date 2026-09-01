# Invoice Processor

## Overview

The Invoice Processor is a Python-based automation project that simulates the initial processing and validation of invoices.

The project collects invoice information, validates the input, determines the invoice processing action based on the invoice amount, identifies duplicate invoices, and stores the processed information in a structured list of dictionaries.

This project was created as part of a progressive learning path toward **Intelligent Automation, RPA, and Intelligent Document Processing (IDP)**.

## Features

* Process multiple invoices in one execution
* Capture invoice number
* Capture supplier name
* Capture invoice amount
* Validate invoice information
* Handle invalid invoice amounts using exception handling
* Determine invoice processing actions based on business rules
* Detect duplicate invoices
* Assign invoice status
* Store invoice information in structured dictionaries
* Store multiple invoices in a list

## Business Rules

### Invoice Validation

An invoice is considered valid when:

* Invoice number is not empty
* Supplier name is not empty
* Invoice amount is a valid number
* Invoice amount is greater than zero

Valid invoices receive:

`Ready`

Invalid invoices receive:

`Review required`

### Processing Rules

For valid invoices:

| Invoice Amount    | Processing Action |
| ----------------- | ----------------- |
| €0 – €1,000       | Auto Process      |
| > €1,000 – €5,000 | Approval Required |
| > €5,000          | Management Review |

### Duplicate Detection

Invoice numbers are used to identify duplicate invoices.

If an invoice number already exists in the processed invoice list, the invoice is classified as:

`Duplicate Invoice`

Otherwise:

`New Invoice`

Duplicate invoices require manual review.

## Example

Example processed invoice data:

```text
INV001 → €500 → Ready → New Invoice → Auto Process
INV002 → €3,500 → Ready → New Invoice → Approval Required
INV003 → €7,500 → Ready → New Invoice → Management Review
INV001 → Duplicate Invoice
INV004 → Invalid → Review Required → Manual Action Required
```

## Technologies

* Python
* Git
* GitHub

## Python Concepts Practiced

This project was used to strengthen the following Python concepts:

* Variables
* User input
* Data types
* Type conversion
* `if / elif / else`
* `for` loops
* `while` loops
* Functions
* Function parameters
* Return values
* Lists
* Dictionaries
* Boolean values
* `try / except`
* `ValueError`
* Generator expressions
* `any()`
* Data validation
* Business-rule implementation

## Project Structure

```text
02_Invoice_Processor/
│
├── invoice_processor.py
└── README.md
```

## Future Improvements

Potential improvements for a production-oriented version include:

* Read invoices directly from PDF documents
* Extract invoice data automatically
* OCR support for scanned invoices
* Improved duplicate handling
* Currency and VAT calculations
* Export results to Excel/CSV
* Logging and error reporting
* Integration with RPA workflows
* Cloud-based document processing
* Integration with Intelligent Document Processing services

## Learning Goal

This project serves as a foundation for the next stage of the learning path:

**Real Document Processing → Intelligent Document Processing → Python + RPA → Cloud Automation**

The next project will move away from manually entered invoice data and begin working with actual document files.
