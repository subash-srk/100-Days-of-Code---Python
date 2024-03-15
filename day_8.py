def greet():
  print("Hello")
  print("How are you?")
  print("Isn't the weather nice today?")

#greet()

def greet_name(name):
  print(f"Hello, {name}")
#greet_name("Subash")

def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"What is it like in {location}")

greet_with("Subash", "TVR")
greet_with(location = "LA", name = "Ariana" )
