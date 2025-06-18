def login_req(func):

    def inner(name,status):
        if status==False:
            print("login please")
        else:
            return func(name,status)
        
    return inner    

def login_required(func):

    def inner(email,status):
        if status==False:
            print("please enter email")
        else:
            return func(email,status)
        
    return inner    

def login_req(func):

    def inner(number,status):
        if status==False:
            print("please enter phone number")
        else:
            return func(number,status)
        
    return inner    

def login_req(func):

    def inner(id,status):
        if status==False:
            print("please enter login id")
        else:
            return func(id,status)
        
    return inner    





