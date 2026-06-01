def main():
    c = 0
    with open("zigzag.txt", "w") as file:
        for i in range(71):
            for i in range(1, 8): #zig
                file.write(" " * c + "*" * 8)
                file.write("\n")
                c += 1

            for i in range(1, 8): #zag
                file.write(" " * c + "*" * 8)
                file.write("\n")
                c -= 1

if __name__ == "__main__":
    main()