def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec, tuple):
        raise TypeError("Input must be a tuple")

    if len(rec) != 3:
        raise ValueError("Tuple must have exactly 3 elements")

    name, group, grade = rec

    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    if not isinstance(group, str):
        raise TypeError("Group must be a string")

    if not isinstance(grade, (int, float)):
        raise TypeError("GPA must be a number")

    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not group.strip():
        raise ValueError("Group cannot be empty")

    if grade < 0:
        raise ValueError("GPA cannot be negative")

    name = name.strip()
    while "  " in name:
        name = name.replace("  ", " ")

    name = name.title()

    parts = name.split()
    last_name = parts[0]

    initials = ""
    if len(parts) > 1:
        initials = parts[1][0] + "."
    if len(parts) > 2:
        initials = initials + parts[2][0] + "."
    gpa_str = f"{grade:.2f}"

    result = last_name + " " + initials + ", gr. " + group + ", GPA " + gpa_str

    return result


print("=== PRUEBAS CORRECTAS ===")
print("1.", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print("2.", format_record(("Петров Пётр", "IKBO-12", 5.0)))
print("3.", format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print("4.", format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
