from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    """
    Student class with COMPLETE VALIDATION (like your friend's)
    """
    full_name: str          # Student's full name
    birthdate: str          # Birth date in YYYY-MM-DD format
    group: str              # Study group
    gpa: float             # Grade point average (0-5)

    def __post_init__(self):
        """
        Validate ALL fields after object creation
        """
        self._validate_full_name()
        self._validate_birthdate()
        self._validate_group()
        self._validate_gpa()
        print(f"✅ Student {self.full_name} created successfully!")

    # ========== VALIDATION METHODS ==========

    def _validate_full_name(self):
        """Validate full name (like your friend's version)"""
        # 1. Check type
        if not isinstance(self.full_name, str):
            raise TypeError("Full name must be a string")
        
        # 2. Check not empty
        if len(self.full_name.strip()) == 0:
            raise TypeError("Full name cannot be empty")
        
        # 3. Check characters (only letters, spaces, hyphen)
        for char in self.full_name:
            if not (char.isalpha() or char.isspace() or char == "-"):
                raise TypeError("Full name can only contain letters, spaces, and hyphen")
        
        # 4. Minimum 2 words (name and surname)
        name_parts = self.full_name.split()
        if len(name_parts) < 2:
            raise TypeError("Full name must contain at least 2 words (name and surname)")
        
        # 5. Each word starts with capital letter
        for name_part in name_parts:
            if not name_part[0].isupper():
                raise TypeError("Each word in full name must start with a capital letter")

    def _validate_birthdate(self):
        """Validate birth date (improved version)"""
        # 1. Check type
        if not isinstance(self.birthdate, str):
            raise ValueError("Birthdate must be a string")
        
        # 2. Check length (YYYY-MM-DD = 10 characters)
        if len(self.birthdate) != 10:
            raise ValueError("Birthdate must be in YYYY-MM-DD format (10 characters)")
        
        # 3. Check separators
        if self.birthdate[4] != "-" or self.birthdate[7] != "-":
            raise ValueError("Birthdate must be in YYYY-MM-DD format")
        
        # 4. Check all parts are digits
        year_part = self.birthdate[0:4]
        month_part = self.birthdate[5:7]
        day_part = self.birthdate[8:10]
        
        if not (year_part.isdigit() and month_part.isdigit() and day_part.isdigit()):
            raise TypeError("Birthdate can only contain digits")
        
        # 5. Check if date is valid
        try:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid birthdate (e.g., 2025-13-45)")
        
        # 6. Check date is not in the future
        today = date.today()
        if birth_date > today:
            raise ValueError("Birthdate cannot be in the future")

    def _validate_gpa(self):
        """Validate grade point average"""
        # 1. Check type (must be float or int)
        if not isinstance(self.gpa, (int, float)):
            raise TypeError("GPA must be a number (float or int)")
        
        # 2. Convert int to float if needed
        if isinstance(self.gpa, int):
            self.gpa = float(self.gpa)
        
        # 3. Check range 0-5
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5. Yours: {self.gpa}")

    def _validate_group(self):
        """Validate group number"""
        # 1. Check type
        if not isinstance(self.group, str):
            raise TypeError("Group must be a string")
        
        # 2. Check not empty
        if not self.group.strip():
            raise ValueError("Group cannot be empty")
        
        # 3. Check minimum length (at least 5 characters)
        if len(self.group) < 5:
            raise ValueError("Group is too short (minimum 5 characters)")

    # ========== MAIN METHODS ==========

    def age(self) -> int:
        """Calculate student's age in full years"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        # If birthday hasn't occurred yet this year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        
        return age

    def to_dict(self) -> dict:
        """Convert object to dictionary for JSON"""
        # Check all fields are filled
        if not self.full_name or not self.full_name.strip():
            raise ValueError("Field 'full_name' cannot be empty")
        
        if not self.birthdate or not self.birthdate.strip():
            raise ValueError("Field 'birthdate' cannot be empty")
        
        if not self.group or not self.group.strip():
            raise ValueError("Field 'group' cannot be empty")
        
        if self.gpa is None:
            raise ValueError("Field 'gpa' cannot be None")
        
        # Return dictionary
        return {
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create Student object from dictionary"""
        return cls(
            full_name=data['full_name'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )

    def __str__(self) -> str:
        """Pretty string representation"""
        return f"👨‍🎓 {self.full_name} | Group: {self.group} | GPA: {self.gpa} | Age: {self.age()} years"