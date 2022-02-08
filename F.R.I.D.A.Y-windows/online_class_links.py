import pickle
#creating a dictionary of contacts
contacts = {
            'maths':'https://meet.google.com/civ-fguz-yxf',
            'computer':'https://meet.google.com/fdc-kwgv-iwn',
            'chemistry':'https://meet.google.com/aka-oieo-eyp',
            'physics':'https://meet.google.com/wke-okmd-wye',
            }

with open("online_class_links.dat","wb") as file:
	pickle.dump(contacts,file)
	
with open("online_class_links.dat","rb") as file:
	data = pickle.load(file)
	num = data["computer"]
print(data)
print(num)	


