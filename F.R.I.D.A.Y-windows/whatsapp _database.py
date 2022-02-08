import pickle
#creating a dictionary of contacts
contacts = {
            'name_1':'xxxxxxxxxx',
            'name_2':'xxxxxxxxx'
            }

with open("first_pickle.pickle","wb") as file:
	pickle.dump(contacts,file)
'''	
with open("first_pickle.pickle","rb") as file:
	data = pickle.load(file)
	num = data["name_1"]
print(data)
print(num)	
'''

