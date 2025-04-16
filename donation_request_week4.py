import uuid


# Task 1: Capture requester name, project name and generate unique request ID
def create_donation_request():
    requester_name = input("Enter requester's name: ")
    project_name = input("Enter project name: ")
    request_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
    return requester_name, project_name, request_id


# Task 2: Collect request items and calculate total
def get_request_items():
    requester_name, project_name, request_id = create_donation_request()
    total_amount = 0
    items = []

    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            item_price = float(input(f"Enter price for {item_name}: "))
            items.append((item_name, item_price))
            total_amount += item_price
        except ValueError:
            print("Invalid input. Please enter a number for the price.")

    return requester_name, project_name, request_id, total_amount


# Task 3: Approval decision based on conditions
def approval_decision():
    requester_name, project_name, request_id, total_amount = get_request_items()
    approval_status = "Pending"
    priority = "Low"
    approval_id = "N/A"

    if "family" in project_name.lower():
        priority = "High"
        approval_status = "Approved"
        approval_id = request_id + requester_name[-2:]
    elif total_amount < 500:
        priority = "Medium"
        approval_status = "Approved"
        approval_id = request_id + requester_name[:2]

    return requester_name, project_name, request_id, total_amount, approval_status, priority, approval_id


# Task 4: Display the output and save the details to a file
def display_output_and_save():
    requester_name, project_name, request_id, total_amount, approval_status, priority, approval_id = approval_decision()

    # Display the donation request summary
    print("\n--- Donation Request Summary ---")
    print(f"Requester Name   : {requester_name}")
    print(f"Project Name     : {project_name}")
    print(f"Request ID       : {request_id}")
    print(f"Total Requested  : ${total_amount:.2f}")
    print(f"Approval Status  : {approval_status}")
    print(f"Priority Level   : {priority}")
    print(f"Approval ID      : {approval_id}")

    # Save to a file
    with open("donation_requests.txt", "a") as file:
        file.write(f"--- Donation Request ---\n")
        file.write(f"Requester Name   : {requester_name}\n")
        file.write(f"Project Name     : {project_name}\n")
        file.write(f"Request ID       : {request_id}\n")
        file.write(f"Total Requested  : ${total_amount:.2f}\n")
        file.write(f"Approval Status  : {approval_status}\n")
        file.write(f"Priority Level   : {priority}\n")
        file.write(f"Approval ID      : {approval_id}\n")
        file.write(f"---------------------\n\n")


# Run the program
display_output_and_save()
