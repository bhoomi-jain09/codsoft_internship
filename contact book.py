#contact book
contacts={}
#function for add number
def addnumber():
    name=input("enter the name:")
    phone_number=input("enter the phone number")
    if name not in contacts:
        contacts[name]= phone_number
        print(f"contact {name} added successfully")
    else:
        print("contact already exist!!!")
#function for delete number
def deletenumber():
    name=input("enter the name you want to delete:")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully")
    else:
        print("no contact found")
#function for view contact list
def viewbook():
    print("\ncontact list")
    if contacts:
        for name,phone_number in contacts.items():
            print(f"{name}:{phone_number}")
    else:
        print("no contact found")
#function for search number
def searchcontact():
    name=input("enter the name:")
    if name in contacts:
        print(f"{name}:{contacts[name]}")
    else:
        print("no contact found")
def main():
    while True:
        print("1.view your contactbook")
        print("2.add contact")
        print("3.delete contact")
        print("4.search contact")
        print("5.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            viewbook()
        elif choice==2:
            addnumber()
        elif choice==3:
            deletenumber()
        elif choice==4:
            searchcontact()
        elif choice==5:
            print("exiting the contactbook\nGoodbye!")
            break
        else:
            print("enter valid choice")
main()