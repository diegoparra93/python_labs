def format_record(rec):
    # Separate data
    name = rec[0]
    group = rec[1] 
    grade = rec[2]
    
    # Clean name spaces
    name = name.strip()
    while "  " in name:
        name = name.replace("  ", " ")
    
    # Capitalize
    name = name.title()
    
    # Split words
    parts = name.split()
    last_name = parts[0]
    
    # Make initials
    initials = ""
    if len(parts) > 1:
        initials = parts[1][0] + "."
    if len(parts) > 2:
        initials = initials + parts[2][0] + "."
    
    # Format GPA with 2 decimals
    gpa_str = f"{grade:.2f}"
    
    # Put everything together
    result = last_name + " " + initials + ", gr. " + group + ", GPA " + gpa_str
    
    return result

# Testing the function
print("=== Testing format_record ===")

test1 = format_record(("Иван де Иисус Иванович", "BIVT-25", 4.6))
print("Input: ('Иван де Иисус Иванович', 'BIVT-25', 4.6)")
print("Output:", test1)
print()

test2 = format_record(("Диего Парра", "IKBO-12", 5.0))
print("Input: ('Диего Парра', 'IKBO-12', 5.0)")
print("Output:", test2)
print()

test3 = format_record((" Сидорова Анна Сергеевна ", "ABB-01", 3.999))
print("Input: ( - Сидорова Анна Сергеевна - , 'ABB-01', 3.999)")
print("Output:", test3)
print()

test4 = format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
print("Input: ('Петров Пётр Петрович', 'IKBO-12', 5.0)")
print("Output:", test4)