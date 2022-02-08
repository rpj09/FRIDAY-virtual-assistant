import pickle
#creating a dictionary of contacts
contacts = {
            'email':'xxx@gmail.com',
            'password':'abc',
            'administrator':'xxx@gmail.com',
            'admin':'xxx@gmail.com',

            }

with open("mail.pickle","wb") as file:
	pickle.dump(contacts,file)
	
with open("mail.pickle","rb") as file:
	data = pickle.load(file)
	num = data["email"]
print(data)
print(num)	


