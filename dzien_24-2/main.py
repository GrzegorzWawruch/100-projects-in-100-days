# file = open("my_file.txt")
# contents = file.read()
# print(contents)

with open("my_file.txt", mode = "r+w") as file:
    content = file.read()
    file.write("New text")
    print(content)



file.close()