def create_admin_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "admin", "2024-01-01", True


def create_editor_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "editor", "2024-01-01", True


def create_viewer_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "viewer", "2024-01-01", True



def create_user(name,email,type_user):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    if type_user not in ['admin','editor','viewer']:
       raise ValueError ('enter a valid user type')
    return name, email, type_user, "2024-01-01", True

create_user('avi','@','adminF')