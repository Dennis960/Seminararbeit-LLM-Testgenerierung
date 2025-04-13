import re

def check_password_strength(password: str) -> str:
    criteria = [
        len(password) >= 8 and len(password) <= 20,
        re.search(r'[A-Z]', password) is not None,
        re.search(r'[a-z]', password) is not None,
        re.search(r'[0-9]', password) is not None,
        re.search(r'[!@#$%^&*()_-]', password) is not None
    ]
    
    met_criteria = sum(criteria)
    
    if met_criteria == 5:
        return "Strong"
    elif met_criteria == 4:
        return "Moderate"
    else:
        return "Weak"