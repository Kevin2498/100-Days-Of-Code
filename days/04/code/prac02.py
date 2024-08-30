
def is_auth(user):
    return(user == "Kevin")


def auth(func):
    def wrapper(**kwargs):
        username = kwargs.get('user')
        print(f"Checking auth for {username}")
        if(is_auth(username)):
            val = func(**kwargs)
            return val
        else:
            return(f"{username} is not authenticated")
    return wrapper


@auth
def check_access(user):
    return(f"{user} is authenticated")


print(check_access(user="Kevin"))
print(check_access(user="Athu"))