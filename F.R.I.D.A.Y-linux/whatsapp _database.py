import pickle
#creating a dictionary of contacts
contacts = {
            'name':'xxxxxxxxxx',
            'name2':'xxxxxxxxxx'
            
                        }

with open("first_pickle.pickle","wb") as file:
	pickle.dump(contacts,file)
'''
with open("first_pickle.pickle","rb") as file:
	data = pickle.load(file)
	num = data["name"]
print(data)
print(num)	
'''

