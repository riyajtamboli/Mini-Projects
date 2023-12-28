from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["address_book"]

collection = db["contacts"]


def create_contact(contact_data):
    result = collection.insert_one(contact_data)
    print(f"Contact created with ID: {result.inserted_id}")

def read_contact(contact_name):
    contact = collection.find_one({"name": contact_name})
    if contact:
        print(contact)
    else:
        print(f"No contact found with name: {contact_name}")

def update_contact(contact_name, new_contact_data):
    result = collection.update_one({"name": contact_name}, {"$set": new_contact_data})
    if result.modified_count > 0:
        print("Contact updated successfully")
    else:
        print(f"No contact found with name: {contact_name}")

def delete_contact(contact_name):
    result = collection.delete_one({"name": contact_name})
    if result.deleted_count > 0:
        print("Contact deleted successfully")
    else:
        print(f"No contact found with name: {contact_name}")

if __name__ == "__main__":
    while True:
        print("\nAddress Book Application")
        print("1. Create Contact")
        print("2. Read Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_data = {"name": name, "phone": phone, "email": email}
            create_contact(contact_data)
        elif choice == "2":
            name = input("Enter contact name: ")
            read_contact(name)
        elif choice == "3":
            name = input("Enter contact name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            new_contact_data = {"phone": phone, "email": email}
            update_contact(name, new_contact_data)
        elif choice == "4":
            name = input("Enter contact name: ")
            delete_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")