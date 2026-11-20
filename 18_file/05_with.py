with open("harry.txt","r") as f:  # Context manager
    content = f.read()
    #There is no need to f.close the file 