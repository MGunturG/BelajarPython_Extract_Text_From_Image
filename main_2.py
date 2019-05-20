from PIL import Image
import pytesseract

//membuat file output berupa text
outputFile = open("output.txt","w+")

//User memasukan nama file gambar
fileName = raw_input('Enter image file name:')

im = Image.open(fileName)
text = pytesseract.image_to_string(im, lang="eng");
print(text)

//proses membuat text file hasil ekstrak
outputFile.write(text)
outputFile.close()

print("Text extracted! Check output.txt file.")