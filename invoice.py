import pyttsx4
import PyPDF2

pdf = PyPDF2.PdfReader("./Mahabharat.pdf")
engine = pyttsx4.init()
voices = engine.getProperty('voices')
female_voice = [v for v in voices if "female" in v.name.lower()]
if female_voice:
    engine.setProperty('voice', female_voice[0].id)
else:
    print("No female voices found. Using the default voice.")
pdf_read = pdf.pages[2]
text = pdf_read.extract_text()
# pyttsx4.engine.Engine.setProperty(self=engine, name=pyttsx4.voice, value="female")
# pyttsx4.voice.Voice(id, gender="female")
engine.say(text=text)
engine.runAndWait()
