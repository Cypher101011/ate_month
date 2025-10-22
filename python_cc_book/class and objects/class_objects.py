class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is a 5-star restaurant whose name is {self.restaurant_name} "
              f"\nand has cuisine {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open!")

# Create objects
restaurant = Restaurant('Lux', 'Bar')
restaurant1 = Restaurant('3Str', '3Star')
restaurant3 = Restaurant('Hell Kitchen', 'Devil Tear')

# Call methods
restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant3.describe_restaurant()

# Open one restaurant
restaurant.open_restaurant()
class User:
    def __init__(self, name, anime, gender, age, blood_group, skills):
        self.name = name
        self.anime = anime
        self.gender = gender
        self.age = age
        self.blood_group = blood_group
        self.skills = skills

    def describe_user(self):
        print(f"""
Character name : {self.name}
Anime          : {self.anime}
Age            : {self.age}
Gender         : {self.gender}
Ability/Skill  : {self.skills}
Blood Group    : {self.blood_group}
""")

    def greet_user(self):
        print(f"Hello {self.name} from anime {self.anime}!")

# Create object (6 values)
luffy = User(
    'Monkey D. Luffy',
    'One Piece',
    'Male',
    19,
    'B+',
    'Hito Hito no Mi: Model Nika'
)
luffy = User('Monkey D. Luffy', 'One Piece', 'Male', 19, 'B+', 'Hito Hito no Mi: Model Nika')
zoro = User('Roronoa Zoro', 'One Piece', 'Male', 21, 'XF', 'Three Sword Style, Haki')
sanji = User('Vinsmoke Sanji', 'One Piece', 'Male', 21, 'S', 'Diable Jambe, Black Leg Style')
naruto = User('Naruto Uzumaki', 'Naruto', 'Male', 17, 'B', 'Sage Mode, Rasengan')
mikasa = User('Mikasa Ackerman', 'Attack on Titan', 'Female', 19, 'O', 'ODM Gear Combat, Strength')

characters =[luffy,zoro,sanji,mikasa,naruto]
for character in characters:
    character.describe_user()
    character.greet_user
    print("-"*40)

# Call methods
# add method dynamitically-----------------------------
User.login_attempts=0
def increment_login_attempts(self):
    self.login_attempts+=1 
def reset_login_attempts(self):
    self.login_attempts=0 
User.increment_login_attempts=increment_login_attempts 
User.reset_login_attempts=reset_login_attempts

# attach methods to class
luffy.increment_login_attempts()
luffy.increment_login_attempts()
print(f"{luffy.name} login attempts:{luffy.login_attempts}")
luffy.reset_login_attempts()
print(f"{luffy.name} login attempts after reset : {luffy.login_attempts}")
