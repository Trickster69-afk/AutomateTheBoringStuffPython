def main():
    list_dir = [] #list of directions
    while True:
        directions = input().strip().lower()
        if directions == "": 
            break
        elif directions not in ["n", "s", "e", "w"]:
            print("Please enter directions(N, S, E, W): ")
            continue
        else:
            list_dir.append(directions)

    print(get_end_coordinates_directions(list_dir))


def get_end_coordinates_directions(dir):
    x = 0
    y = 0
    for i in dir:
        if i == "n": 
            y += 1
        elif i == "s":
            y -= 1
        elif i == "e":
            x += 1
        elif i == "w":
            x -= 1
    return [x, y] #returns a list of coordinates

if __name__ == "__main__":
    main()