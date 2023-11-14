
# user = {
#     "name":'Alisher',
#     "age":40,
#     "children":3,
#     "dev":[
#         'React', 'python', 'js'
#     ]
# }


class User:
    
    def __init__(self, name, age, dev):
        self.name = name
        self.age = age
        self.dev = dev

    def say(self):
        print("Salom men {}".format(self.name))

# sardorbek = User('Sardorbek', 18, ['react', 'python', 'js'])

class Teacher(User):
    pass

muhiddin = Teacher('Muhiddin', 18, ['fulldev'])

muhiddin.say()