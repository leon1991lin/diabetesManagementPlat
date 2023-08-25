from apiproject.repository import UserRepository


def get_all():
    return {"data": UserRepository.get_all()}

def search_user(searchInput:dict):

    for key, value in searchInput.items():
        if key == "user_id":
            return {"data": [UserRepository.get_user_by_id(value)]}

        elif key == "user_name":
            return {"data": UserRepository.get_user_by_name(value)}

        else:
            return {"data": []}

def insert_one(user:dict):

    if ("user_name" in user.keys()) \
        and ("user_account" in user.keys()) \
        and ("user_password" in user.keys()) \
        and ("born_date" in user.keys()) \
        and ("telephone" in user.keys()) \
        and ("user_type" in user.keys()):

        msg = UserRepository.insert_one(user)

    else:
        msg = f"Input Element Key Error: need 'user_name','user_account', 'user_password', 'born_date', 'telephone' and 'user_type'."

    return {"message": msg}

def update_one(user: dict):

    if "user_id" in user.keys():
        msg = UserRepository.update_one(user)
    else:
        msg = f"Update  Error: need 'user_id'."
    return msg

def delete_one_by_id(user_id):

    try:
        return {"message": UserRepository.delete_one_by_id(user_id)}
    except Exception as e:
        return {"message": f"Delete Error: {e}."}