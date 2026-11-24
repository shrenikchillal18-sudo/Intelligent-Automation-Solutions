from invoice_document_processor import get_processing_action


def test_small_invoice():
    result = get_processing_action(999.99) 
    assert result == "Auto Process"

def test_medium_invoice():
    result = get_processing_action(3500) 
    assert result == "Approval Required"

def test_large_invoice():
    result = get_processing_action(7000) 
    assert result == "Management Review"

def test_maximum_auto_process():
    result = get_processing_action(1000.00)
    assert result == "Auto Process"

def test_first_approval_amount():
    result = get_processing_action(1000.01)
    assert result == "Approval Required"

def test_maximum_approval_amount():
    result = get_processing_action(4999.99)
    assert result == "Approval Required"

def test_first_management_review_amount():
    result = get_processing_action(5000.0123)
    assert result == "Manual Review"

def test_second_management_review_amount():
    result = get_processing_action(5000.01)
    assert result == "Management Review"

def test_negative_invoice():
    result = get_processing_action(-100)
    assert result == "Manual Review"

def test_missing_invoice_amount():
    result = get_processing_action(None)
    assert result == "Manual Review"

def test_invalid_invoice_amount():
    result = get_processing_action("abc")
    assert result == "Manual Review"

def test_boolean_invoice_amount():
    result = get_processing_action(True)
    assert result == "Manual Review"