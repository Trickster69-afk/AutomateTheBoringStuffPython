def main():
    file1 = "foo.txt"
    file2 = "bar.txt"
    output = "result.txt"
    combine_two_text_files(file1, file2, output)

def combine_two_text_files(file1, file2, output):

    with open(output, "w") as file:
        with open(file1, "r") as f: #write contents of file1
            for i in f:
                file.write(i)
        file.write("\n")
        with open(file2, "r") as f: #write contents of file 2
            for i in f:
                file.write(i)

if __name__ == "__main__":
    main()