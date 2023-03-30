def reverse_string(x):
  return x[::-1]



def reverseStringInFile():
    open("string.txt", "a") # Ñheck if there is such a file, if not, then create

    with open("string.txt", "r") as file_read:
        with open("output.txt", "w") as file_write:
            file_write.write(reverse_string(file_read.read())) 
