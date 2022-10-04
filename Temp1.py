#**____Functions_____**

def c_to_f(temp):
    f = (temp *1.8) + 32
    return (f" Your degrees {temp} C = {f} degrees F")

def f_to_c(temp, name):
    c = (temp - 32) * (5/9)
    return (f"Your degrees {temp} F = {c} degrees C")
    

#***______Main Code_________***
user_choice = input("C or F ")
user_temp = int(input("What temperature C or F? "))
    
if user_choice == "C":
    output = c_to_f(user_temp)
    
else:
    output = f_to_c(user_temp)

print(output)
