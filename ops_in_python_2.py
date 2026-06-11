# practice code for OOPs in python
# self 

class fbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.menu("exit")
    def menu(self,user_input):
        if user_input == 'exit':
            user_input = input("""Enter your choice:
                           1. signup
                           2. login
                           3. post 
                           """)
        if user_input == 'signup':
            user_input = input("""Enter your choice:
                           3. post 
                           """)
        if user_input == '1':
            self.signup()
           
            print("input is here")
            
        if user_input == '3':
            self.makePost()
        
        return user_input 
    
    def signup(self):
        username = input("enter username :")
        password = input("enter password:")
        self.username = username
        self.password = password
        self.menu("signup")
        
    def makePost(self):
        post = input("enter your post :")
        
        print ("post created")
        self.postMenu(post)
        
        
    def postMenu(self,post):
        posts = []
        posts.append(post)
        print(posts)
        self.makePost()
        

obj = fbook()

print("username ==",obj.username)
print("pasword ==",obj.password)