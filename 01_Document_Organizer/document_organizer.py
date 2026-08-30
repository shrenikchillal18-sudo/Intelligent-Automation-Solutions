documents = []

def get_document_type():
    document_type  = input("Enter document type: ").strip().lower()
    
    return document_type

document_categories = {"invoice":"Financial Document", "po":"Procurement Document", "contract":"Legal Document", "":"Unknown"}

def get_category(document_type):
    document_category = document_categories.get(document_type, "Unknown")
  
    return document_category

def get_page_count(document_category):
    if document_category != "Unknown":
        while True:
            try:
                number_of_pages  = int(input("Enter the number of pages: "))
            except ValueError:
                print("That is not valid number. Please enter the number again")
                continue    
            if number_of_pages <= 0:
                print("Pages must be greater than Zero.")
                continue     
            break
    else:
        number_of_pages = "Number of pages not required."
        
    return number_of_pages

def get_document_status():
    document_status = "Ready"
    return document_status

document_destination_dictionary = {"Financial Document":"Financial Documents", "Procurement Document":"Procurement Documents", "Legal Document":"Legal Documents", "Unknown":"No destination"}

def get_document_destination(document_category):
    document_destination = document_destination_dictionary.get(document_category, "No destination")
    return document_destination

number = int(input("How many documents needs to be processed? " ))

for n in range(number):
        document_dictionary = {}

        print("Document needed to be precessed number:", n+1)

        document_type = get_document_type()

        document_category = get_category(document_type)
        print("Document category is: ",document_category)

        document_count = get_page_count(document_category)
        print("Document page count is: ",document_count)

        document_status = get_document_status()

        document_destination = get_document_destination(document_category)
        
        if document_category != "Unknown":
            document_dictionary["type"] = document_type
            document_dictionary["category"] = document_category
            document_dictionary["pages"] = document_count
            document_dictionary["status"] = document_status
            document_dictionary["destination"] = document_destination
            documents.append(document_dictionary)    
        else:
            print("Since document is Unknown we are not adding it.")    

print("Documents entered details: ", documents) 

for num, document in enumerate(documents, start=1):
    print("Document:", num)
    print("Document type:",document["type"])   
    print("Document category:",document["category"])
    print("Document pages:",document["pages"])
    print("Document status:",document["status"])
    print("Document destination:",document["destination"])

