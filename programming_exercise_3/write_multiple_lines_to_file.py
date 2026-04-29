def write_lines():
    output_file = open("mylife.txt", "w")

    continue_input = "y"

    while continue_input == "y":
        user_line = input("Enter line: ")
        output_file.write(user_line + "\n")

        continue_input = input("Are there more lines y/n? ")

    output_file.close()


write_lines()