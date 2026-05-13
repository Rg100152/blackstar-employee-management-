import os
import time
import json
import platform
from datetime import datetime

# ==================== Colors ====================
class Colors:
    G = '\033[92m'   # Green
    R = '\033[91m'   # Red
    C = '\033[96m'   # Cyan
    Y = '\033[93m'   # Yellow
    W = '\033[0m'    # Reset
    B = '\033[94m'   # Blue

# ==================== Config ====================
DB_FILE = "blackstar_db.json"

# ==================== Banner ====================
def banner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.G + r"""
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ███████╗████████╗██████╗ ██████╗ 
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
    ██████╦╝██║     ███████║██║     █████╔╝     ███████╗   ██║   ███████║██████╔╝
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ╚════██║   ██║   ██╔══██║██╔══██╗
    ██████╦╝███████╗██║  ██║╚██████╗██║  ██╗    ███████║   ██║   ██║  ██║██║  ██║
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
    """ + Colors.W)
    print(Colors.C + "              [ Project Black Star - Employee Management System ]" + Colors.W)
    print(Colors.Y + f"              Version 2.0 | {datetime.now().strftime('%Y-%m-%d %H:%M')}" + Colors.W)
    print("=" * 80 + "\n")

# ==================== Database ====================
def load_data():
    try:
        if not os.path.exists(DB_FILE):
            with open(DB_FILE, 'w') as f:
                json.dump({}, f, indent=4)
            return {}
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(Colors.R + f"[!] Database Error: {e}" + Colors.W)
        return {}

def save_data(data):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception:
        print(Colors.R + "[!] Failed to save database!" + Colors.W)
        return False

