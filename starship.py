import random
from datetime import datetime

random.seed(datetime.now().timestamp())


class Starship:

  def __init__(self):  # Constructor
    self.__hitPoint = 100 + (10 * random.randint(0, 5))
    # Hit point is 100 + random from 0 to 50
    self.__shieldStrength = 50 + (10 * random.randint(0, 5))
    self.__newlyCalled = True
    # Flag variable to indicate a battleship newly called should not act during its first turn.

  def getHp(self):
    return self.__hitPoint

  def getSs(self):
    return self.__shieldStrength

  def getNewlyCalled(self):
    return self.__newlyCalled

  def setNewlyCalled(self):
    self.__newlyCalled = False

  def takeDamage(self, damage):
    if damage <= self.__hitPoint:
      # If damage is smaller than or equal to its HP
      self.__hitPoint -= damage
    else:
      # If damage is bigger than its HP
      self.__hitPoint = 0

  def takeHealing(self, healing):
    self.__hitPoint += healing

  def callForSupport(self, list):
    num = len(list) - 1
    # We want to determine the number of existing battleships to distinguish among them.
    list.append(Battleship(num))

  def display(self):
    print(f"\tRemaining HP: {self.__hitPoint}")
    print(f"\tShield Strength: {self.__shieldStrength}")


class Battleship(Starship):

  def __init__(self, count):
    super().__init__()
    self.__attackPoint = 50 + (10 * random.randint(0, 5))
    self.__speed = 50 + (10 * random.randint(0, 5))
    self.__name = f"Battleship #{count}"
    # We want to distinguish battleship, medical or fortress since each object doesn't have an identifier. Each object is created as an element of a list.

  def getName(self):
    return self.__name

  def getAttackPoint(self):
    return self.__attackPoint

  def getSpeed(self):
    return self.__speed

  def beam(self):
    attack = self.getAttackPoint() * random.randint(1, 3)
    return attack

  def display(self):
    print(f"\t{self.__name}")
    super().display()
    print("\tAttack point:", self.__attackPoint)
    print("\tSpeed:", self.__speed)


class Medical(Starship):

  def __init__(self):
    super().__init__()
    self.__healingPower = 50 + (10 * random.randint(0, 5))
    self.__healingResource = 300
    self.__speed = 0
    self.__name = "Medical"

  def getName(self):
    return self.__name

  def getSpeed(self):
    return self.__speed

  def heal(self):
    healing = self.__healingPower
    if self.__healingResource == 0:
      print("Medical ran out of the healing resources!")
      return 0
    elif self.__healingResource >= healing:
      self.__healingResource -= healing
      return healing
    elif self.__healingResource < healing:
      healing = self.__healingResource
      self.__healingResource = 0
      return healing

  def display(self):
    print("\tMedical")
    super().display()
    print("\tHealing power:", self.__healingPower)
    print("\tHealing resource:", self.__healingResource)


class SpaceFortress:

  def __init__(self):
    self.__hitPoint = 1000
    self.__attackPoint = 120
    self.__speed = 75
    self.__name = "Space Fortress"
    self.__newlyCalled = True

  def getName(self):
    return self.__name

  def getHp(self):
    return self.__hitPoint

  def getNewlyCalled(self):
    return self.__newlyCalled

  def setNewlyCalled(self):
    self.__newlyCalled = False

  def takeDamage(self, damage):
    if damage <= self.__hitPoint:
      self.__hitPoint -= damage
    else:
      self.__hitPoint = 0

  def getSpeed(self):
    return self.__speed

  def beam(self):
    attack = self.__attackPoint + (10 * random.randint(0, 3))
    return attack

  def display(self):
    print("\tSpace fortress")
    print("\tRemaining HP:", self.__hitPoint)
    print("\tAttack point:", self.__attackPoint)
    print("\tSpeed:", self.__speed)
