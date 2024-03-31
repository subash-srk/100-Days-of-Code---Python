# list = [i * 2 for i in range(1,5)]
# list
# [2, 4, 6, 8]
# names = ["Subash", "Ariana", "Abel", "Dua", "Elanor"]
# shrt_names = [name for name in names if len(name) < 5]
# shrt_names
# ['Abel', 'Dua']
# upper_names = [name.upper() for name in names]
# upper_names
# ['SUBASH', 'ARIANA', 'ABEL', 'DUA', 'ELANOR']
# long_names = [name.upper() for name in names if len(name) > 5]
# long_names
# ['SUBASH', 'ARIANA', 'ELANOR']


student_dict = {
    "student": ["Ariana, Abel", "Subash"],
    "score" : [56, 76, 91]
}


import pandas


student_df = pandas.DataFrame(student_dict)
print(student_df)