# ==================== Operations ====================
def add_employee():
    data = load_data()
    banner()
    print(Colors.C + ">>> ADD NEW TARGET" + Colors.W + "\n")
    
    emp_id = input(Colors.G + "Enter Employee ID: " + Colors.W).strip()
    if not emp_id:
        print(Colors.R + "[!] ID cannot be empty!" + Colors.W)
        time.sleep(1.5)
        return
    
    if emp_id in data:
        print(Colors.R + "[!] Employee ID already exists in database!" + Colors.W)
        time.sleep(1.5)
        return

    name = input(Colors.G + "Enter Full Name: " + Colors.W).strip()
    role = input(Colors.G + "Enter Role / Position: " + Colors.W).strip()
    salary = input(Colors.G + "Enter Salary: " + Colors.W).strip()

    if not all([name, role, salary]):
        print(Colors.R + "[!] All fields are required!" + Colors.W)
        time.sleep(1.5)
        return

    data[emp_id] = {
        "Name": name,
        "Role": role,
        "Salary": salary,
        "Added_On": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Last_Modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if save_data(data):
        print(Colors.G + "\n[+] Target successfully added to Black Star Database!" + Colors.W)
    time.sleep(2)

def view_employee():
    data = load_data()
    banner()
    print(Colors.C + ">>> SEARCH TARGET" + Colors.W + "\n")
    
    emp_id = input(Colors.G + "Enter Employee ID: " + Colors.W).strip()
    
    if emp_id in data:
        emp = data[emp_id]
        print(Colors.G + "\n[+] TARGET LOCATED SUCCESSFULLY" + Colors.W)
        print(f"{Colors.C}ID           :{Colors.W} {emp_id}")
        print(f"{Colors.C}Name         :{Colors.W} {emp['Name']}")
        print(f"{Colors.C}Role         :{Colors.W} {emp['Role']}")
        print(f"{Colors.C}Salary       :{Colors.W} ₹{emp['Salary']}")
        print(f"{Colors.C}Added On     :{Colors.W} {emp['Added_On']}")
        print(f"{Colors.C}Last Modified:{Colors.W} {emp.get('Last_Modified', 'N/A')}")
    else:
        print(Colors.R + "\n[!] Target Not Found in Database." + Colors.W)
    
    input(Colors.C + "\nPress ENTER to continue..." + Colors.W)

def list_employees():
    data = load_data()
    banner()
    print(Colors.C + f">>> ALL TARGETS ({len(data)})" + Colors.W + "\n")
    
    if not data:
        print(Colors.R + "No employees found in database." + Colors.W)
        input(Colors.C + "\nPress ENTER..." + Colors.W)
        return

    print(f"{Colors.Y}{'ID':<10} {'Name':<25} {'Role':<25} {'Salary':<12} {'Added On'}{Colors.W}")
    print("-" * 80)
    
    for emp_id, info in data.items():
        print(f"{Colors.G}{emp_id:<10}{Colors.W} {info['Name']:<25} {info['Role']:<25} "
              f"₹{info['Salary']:<12} {info['Added_On'][:10]}")
    
    input(Colors.C + "\nPress ENTER to continue..." + Colors.W)

def update_employee():
    data = load_data()
    banner()
    print(Colors.C + ">>> UPDATE TARGET" + Colors.W + "\n")
    
    emp_id = input(Colors.G + "Enter Employee ID to update: " + Colors.W).strip()
    
    if emp_id not in data:
        print(Colors.R + "[!] Employee ID not found!" + Colors.W)
        time.sleep(1.5)
        return

    print(Colors.Y + "\nLeave blank to keep current value\n" + Colors.W)
    
    name = input(Colors.G + f"Name ({data[emp_id]['Name']}): " + Colors.W).strip()
    role = input(Colors.G + f"Role ({data[emp_id]['Role']}): " + Colors.W).strip()
    salary = input(Colors.G + f"Salary (₹{data[emp_id]['Salary']}): " + Colors.W).strip()

    if name:
        data[emp_id]["Name"] = name
    if role:
        data[emp_id]["Role"] = role
    if salary:
        data[emp_id]["Salary"] = salary
    
    data[emp_id]["Last_Modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if save_data(data):
        print(Colors.G + "\n[+] Target data successfully updated!" + Colors.W)
    time.sleep(2)

def delete_employee():
    data = load_data()
    banner()
    print(Colors.C + ">>> DELETE TARGET" + Colors.W + "\n")
    
    emp_id = input(Colors.G + "Enter Employee ID to delete: " + Colors.W).strip()
    
    if emp_id not in data:
        print(Colors.R + "[!] Employee ID not found!" + Colors.W)
        time.sleep(1.5)
        return

    confirm = input(Colors.R + f"Are you sure you want to delete {emp_id} ({data[emp_id]['Name']})? (y/n): " + Colors.W).lower()
    
    if confirm == 'y':
        del data[emp_id]
        if save_data(data):
            print(Colors.G + "[+] Target successfully eliminated from database." + Colors.W)
    else:
        print(Colors.Y + "[i] Operation cancelled." + Colors.W)
    time.sleep(2)

# ==================== Main Menu ====================
def main_menu():
    while True:
        banner()
        print(f"{Colors.G}[1]{Colors.W} Add New Employee")
        print(f"{Colors.G}[2]{Colors.W} Search Employee by ID")
        print(f"{Colors.G}[3]{Colors.W} List All Employees")
        print(f"{Colors.G}[4]{Colors.W} Update Employee")
        print(f"{Colors.G}[5]{Colors.W} Delete Employee")
        print(f"{Colors.G}[6]{Colors.W} Exit Black Star\n")
        
        choice = input(Colors.C + "root@blackstar:\~# " + Colors.W).strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employee()
        elif choice == '3':
            list_employees()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print(Colors.R + "\n[!] Shutting down Project Black Star... Goodbye!" + Colors.W)
            time.sleep(1.5)
            break
        else:
            print(Colors.R + "\n[!] Invalid Command!" + Colors.W)
            time.sleep(1)

# ==================== Start ====================
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Colors.R + "\n\n[!] Program terminated by user." + Colors.W)
