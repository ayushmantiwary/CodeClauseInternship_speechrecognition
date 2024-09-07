import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
with sr.Microphone() as source:
    print("Talk")
    try:
        audio_text = r.listen(source, timeout=5)  # record audio for 5 seconds
        print("Time over, thanks")
        
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except sr.UnknownValueError:
            print("Sorry, I did not understand what you said")
        except sr.RequestError:
            print("Error requesting results from Google Speech Recognition")
    except sr.WaitTimeoutError:
        print("Timeout: No audio input received")