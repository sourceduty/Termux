import os

TEMPLATES = {
    "Product Record": "Product Record\n===============\nProduct Name: \nCategory: \nQuantity: \nPrice per Unit: \n",
    "Supplier Record": "Supplier Record\n===============\nSupplier Name: \nContact Information: \nProducts Supplied: \n",
    "Stock Adjustment": "Stock Adjustment\n================\nProduct Name: \nAdjustment Date: \nQuantity Adjusted: \nReason: \n",
}

def main_menu():
    print("Inventory Management System")
    print("==========================")
    print("1. Add a new inventory record")
    print("2. Add a record from template")
    print("3. View a record")
    print("4. Update a record")
    print("5. Delete a record")
    print("6. List all records")
    print("7. List templates")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    return choice

def add_record():
    title = input("Enter the record title: ")
    content = input("Enter the record content: ")
    filename = title + ".txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"Record '{title}' added successfully.")

def add_record_from_template():
    list_templates(show=True)
    template_choice = input("Enter the template name or number to use: ")
    template_content = None
    
    if template_choice.isdigit():
        template_choice = int(template_choice)
        if 1 <= template_choice <= len(TEMPLATES):
            template_content = list(TEMPLATES.values())[template_choice - 1]
        else:
            print("Invalid template number.")
            return
    elif template_choice in TEMPLATES:
        template_content = TEMPLATES[template_choice]
    else:
        print("Invalid template name.")
        return

    title = input("Enter the record title: ")
    filename = title + ".txt"
    with open(filename, "w") as file:
        file.write(template_content)
    print(f"Record '{title}' added successfully from template.")

def view_record():
    records = list_records(show=False)
    if records:
        try:
            record_number = int(input("Enter the record number to view: "))
            if 1 <= record_number <= len(records):
                filename = records[record_number - 1]
                with open(filename, "r") as file:
                    content = file.read()
                print(f"\nRecord content for '{filename.replace('.txt', '')}':\n")
                print(content)
            else:
                print("Invalid record number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No records available to view.")

def update_record():
    records = list_records(show=False)
    if records:
        try:
            record_number = int(input("Enter the record number to update: "))
            if 1 <= record_number <= len(records):
                filename = records[record_number - 1]
                content = input("Enter the new content: ")
                with open(filename, "w") as file:
                    file.write(content)
                print(f"Record '{filename.replace('.txt', '')}' updated successfully.")
            else:
                print("Invalid record number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No records available to update.")

def delete_record():
    records = list_records(show=False)
    if records:
        try:
            record_number = int(input("Enter the record number to delete: "))
            if 1 <= record_number <= len(records):
                filename = records[record_number - 1]
                os.remove(filename)
                print(f"Record '{filename.replace('.txt', '')}' deleted successfully.")
            else:
                print("Invalid record number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No records available to delete.")

def list_records(show=True):
    files = [f for f in os.listdir() if f.endswith('.txt') and not f.startswith('template_')]
    if show:
        if files:
            print("\nList of all records:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file.replace('.txt', '')}")
        else:
            print("No records available.")
    return files

def list_templates(show=False):
    templates = list(TEMPLATES.keys())
    if show:
        if templates:
            print("\nList of templates:")
            for i, template in enumerate(templates, start=1):
                print(f"{i}. {template}")
        else:
            print("No templates available.")
    return templates

def run_inventory_system():
    while True:
        choice = main_menu()
        if choice == '1':
            add_record()
        elif choice == '2':
            add_record_from_template()
        elif choice == '3':
            view_record()
        elif choice == '4':
            update_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            list_records()
        elif choice == '7':
            list_templates(show=True)
        elif choice == '8':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    run_inventory_system()