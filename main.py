list = []
while True:
    set = {}
    date = input("Enter a date (YYYY-MM-DD): ")
    dates= date.split("-")
    for i,d in enumerate(dates):
        dates[i] = int(d)
    if dates[0] > 31 or dates[0] < 0:
        print("Invalid Date")
        continue
    elif dates[1] > 12 or dates[1] < 0:
        print("Invalid Date")
        continue
    elif dates[2] > 2026 or dates[2] < 0:
        print("Invalid Date")
        continue
    else:
        category = input("Enter category: ")
        amount = eval(input("Enter amount: "))
        if amount < 0:
            print("Invalid Amount")
            continue
        else:
            set["Date"] = date
            set["Category"] = category
            set["Amount"] = amount
            list.append(set)
            choice = input("\nDo you want to add another entry? (yes/no):")
            if choice.lower() == "no":
                print("\n")
                break
            elif choice.lower() == "yes":
                print("\n")
                continue
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                break
print("Date,Category,Amount")
for set in list:
    print(f"{set['Date']},{set['Category']},{set['Amount']}")
