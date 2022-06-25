# Making Character object for pokemon characters
class Character:
    name = "" # Their name
    hp = 50 # Their initial health
    attack_pow = 20 # Their initial attack power
    type = ["fire", "water", "grass"] # Array of available attack types

# Fire Type
Charmander = Character()
Charmander.type = Character.type[0]
Charmander.name = Character.name = "Charmander"
Cyndaquil = Character()
Cyndaquil.type = Character.type[0]
Cyndaquil.name = Character.name = "Cyndaquil"
# Water Type
Squirtle = Character()
Squirtle.type = Character.type[1]
Squirtle.name = Character.name = "Squirtle"
Totodile = Character()
Totodile.type = Character.type[1]
Totodile.name = Character.name = "Totodile"
# Grass Type
Bulbasaur = Character()
Bulbasaur.type = Character.type[2]
Bulbasaur.name = Character.name = "Bulbasaur"
Chikorita = Character()
Chikorita.type = Character.type[2]
Chikorita.name = Character.name = "Chikorita"

# Character.type[0] means fire, Character.type[1] means water, Character.type[2] means grass.

ash_type = ""
gary_type = ""

type_affinity1 = 0
type_affinity2 = 0

ash_input = input("You Choose: ")
gary_input = input("Gary Chooses: ")

choose_character_ash = Character()
choose_character_gary = Character()

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

# 0 = fire, 1 = water, 2 = grass
if ash_type == Character.type[0] and gary_type == Character.type[0]: # making equal affinity for same types. (fire vs fire, water vs water, grass vs grass)
    type_affinity1 = 1
    type_affinity2 = 1
elif ash_type == Character.type[1] and gary_type == Character.type[1]:
    type_affinity1 = 1
    type_affinity2 = 1
elif ash_type == Character.type[2] and gary_type == Character.type[2]:
    type_affinity1 = 1
    type_affinity2 = 1

if ash_type == Character.type[0] and gary_type == Character.type[1]: # fire weaker against water
    type_affinity1 = 0.5
    type_affinity2 = 2
elif ash_type == Character.type[1] and gary_type == Character.type[0]: # water stronger against fire
    type_affinity1 = 2
    type_affinity2 = 0.5
elif ash_type == Character.type[0] and gary_type == Character.type[2]: # fire stronger against grass
    type_affinity1 = 2
    type_affinity2 = 0.5
elif ash_type == Character.type[1] and gary_type == Character.type[2]: # water weaker against grass
    type_affinity1 = 0.5
    type_affinity2 = 2
elif ash_type == Character.type[2] and gary_type == Character.type[1]: # grass stronger against water
    type_affinity1 = 2
    type_affinity2 = 0.5
elif ash_type == Character.type[2] and gary_type == Character.type[0]: # grass weaker against fire
    type_affinity1 = 0.5
    type_affinity2 = 2

turn = 0 # Game turn
remaining_hp1 = choose_character_ash.hp # Health of the character choosen by Ash
remaining_hp2 = choose_character_gary.hp # Health of the character choosen by Gary

# Main game loop
while True:
    # Incrementing turns
    turn += 1
    print("===", "Turn", turn,"===")
    
    # Remaining hp = previous hp – attack power * type affinity
    remaining_hp1 = remaining_hp1 - (choose_character_gary.attack_pow * type_affinity2)
    remaining_hp2 = remaining_hp2 - (choose_character_ash.attack_pow * type_affinity1)
    if remaining_hp1 < 0:
        remaining_hp1 = 0
    if remaining_hp2 < 0:
        remaining_hp2 = 0
    print(choose_character_ash.name, "has", int(remaining_hp1), "hp left")
    print(choose_character_gary.name, "has", int(remaining_hp2), "hp left")
    
    # Loop break logic
    if remaining_hp1 <= 0 or remaining_hp2 <= 0:
        if remaining_hp1 > remaining_hp2:
            print(choose_character_ash.name, "and Ash Wins!")
        elif remaining_hp1 < remaining_hp2:
            print(choose_character_gary.name, "and Gary Wins!")
        else:
            print("It's a tie!")
        break

# The end!
