import json

def convert_retail_items():
    # Open the JSON file and load its contents
    with open('retailitems.json', 'r') as f:
        data = json.load(f)

    # Loop over each item in the list
    for item in data:
        # Extract the AttributeName and ID
        item_id = item['ID']
        # Combine them to form the new values
        new_display_name =  'DisplayName_' + item_id
        new_norm_name = 'NormName_' + item_id
        new_supplier_name =  '仕入先名_' + item_id
        # Update the corresponding fields with the new values
        item['Category'] = 'Category_' + item_id
        item['DisplayName'] = new_display_name
        item['NormName'] = new_norm_name
        item['仕入先名'] = new_supplier_name

    # Write the modified data back to the JSON file
    with open('retailitems_out.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)

def convert_payments():
    # Open the JSON file and load its contents
    with open('payments.json', 'r') as f:
        data = json.load(f)

    # Loop over each item in the list
    for item in data:
        # Extract the AttributeName and ID
        item_id = item['SalesId']
        item['Payment ID'] = 'PaymentID_' + item_id

    # Write the modified data back to the JSON file
    with open('payments_out.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def convert_salesdetails():
    # Open the JSON file and load its contents
    with open('salesdetails.json', 'r') as f:
        data = json.load(f)

    # Loop over each item in the list
    for item in data:
        # Extract the AttributeName and ID
        item_id = item['ID']
        item['Customer'] = 'Customer_' + item_id
        item['Staff'] = 'Staff_' + item_id

    # Write the modified data back to the JSON file
    with open('salesdetails_out.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)

def convert_salonitems():
    # Open the JSON file and load its contents
    with open('salesdetails.json', 'r') as f_detail:
        data = json.load(f_detail)

    salon_items_detail = set()
    # Loop over each item in the list
    for item in data:
        if item['ItemType'] == '技術':
            salon_items_detail.add( item['ItemId'])

    with open('salonitems.json', 'r') as f:
        data = json.load(f)

    salon_items = []
    for item in data:
        if item['ID'] in salon_items_detail:
            item['Category'] = 'Category_' + item['ID']
            item['DisplayName'] = 'DisplayName_' + item['ID']
            item['NormName'] = 'NormName_' + item['ID']
            salon_items.append(item)

    # Write the modified data back to the JSON file
    with open('salonitems_out.json', 'w') as f:
        json.dump(salon_items, f, ensure_ascii=False)


if __name__ == '__main__':
    convert_salonitems()  


