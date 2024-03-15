dictionary = {"name": "Subash",
              "age": 21,
              "location": "tnk"}
empty_dict = {}
print(dictionary["name"])
print(dictionary["location"])

dictionary["age"] = 20
print(dictionary["age"])

for key in dictionary:
    print(f"{key} : {dictionary[key]}")


#Nested Dictionary
    
travel_log = {"France" : ["Paris", "Djorn", "Lillie"],
              "India" : {"Visited" : ["Chennai", "Trichy"] }
              }

