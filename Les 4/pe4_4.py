def new_password(oldpassword, newpassword):
    if newpassword is not oldpassword and len(newpassword) > 6 and any(i.isdigit() for i in newpassword):
        return True
    else: return False

print(new_password("hallo123", "hallosadasd"))