with open("sample.txt" , "w") as file:
    file.write("welcome to my file. \n")
    file.write("This is the first line \n")
    file.write("somethig going wrong! \n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
    print("File content: \n", content)
#second (read single line)
with open("sample.txt" , "w") as file:
    file.write("welcome to my file. \n")
    file.write("This is the first line \n")
    file.write("somethig going wrong! \n")

with open("sample.txt", "r") as file:
    content = file.readline()
    print(content)
    print("File content: \n", content)

#third(overwrite )
with open("sample.txt" , "w") as file:
    file.write("Hello, this is the new content. \n")
    file.write("This is the first line \n")
    file.write("somethig going wrong! \n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
    print("File content: \n", content)

#fourth(append new line)
with open("sample.txt", "a") as file:
    file.write("\n appending a new line")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content: \n", content)

#fifth
with open("sample.txt" , "w+") as file:
    file.write("welcome to my file. \n")
    file.seek(0)   #go back to the start
    content = file.read()
    print("After writing:\n" , content)