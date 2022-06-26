# Making Character object for pokemon characters
class Character:
    name = "" # Their name
    hp = 50 # Their initial health
    attack_pow = 20 # Their initial attack power
    type = ["fire", "water", "grass"] # List of available attack types

# Fire Type
Charmander = Character()
Charmander.type = Character.type[0]
Charmander.name = "Charmander"
Cyndaquil = Character()
Cyndaquil.type = Character.type[0]
Cyndaquil.name = "Cyndaquil"
# Water Type
Squirtle = Character()
Squirtle.type = Character.type[1]
Squirtle.name = "Squirtle"
Totodile = Character()
Totodile.type = Character.type[1]
Totodile.name = "Totodile"
# Grass Type
Bulbasaur = Character()
Bulbasaur.type = Character.type[2]
Bulbasaur.name = "Bulbasaur"
Chikorita = Character()
Chikorita.type = Character.type[2]
Chikorita.name = "Chikorita"

# We take input from ash and gary, and store them in variables
ash_input = input("You Choose: ")
gary_input = input("Gary Chooses: ")

ash_type = []
gary_type = []

# Declaring variables based on Ash's input
if ash_input == "Charmander":
    ash_type = Character.type[0]
    choose_character_ash = Charmander
elif ash_input == "Cyndaquil":
    ash_type = Character.type[0]
    choose_character_ash = Cyndaquil
elif ash_input == "Squirtle":
    ash_type = Character.type[1]
    choose_character_ash = Squirtle
elif ash_input == "Totodile":
    ash_type = Character.type[1]
    choose_character_ash = Totodile
elif ash_input == "Bulbasaur":
    ash_type = Character.type[2]
    choose_character_ash = Bulbasaur
elif ash_input == "Chikorita":
    ash_type = Character.type[2]
    choose_character_ash = Chikorita

# Declaring variables based on Gary's input
if gary_input == "Charmander":
    gary_type = Character.type[0]
    choose_character_gary = Charmander
elif gary_input == "Cyndaquil":
    gary_type = Character.type[0]
    choose_character_gary = Cyndaquil
elif gary_input == "Squirtle":
    gary_type = Character.type[1]
    choose_character_gary = Squirtle
elif gary_input == "Totodile":
    gary_type = Character.type[1]
    choose_character_gary = Totodile
elif gary_input == "Bulbasaur":
    gary_type = Character.type[2]
    choose_character_gary = Bulbasaur
elif gary_input == "Chikorita":
    gary_type = Character.type[2]
    choose_character_gary = Chikorita

# Character.type[0] means fire, Character.type[1] means water, Character.type[2] means grass.

if ash_type == Character.type[0] and gary_type == Character.type[0]: # fire v fire
    type_affinity1_ash = 1
    type_affinity2_gary = 1
elif ash_type == Character.type[1] and gary_type == Character.type[1]: # water v water
    type_affinity1_ash = 1
    type_affinity2_gary = 1
elif ash_type == Character.type[2] and gary_type == Character.type[2]: # grass vs grass
    type_affinity1_ash = 1
    type_affinity2_gary = 1

# We compare two types and their vice versa

if ash_type == Character.type[0] and gary_type == Character.type[1]: # fire weaker against water
    type_affinity1_ash = 0.5
    type_affinity2_gary = 2
elif ash_type == Character.type[1] and gary_type == Character.type[0]: # water stronger against fire
    type_affinity1_ash = 2
    type_affinity2_gary = 0.5
elif ash_type == Character.type[0] and gary_type == Character.type[2]: # fire stronger against grass
    type_affinity1_ash = 2
    type_affinity2_gary = 0.5
elif ash_type == Character.type[2] and gary_type == Character.type[0]: # grass weaker against fire
    type_affinity1_ash = 0.5
    type_affinity2_gary = 2
elif ash_type == Character.type[1] and gary_type == Character.type[2]: # water weaker against grass
    type_affinity1_ash = 0.5
    type_affinity2_gary = 2
elif ash_type == Character.type[2] and gary_type == Character.type[1]: # grass stronger against water
    type_affinity1_ash = 2
    type_affinity2_gary = 0.5

# For updating fight turns
turn = 0

remaining_hp1 = choose_character_ash.hp
remaining_hp2 = choose_character_gary.hp

while True:
    # Updating turn and printing it
    turn += 1
    print("===", "Turn", turn, "===")

    # Remaining hp = previous hp – attack power * type affinity
    remaining_hp1 = remaining_hp1 - (choose_character_gary.attack_pow * type_affinity2_gary)
    remaining_hp2 = remaining_hp2 - (choose_character_ash.attack_pow * type_affinity1_ash)

    # If any of their hp goes down below 0 (like -10, -30)
    if remaining_hp1 < 0:
        remaining_hp1 = 0
    if remaining_hp2 < 0:
        remaining_hp2 = 0

    # Printing character name and hp
    print(choose_character_ash.name, "has", int(remaining_hp1), "hp left")
    print(choose_character_gary.name, "has", int(remaining_hp2), "hp left")

    # Game end logic
    if remaining_hp1 <= 0 or remaining_hp2 <= 0:
        if remaining_hp1 > remaining_hp2:
            print(choose_character_ash.name, "and Ash Wins!")
        elif remaining_hp1 < remaining_hp2:
            print(choose_character_gary.name, "and Gary Wins!")
        else:
            print("It's a tie!")
        break
