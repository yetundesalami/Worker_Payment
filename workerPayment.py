import random

def generate_workers(num=400):
    """Dynamically generates a list of worker dictionaries."""
    workers = []
    for i in range(1, num + 1):
        name = f"Worker_{i}"
        salary = random.randint(5000, 35000)
        gender = random.choice(["Male", "Female"])
        workers.append({"ID": i, "Name": name, "Salary": salary, "Gender": gender})
    return workers

def determine_employee_level(worker):
    """Determines the employee level based on salary and gender conditions."""
    try:
        salary = worker["Salary"]
        gender = worker["Gender"]
        level = "N/A"  # Default level
        
        if 10000 < salary < 20000:
            level = "A1"
        if 7500 < salary < 30000 and gender == "Female":
            level = "A5-F"
        
        worker["Employee Level"] = level
    except KeyError as e:
        print(f"Missing key in worker data: {e}")
    except Exception as e:
        print(f"Error processing worker data: {e}")

def generate_payment_slips(workers):
    """Prints payment details for each worker."""
    print("\nPayment Slips:\n")
    print("{:<5} {:<12} {:<8} {:<8} {:<10}".format("ID", "Name", "Salary", "Gender", "Level"))
    print("-" * 50)
    
    for worker in workers:
        print("{:<5} {:<12} {:<8} {:<8} {:<10}".format(
            worker["ID"], worker["Name"], worker["Salary"], worker["Gender"], worker["Employee Level"]
        ))

# Main Execution
workers = generate_workers()
for worker in workers:
    determine_employee_level(worker)
generate_payment_slips(workers)
