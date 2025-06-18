#decorator:
   # decorator is a function.
   # it takes function as an argument.
   #it retuens modified function as an argument.
# how to create a decorator:
# def login_required(function):

#     def inner(name,status):
#         if status==False:
#             print("please login")
#         else:
#             return function(name,status)
#     return inner
