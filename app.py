import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 5 seconds")
    recorded_audio = recognizer.listen(source, timeout=5)
    print("Done recording")

try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )

    print("Decoded Text : {}".format(text))

except Exception as ex:

    print(ex)


sr.Microphone.list_microphone_names()