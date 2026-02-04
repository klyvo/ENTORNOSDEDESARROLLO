class User:
    def __init__(self,username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom

#us1=User(username="ama",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor")
#print(us1)
users = [
    User(username="rob",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor"),
    User(username="john",nom="John Cannigan",password="12345", email="john@gmail.com",rol="tutor"),
    User(username="maria",nom="Maria Sams",password="12345", email="maria@gmail.com",rol="admin")
]


class UserDao:
    def __init__(self):
        self.users=users
    
    def getUserByUsername(self,uname):
        user = None
        for u in self.users:
            if u.username == uname:
                user = u.__dict__
        return user
    
    def addUser(self,u):
       self.users.append(u)
       return u
    
    def getAllUsers(self):
        return [user.__dict__ for user in self.users]
        #return self.users
# Test DAO
'''
user_dao = UserDao()
a=user_dao.getAllUsers()
print(a)
response=user_dao.getUserByUsername("maria")
print(response)
response=user_dao.getUserByUsername("AAAA")
print(response)'''
# End TEST