from pathlib import Path
from pypdf import PdfReader
from decimal import Decimal, InvalidOperation
import re

folder_path = Path(r"C:\Users\Dell\OneDrive\Documents\Intelligent_Automation_Solutions\03_Invoice_Document_Processor\invoices")

def get_pdf_files(folder_path):
    pdf_files = []
    file_names = [f for f in folder_path.iterdir()]
    for f in file_names:
        if f.name.lower().endswith(".pdf"):
           pdf_files.append(f)
    return pdf_files
pdf_files = get_pdf_files(folder_path)

if not pdf_files:
    print("PDF File not found.")

def get_invoice_number(all_pdf_text):
    invoice_number = re.search(r"#\s*(\d+)", all_pdf_text)
    if invoice_number is not None:
        print("Invoice number is:", invoice_number.group(1))
        return invoice_number.group(1)
    else:
        print("Invoice number value is null.")
        return None


def get_supplier_name(all_pdf_text):
    supplier_name = re.search(r"#\s*(\d+)\n([^\n]+)", all_pdf_text)
    if supplier_name:
        return supplier_name.group(2)
    else:
        print("Supplier name value is null.")
        return None
    
def get_amount_value(invoice_parts):
    try:
        locating_position_amount = invoice_parts.index("Subtotal")
        amount_value = invoice_parts[locating_position_amount - 1]
        amount_value = Decimal(amount_value.replace("$", "").replace(",", ""))
    except (ValueError, TypeError, AttributeError):
        print("Amount value could not be extracted.")
        return None
    return amount_value

def validate_decimal_places(amount_value):
    if amount_value is None or isinstance(amount_value, bool):
        return False
    try:
        amount_value = Decimal(str(amount_value))
    except (InvalidOperation, TypeError, ValueError):
        return False
    if not amount_value.is_finite():
        return False

    return amount_value.as_tuple().exponent >= -2

def get_processing_action(amount_value):
    if (isinstance(amount_value, bool) or not isinstance(amount_value, (int, float, Decimal))) or validate_decimal_places(amount_value) == False:
        processing_status = "Manual Review"
    elif not validate_decimal_places(amount_value):
        processing_status = "Manual Review"
    elif amount_value < 0:
        processing_status = "Manual Review"
    elif amount_value <= 1000:
            processing_status = "Auto Process"
    elif amount_value <= 5000:
        processing_status = "Approval Required"
    else:
        processing_status = "Management Review"
    return processing_status

def validate_invoice(amount_value, invoice_number, supplier_name):
    validation_errors = []
    if not validate_decimal_places(amount_value):
        validation_errors.append("Amount value is invalid.")
    elif Decimal(str(amount_value)) < 0:
        validation_errors.append("Amount value is invalid.")
        
    if invoice_number is None:
        validation_errors.append("Invoice number is missing.")
        
    if supplier_name is None:
        validation_errors.append("Supplier name is missing.")

    if validation_errors:
        return False, validation_errors
    else:
        return True, None

def is_duplicate_invoice(invoice_number, processed_invoices):
    for processed_invoice in processed_invoices:
        if invoice_number == processed_invoice["invoice_number"]:
            return True

    return False

processed_invoices = []
manual_review_invoices = []
duplicate_invoices = []

def main():
    for f in pdf_files:
        info_dict = {}
        reader = PdfReader(f)
        pdf_pages = reader.pages
        print("PDF Name:", f.name,  ", & Number of PDF pages:", len(pdf_pages))
        all_pdf_text = ""

        for page in pdf_pages:
            pdf_text = page.extract_text() or ""
            all_pdf_text += pdf_text + "\n"

        invoice_parts = all_pdf_text.split()
        invoice_number = get_invoice_number(all_pdf_text)
        supplier_name = get_supplier_name(all_pdf_text)
        amount_value = get_amount_value(invoice_parts)
        validation_result, validation_reason = validate_invoice(amount_value, invoice_number, supplier_name)

        duplicate_result = False

        if validation_result:
            duplicate_result = is_duplicate_invoice(invoice_number, processed_invoices)       
            if duplicate_result:
                processing_status = "Manual Review Required"
                validation_reason = ["Duplicate invoice"]
            else:
                processing_status = get_processing_action(amount_value)
        else:
            processing_status = "Manual Review Required"   

        print(invoice_number)
        print(supplier_name)
        print(amount_value)
        print(processing_status)
        info_dict["invoice_number"] = invoice_number
        info_dict["supplier"] = supplier_name
        info_dict["amount"] = amount_value
        info_dict["validation_result"] = validation_result
        info_dict["validation_reason"] = validation_reason
        if validation_reason is not None and "Duplicate invoice" in validation_reason:
            duplicate_invoices.append(info_dict)
        info_dict["processing_status"] = processing_status
        if processing_status == "Manual Review Required":
            manual_review_invoices.append(info_dict)
        if validation_result and not duplicate_result:
            processed_invoices.append(info_dict)
        
        print(info_dict)
    
if __name__ == "__main__":
    main()

print("Processed invoices are:", processed_invoices, end="\n")
print("Manual review invoices are:", manual_review_invoices, end="\n")
print("Duplicate invoices are:", duplicate_invoices)