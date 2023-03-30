import FileStringReverse  as fileStrRev

def ReadFile(fileName):
    with open(fileName, "r") as reader:
        print(reader.read() + "\n")

ReadFile("string.txt")

with open ("string.txt", "a") as fileWriter:    
    fileWriter.write("\nMy name is Tom")

fileStrRev.reverseStringInFile()
    
ReadFile("string.txt")

