from starship import *

ships = []
# We want to create as many battleship objects as possible. To make the program easy to handle, we add a new object to a list.
ships.append(Battleship(1))
ships.append(Medical())
ships.append(SpaceFortress())


def main():

  print(
      "Finally, you have made it to the enemy's space fortress!\nYour final mission is to destroy the fortress.\n"
  )

  input("Press enter to continue... ")

  print(
      "\nYou, a battleship #1, are accompanied by a medical ship.\nEach turn, each ship can choose a command:\n"
  )

  print("\tBattleship: beam\n\tGives a damage to the fortress\n")
  print(
      "\tMedical: heal\n\tHeals one battleship or the medical itself up to remaining healing resource\n"
  )
  print("\tBoth: call for support\n\tCalls one additional battleship for help")

  print(
      "\n\tSpace fortress: beam\n\tDeals damage to all battleships and the medical\n"
  )

  input("Press enter to continue... ")

  print("\nHere are the data of your battleship, medical, and the fortress:\n")
  for ship in ships:
    ship.display()
    print("")

  print(
      "\nWhen the HP of the fortress reaches 0, the mission is completed!\nIf all battleships are defeated, it's game over.\nOne more thing: the battleships and fortress move in the order of their speed, with the medical always moving at last."
  )

  input("\nPress Enter to start! ")

  end = False # Flag variable to terminate the while loop.
  turnCount = 1 # We want to count the turns.

  while not end:
    print(f"\nTurn #{turnCount}")
    ships.sort(key=lambda x: x.getSpeed(), reverse=True)
    # Because each ship moves in the order of their speed, we want to sort the list of ships based on their speed attribute. And we simply iterate the list.

    print("\n[Current status]")
    for ship in ships:
      ship.display()
      print("")
      if ship.getNewlyCalled():
        ship.setNewlyCalled()
        # This method sets the flag variable indicating whether a battleship is newly called or not. This should be set as False.

    indexFortress = findFortress(ships)
    fortressObj = ships[indexFortress]
    # For further use, we want to specify where the fortress is in the list.

    for ship in ships:
      input("\nPress enter ") # We want a pause, proceeding the game.
      if fortressObj.getHp() != 0:
        # If the HP of the fortress reaches 0, no need to iterate any more. Actually the program iterates even after the HP reaches 0, but we don't want a command anymore.
        if ship.getNewlyCalled():
          # If the battleship is newly called, it should not act at that turn.
          pass
        elif ship.getHp() != 0: # If the ship is still alive
          chooseCommand(ship, fortressObj) # We need this specified fortress object
          if fortressObj.getHp() == 0:
            print(
                "\nCongratulations! You destroyed the space fortress and completed the mission. Well done!"
            )
            end = True # Terminates the while loop

        elif ship.getHp() == 0:
          print(f"\n{ship.getName()} can't do anything!")

    dead = 0
    # This for loop wants to check whether all battleships are dead or not. If so, we need to terminate the while loop.
    for ship in ships:
      if (ship.getName()[0] == "B") and (ship.getHp() == 0):
        dead += 1
    if dead == (len(ships) - 2): # This "-2" means fortress and medical. We want the number of the battleships in the list, dead or alive. If the counter of "dead" is identical with the number of the battleships in the list, that means all the battleships are dead, which is game over.
      print("\nOh no! Your team has been defeated..")
      end = True # Terminates the while loop

    turnCount += 1


def findFortress(ships):
  for i, ship in enumerate(ships):
    if ship.getName()[0] == "S": # Accesses to the name attribute of the class object and if the first letter of the name is "S", that means that object is SpaceFortress.
      return i # We want the index of the fortress in the list to specify where the fortress is.


def chooseCommand(ship, fortressObj):
  if ship.getName()[0] == "B": # If the first letter of the name attribute is "B", that object is "Battleship"
    print(f"\nWhat does {ship.getName()} do?")
    print("\n1: Beam\n2: Call for support")
    command = input("\nType the number: ") # No input validation here...
    if command == "1":
      bAttack = ship.beam()
      print(
          f"\n{ship.getName()} fired a beam! {bAttack} damage dealt to the fortress!"
      )
      fortressObj.takeDamage(bAttack)
      print(f"Remaining HP of the fortress: {fortressObj.getHp()}")
    elif command == "2":
      print(f"\n{ship.getName()} called for a support!")
      ship.callForSupport(ships) # We want to append a new Battleship object to the list ships, which is passes by reference (=The value is even changed after the function call.)
      print(f"{ships[-1].getName()} joined the team!")
      # We don't know the identifier of the newly added battleship, but we append it to the end of the list, so it should be at the end of the list [-1].

  elif ship.getName()[0] == "S": # If the object is "SpaceFortress"
    fAttack = fortressObj.beam()
    print(f"\nSpace fortress fired a beam! {fAttack}!")
    for ship in ships:
      if (ship.getName()[0] != "S") and (ship.getHp() != 0):
        # We want to give a damage to "Battleships" and "Medical", so if the ship object is NOT "SpaceFortress". And we don't need to give a damage to a ship which is already dead. 
        fDamage = fAttack - ship.getSs()
        # We need to reduce the damage by the shield strength point
        ship.takeDamage(fDamage)
        print(
            f"{fDamage} damage dealt to {ship.getName()}! Remaining HP: {ship.getHp()}"
        )

  elif ship.getName()[0] == "M": # If the ship object is "Medical"
    print(f"\nWhat does {ship.getName()} do?")
    print("\n1: Heal\n2: Call for support")
    command = input("\nType the number: ") # No input validation here...
    if command == "1":
      healing = ship.heal()
      print("\nWhich ship to heal?\n")
      for i, ship in enumerate(ships):
        # We need this index variable by enumerate() function to specify which ship to heal.
        if ((ship.getName()[0] == "B") and (ship.getHp() != 0)):
          print(f"{i}: {ship.getName()} Remaining HP: {ship.getHp()}")
        elif ((ship.getName()[0] == "M") and (ship.getHp() != 0)):
          print(f"{i}: {ship.getName()} Remaining HP: {ship.getHp()}")
      index = int(input("\nType the index # (before the colon): ")) # Index is the index variable generated by enumerate() function. User can specify a ship to be healed by choosing the index. No input validation here...
      ships[index].takeHealing(healing)
      print(
          f"\n{ships[index].getName()} was healed for {healing} points! Remaining HP: {ships[index].getHp()}"
      )

    elif command == "2":
      print(f"\n{ship.getName()} called for a support!")
      ship.callForSupport(ships)
      print(f"{ships[-1].getName()} joined the team!")


if __name__ == "__main__":
  main()
