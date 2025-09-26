# src/04_minutes_to_hhmm.py
# Ask user for minutes
minutes = int(input("Minutes: "))
# Calculate hours and minutes
hours = minutes // 60
remaining_minutes = minutes % 60
# Display in HH:MM format
print(f"{hours}:{remaining_minutes:02d}")