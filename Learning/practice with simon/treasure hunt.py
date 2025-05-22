import random

def treasure_hunt():
    locations = {
        "Forest": ("old tree", "hidden cave", "deep ravine"),
        "Desert": ("sand dune", "abandoned oasis", "ancient ruins"),
        "Mountain": ("snowy peak", "rocky ledge", "secret tunnel")
    }

    treasure_map = {
        ("old tree", "red"): "Forest",
        ("sand dune", "blue"): "Desert",
        ("snowy peak", "green"): "Mountain",
        ("hidden cave", "silver"): "Treasure!",
        ("abandoned oasis", "gold"): "Treasure!",
        ("secret tunnel", "diamond"): "Treasure!"
    }

    items = ["red cloth", "blue gem", "green feather", "silver coin", "gold nugget", "diamond ring"]
    backpack = []

    location = random.choice(list(locations.keys()))
    print("Welcome to the Treasure Hunt! You're starting in the", location)

    while True:
        landmark = random.choice(locations[location])
        print("You see a", landmark)

        item = random.choice(items)
        print("You found a", item)
        backpack.append(item)

        clue = (landmark, item.split()[-1])
        if clue in treasure_map:
            destination = treasure_map[clue]
            if destination == "Treasure!":
                print("Congratulations! You found the treasure!")
                break
            else:
                print("The clue leads you to the", destination)
                location = destination
        else:
            print("This doesn't seem to be a helpful clue...")

if __name__ == "__main__":
    treasure_hunt()