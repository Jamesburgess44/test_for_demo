

taco_meat_options = ["Steak","Chicken","Pork","Shrimp","Veggie"]

def list_maker(list):
    string_list_format = ""
    for item in list:
        string_list_format += " " + item
    return string_list_format

string_list = list_maker(taco_meat_options)
print(string_list) 








