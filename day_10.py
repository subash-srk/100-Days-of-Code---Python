def format_name(f_name, l_name):
    """Capitalize First Letter"""
    if f_name == "" or l_name == "":
        return "you didn't entered the name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
#   print(f"{formated_f_name} {formated_l_name}")

formated_name = format_name(input("First name: "), input("Last Name: "))
print(formated_name)
print(format_name("tAylor", "SWift"))
