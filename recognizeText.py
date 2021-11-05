try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# List of available languages
print(pytesseract.get_languages(config=''))

def recognizeText(filename):
    # Convert image to string
    text = pytesseract.image_to_string(Image.open(filename))
    return text

result = recognizeText('img.png')
print("\n", result)

file = open("textResult.txt", "w")
file.write(result)
file.close()
print("Successfully Completed")