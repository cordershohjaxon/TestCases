def get_full_name(name, surename, otasi=''):
    if otasi:
        return f"{name} {otasi} {surename}".title()
    else:
        return f"{name} {surename}".title()

