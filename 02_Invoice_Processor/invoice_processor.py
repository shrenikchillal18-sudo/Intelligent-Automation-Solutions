invoice_list = []

def get_invoices_count():
    invoices_count = int(input("How many invoices needs to be processed? "))
    return invoices_count

def get_invoice_number():
    invoice_number = input("Please insert the invoice number? ").strip()
    return invoice_number

def get_invoice_amount():
    invoice_amount = input("Please insert the invoice amount? ").strip()
    return invoice_amount

def get_supplier_name():
    supplier_name = input("Please insert the supplier name? ").strip()
    return supplier_name

def validate_invoice(invoice_number, invoice_amount, supplier_name):
        try: 
            if float(invoice_amount) > 0 and (invoice_number) != "" and (supplier_name) != "":
                return True
            else:
                return False
        except ValueError:
            return False

def get_invoice_status(validate_invoice):
    if validate_invoice == True:
        invoice_status = "Ready"
    else:
        invoice_status = "Review required"
    return invoice_status

def get_processing_action(invoice_amount):
    invoice_amount = float(invoice_amount)
    if invoice_amount > 0 and invoice_amount <= 1000:
       processing_action = "Auto Process"
    elif invoice_amount <= 5000:
       processing_action = "Approval Required"
    else:
        processing_action = "Management Review"
    return processing_action

invoices_count = get_invoices_count()

for n in range(invoices_count):
    invoice_dict = {}
    print("Document processing: ", n + 1)

    invoice_number = get_invoice_number()
    print("Invoice number is:", invoice_number)

    invoice_amount = get_invoice_amount()
    print("Invoice amount is:", invoice_amount)

    supplier_name = get_supplier_name()
    print("Supplier name is:", supplier_name)

    validation_result = validate_invoice(invoice_number, invoice_amount, supplier_name)

    invoice_status = get_invoice_status(validation_result)
    print("Invoice status is:", invoice_status)

    if validation_result == True:
        processing_action = get_processing_action(invoice_amount)
        invoice_amount = float(invoice_amount)
        print(processing_action)
    else:
        processing_action = "Manual action required"
        print(processing_action)

    invoice_dict["invoice_number"] = invoice_number
    invoice_dict["invoice_amount"] = invoice_amount
    invoice_dict["supplier_name"] = supplier_name
    invoice_dict["status"] = invoice_status
    

    if any(invoice_number["invoice_number"] == invoice_dict["invoice_number"] for invoice_number in invoice_list):
        invoice_dict["invoice_type"] = "Duplicate Invoice"
        invoice_dict["processing_action"] = "Manual Review"
    else:
        invoice_dict["invoice_type"] = "New Invoice"

    invoice_dict["processing_action"] = processing_action
    invoice_list.append(invoice_dict)

print(invoice_list)    
