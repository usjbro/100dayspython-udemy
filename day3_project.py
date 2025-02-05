print("Welcome to Treasure Island\nYour mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go?\nType \"left\" or \"right\"\n")
lake = input("You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
print("You arrive at the island unharmed. There is a house with 3 doors.")
island = input("One red, one yellow and one blue.\nWhich color do you choose: red, yellow, blue?\n")
if island == "red":
    print("It's a room full of fire. Game Over")
    break