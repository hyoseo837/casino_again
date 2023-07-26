from database_operations import fetch_data_by_email

def is_email_valid(email):
    if not('@' in email and '.' in email):
        return False
    else:
        result = fetch_data_by_email(email)
        if result == []:
            return True
        else:
            return False
        
def is_name_valid(name):
    if len(name) > 50:
        return False
    else:
        return True
    
def is_password_valid(pw1,pw2):
    if pw1 != pw2:
        return False
    else:
        return True