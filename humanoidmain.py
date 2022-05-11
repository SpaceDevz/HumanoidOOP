import random

global id
id = []

class Human():
  def __init__(self, name=None, age=None, hair_style=None, id=None):
    self.name = name
    self.age = age
    self.hair_style = hair_style
    self.id = id

  def createHumanoid(self):
    ##      HUMANOID CREATION PROCESS       ##
    ## 1. Get Name (User Input)             ##
    ## 2. Get Age (Randomly Generated)      ##
    ## 3. Get Hair Stlye (Random List Pick) ##

    self.name = input("Whats the name of the humanoid? ")
    if self.name == "":
      raise Exception("Please pass in a valid name.")
    
    hair_list = ['Curly', 'Straight', 'Wave', 'Bald']
    self.age = random.randint(1,110)
    self.hair_style = hair_list[random.randint(range(len(hair_list)-1)[0], range(len(hair_list)-1)[1])]
    try:
      id.append(id[-1]+1)
    except IndexError:
      id.append(1)

    try:
      print('Humanoid:')
      print('Name: ',object.name)
      print('Age: ',object.age)
      print('Hair: ',object.hair_style)
      print('ID: ',id[-1])
    except NameError:
      raise Exception('Unexpected Humanoid Creation Error: Failed to generate humanoid specs.')


object = Human()
object.createHumanoid()

