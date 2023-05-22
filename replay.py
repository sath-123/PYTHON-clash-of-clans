import json

with open("replay.json", "r+") as file:

    data = json.load(file)

    file.seek(0)

    file.close()

x=data["games"]

game_number=int(input())
if(game_number<=len(x)):
    for j in x[game_number]:
        print('\033[H'+j)
else:
    print("That attack is not available")