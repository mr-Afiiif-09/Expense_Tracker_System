import json    #Importing json file

expenses = []
 
#Opening the file using json
try:     
    with open('expenses.json','r') as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses= []

#defining function to save data into json file
def save():
    with open('expenses.json','w',) as f:
        json.dump(expenses,f,indent = 4)

# preparing the menu of program
while True:
    print("------Expense Tracker System------")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.Search Expenses")
    print("4.Delete Expense")
    print("5.Total Expenses")
    print("6.Category-wise Summary")
    print("7.Exit the System")

    choice = input("Enter your choice:")

#Adding data and declaring Data struture
    if choice == '1':
        Date = (input("Enter Date (YYYY-MM-DD):"))
        Category = input("Enter Category:")
        Amount = float(input("Enter Amount:"))
        Description = input("Enter Description:")

        expense = {
            "Date" : Date,
            "Category" : Category,
            "Amount" : Amount,
            "Description" : Description
        }
        expenses.append(expense)
        save()
        print("\n Added Successfully.")

    elif choice =='2':
        if len(expenses) == 0:
            print("Expense not Found.")
        else:
            for expense in expenses:
                print(
                    f"Date:{expense['Date']}",
                    f"Category:{expense['Category']}",
                    f"Amount:{expense['Amount']}",
                    f"Description:{expense['Description']}"
                )

    elif choice =='3':
        Date = (input("Enter Date of expense to search:"))
        found = False

        for expense in expenses:
            if expense['Date'] == Date:
                print(expense)
                found = True
                break
            else:
                print("Date not found.")

    elif choice == '4':
        Date = (input("Enter Date of expense to delete:"))
        found = False

        for expense in expenses:
            if expense['Date'] == Date:
                expenses.remove(expense)
                save()
                print("Expense deleted successfully.")
                found = True
                break
            else:
                print("Expense Date not found.")
    
    elif choice == '5':
        total = sum(float(expense["Amount"]) for expense in expenses)
        print("Total Expenses spent are:",total)
        break

    elif choice == '6':
        summary = {}

        for expense in expenses:
            category = expense['Category']
            amount = float(expense['Amount'])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("\n Category Wise Summary")

        for category,total in summary.items():
            print(f"{category}: ₹{total}")

    elif choice == '7':
        print("Closing the System.")
    
    else:
        print("Invalid choice.")
    

    