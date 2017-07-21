class User:
    # Define the fields and methods for your object here.
    def __init__(self, user_name, password):
    	self.user_name = user_name #attribute
    	self.password= password
    	self.connections = []

    def getUserName(self):
    	return self.user_name	

    def getConnections(self):
    	return self.connections

    def addConnection(self, connection_id):
    	self.connections.append(connection_id)


class Network:
    # Define the fields and methods for your object here.
    def __init__ (self):
    	self.user=[]

    def adduser(self, username, password):
    	#create new user
    	#and password
    	#append that user in the list
    	myUser= User(username, password)
    	self.user.append(myUser)
    	print("User added!")



def main():
    # Define the program flow for your user interface here.
 	myNetwork = Network() 
 	myNetwork.adduser("jody","me")
 	response= input ("Add user_name:")
 	store(input)
 	

    
# Runs your program.
if __name__ == '__main__':
    main()
