from decorator1 import login_required

def homepage(name,status):
    print("Home page")

@login_required
def services(name,status):
    print("service page")

@login_required
def products(name,status):
    print("product page")

def contact(name,status):
    print("contact page")

homepage("john",True)
services("python",False)
products("html,css",True)
contact(6281898087,True)

