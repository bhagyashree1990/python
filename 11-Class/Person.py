class Person(object):

    # initialize
    def __init__(self, name, title, gender):
        self.name = name
        self.title = title
        self.gender = gender

    # display full name
    def display_name(self):
        return self.name + ' ' + self.title

    # display gender
    def isgender(self):
        return self.gender

    # change first name
    def change_first_name(self, new_name):
        self.name = new_name

    # change title
    def change_title(self, new_title):
        self.title = new_title

# object name "p"
p = Person('Rita', 'Roy', 'female')

# display full name
print(p.display_name())
print('='*50)

# display gender
print(p.isgender())
print('='*50)

# change first name
p.change_first_name('Amrita')

# change title
p.change_title('Ganguly')

# print full name
print(p.display_name())