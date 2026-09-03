import qrcode 

url = input("Enter the url: ")
filename = input("Enter the filename to  save: ")

if not (filename.endswith(" .png")):
    filename = filename + " .png"

img = qrcode.make(url)
img.save(filename)
