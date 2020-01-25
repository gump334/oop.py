#OOP learning
#created a character class
class PlayerCharacter:
  #Class Object Attribute
  membership = True
  def __init__(self, name='anonymous', age=0):
    if (age > 8):
      self.name = name #attributes
      self.age = age

  def shout(self):
    print(f'My name is {self.name}')

  @classmethod
  def adding_things(cls, num1,num2):
    return num1 + num2

  @staticmethod
  def adding_things2(num1, num2):
    return  num1 + num2

    

player1 = PlayerCharacter('Terrell', 36)
#player2 = PlayerCharacter('Amy', 30)
print(player1.shout(), player1.age)
#print(player2.shout(), player2.age)
print(player1.membership)

print(player1.adding_things(5,5))


