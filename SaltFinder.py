SALT_MODIFIER = 23
rng_table = [
    7, 182, 240, 31, 85, 91, 55, 227, 174, 79, 178, 94, 153, 246, 119, 203,
    96, 143, 67, 62, 167, 76, 45, 136, 199, 104, 215, 209, 194, 242, 193, 221,
    170, 147, 22, 247, 38, 4, 54, 161, 70, 78, 86, 190, 108, 110, 128, 213,
    181, 142, 164, 158, 231, 202, 206, 33, 255, 15, 212, 140, 230, 211, 152, 71,
    244, 13, 21, 237, 196, 228, 53, 120, 186, 218, 39, 97, 171, 185, 195, 125,
    133, 252, 149, 107, 48, 173, 134, 0, 141, 205, 126, 159, 229, 239, 219, 89,
    235, 5, 20, 201, 36, 44, 160, 60, 68, 105, 64, 113, 100, 58, 116, 124,
    132, 19, 148, 156, 150, 172, 180, 188, 3, 222, 84, 220, 197, 216, 12, 183,
    37, 11, 1, 28, 35, 43, 51, 59, 151, 27, 98, 47, 176, 224, 115, 204,
    2, 74, 254, 155, 163, 109, 25, 56, 117, 189, 102, 135, 63, 175, 243, 251,
    131, 10, 18, 26, 34, 83, 144, 207, 122, 139, 82, 90, 73, 106, 114, 40,
    88, 138, 191, 14, 6, 162, 253, 250, 65, 101, 210, 77, 226, 92, 29, 69,
    30, 9, 17, 179, 95, 41, 121, 57, 46, 42, 81, 217, 93, 166, 234, 49,
    129, 137, 16, 103, 245, 169, 66, 130, 112, 157, 146, 87, 225, 61, 241, 249,
    238, 8, 145, 24, 32, 177, 165, 187, 198, 72, 80, 154, 214, 127, 123, 233,
    118, 223, 50, 111, 52, 168, 208, 184, 99, 200, 192, 236, 75, 232, 23, 248
]

possible_seeds = list(range(256))
battle_counter = 0

print("Commands:")
print("")
print("salts - List the current set of possible salt")
print("reset - Reset the program to the beginning")
print("1 - Encountered four Gabbledegaks")
print("2 - Encountered a Harvester and two Gabbledegaks")
print("3 - Encountered a Hadesgigas")
print("4 - Encountered a Hadesgigas and a Harvester")

def reset():
    global possible_seeds
    global battle_counter
    
    print("Resetting")
    possible_seeds = list(range(256))
    battle_counter = 0
    
def narrow_seeds(rng_start, rng_end):
    global possible_seeds
    global battle_counter
    
    new_seeds = possible_seeds.copy()
    battle_counter += 1
    
    for seed in possible_seeds:
        index = (seed + battle_counter) % 256
        random_number = rng_table[index]
        
        salt = seed
        if (seed + battle_counter) / 256 >= 1:
            salt += SALT_MODIFIER
        salted_random_number = (random_number + salt) % 256
        
        if salted_random_number < rng_start or salted_random_number >= rng_end:
            new_seeds.remove(seed)
            
    possible_seeds = new_seeds

while(True):
    print("")
    print("Enter a command")
    
    command = input()
    
    if command == "reset":
        reset()
    elif command == "salts":
        print(possible_seeds)
    elif command == "1":
        narrow_seeds(0, 80)
    elif command == "2":
        narrow_seeds(80, 160)
    elif command == "3":
        narrow_seeds(160, 240)
    elif command == "4":
        narrow_seeds(240, 256)
    else:
        print("Invalid command")
        
    if len(possible_seeds) == 1:
        print("Your salt is " + str(possible_seeds[0]))
        reset()
    elif len(possible_seeds) == 0:
        print("No salts are possible (did you make a mistake?)")
        reset()