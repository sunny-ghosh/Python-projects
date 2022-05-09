# This is the solution of sample program no.- 3 (see: no.5, 6, 7 & 8 in practice list)
'''This program is the application of chapter no.- 5.
It's under the basic python lessions.'''
empty_set = set()                        # It's used to create empty set.
print(type(empty_set))
empty_dict = {}                          # It's used to create empty dictionary.
print(type(empty_dict))
n1 = input("Enter your favourite programming language : ")
n2 = input("Enter your favourite programming language : ")
n3 = input("Enter your favourite programming language : ")
n4 = input("Enter your favourite programming language : ")
n5 = input("Enter your favourite programming language : ")
n6 = input("Enter your favourite programming language : ")
n7 = input("Enter your favourite programming language : ")
n8 = input("Enter your favourite programming language : ")
empty_dict["Sunny"] = n1             # It's used to take values of the specified keys.
empty_dict["Biprojit"] = n2
empty_dict["Bidusha"] = n3
empty_dict["Jayashree"] = n4
empty_dict["Chayan"] = n5
empty_dict["Sourish"] = n6
empty_dict["Dibyendu"] = n7
empty_dict["Jayashree"] = n8      # Here, the key "Jayashree" has been repeated in the dictionary twice, that's why the latest given value will be taken as the value of this key.
print(empty_dict)
print(empty_dict.items())           # It's a method of dictionary which returns a list of all contents in ('key','value') tuples format.


'''In dictionary, the values of keys can be same but the keys must be unique.'''