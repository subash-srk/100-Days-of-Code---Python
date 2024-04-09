try:
    file = open("a_file.txt")
    dict_a = {"key": "value"}
    print(dict_a["sddfs"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello")
except KeyError as error_msg:
    print(f"The key {error_msg} is not exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise KeyError("The is My Error")
