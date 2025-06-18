from decorator2 import login_required, login_req

def homepage(name,status):
    print("home page")

@login_required
def email(email,status):
    print("email address")

def ph_number(number,status):
    print("phone number")

@login_req
def user_id(id,status):

    print("login")

homepage("john",True)
email("john16@gmail.com",False)
ph_number(6272727272,True)
user_id("john_16",False)

