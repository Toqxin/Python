import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import sys
import virtualData
import pyautogui
import time

engine = pyttsx3.init() #start speech engine
recognizer = sr.Recognizer() #initialize speech recognition object
engine.setProperty('rate', 170) #speech rate
engine.setProperty('pitch', 250) # speech pitch
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #get the sound in the second index

#perform certain actions based on user input
def process_input(user_input):
    user_input_lower = user_input.lower().strip()
    responded = False

    if 'search the' in user_input_lower:
        query = user_input_lower.split('search the', 1)[1].strip()
        google_search(query)
        responded = True

    if 'notepad' in user_input_lower:
        speak('I am opening notepad')
        notepad()
        responded = True

    if 'calculator' in user_input_lower:
        speak('I am opening calculator')
        calculator()
        responded = True
    
    if 'email' in user_input_lower:
        speak('I am opening mail')
        mail()
        responded = True

    for clock_search in virtualData.questions_for_clock:
        if clock_search == user_input_lower:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
            responded = True
            break
    
    for bye_key, bye_response in virtualData.shut_down_siona.items():
        if bye_key in user_input_lower:
            speak(bye_response)
            responded = True
            sys.exit()
    
    for date_search in virtualData.question_for_date:
        if date_search == user_input_lower:
            speak(datetime.datetime.now().strftime("%m-%d-%Y"))
            responded = True
            break

    if not responded:
        for name_search, response in virtualData.questions_for_name.items():
            if name_search in user_input_lower:
                speak(response)
                responded = True
                break

    if not responded:
        speak("I did not get that.")

#for google search
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"I am searching for {query}")

#for notepad
def notepad():
    pyautogui.hotkey('winleft')
    time.sleep(0.2)
    pyautogui.write('Notepad', interval=0.10)
    pyautogui.press('enter')

#for calculator
def calculator():
    pyautogui.hotkey('winleft')
    time.sleep(0.2)
    pyautogui.write('Calculator', interval=0.10)
    pyautogui.press('enter')

#for mail
def mail():
    pyautogui.hotkey('winleft')
    time.sleep(0.2)
    pyautogui.write('Mail', interval=0.10)
    pyautogui.press('enter')

#another functions
# def function():
#     pass
# ...

#speech function for voice output
def speak(text):
    print(f"Siona: {text}")
    engine.say(text)
    engine.runAndWait()

#default voice output
speak("Hello sir, what can I do for you?")

while True:
    #receive user input via microphone
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    #Capture the user's voice in English and send it to the process_input function
    try:
        user_input = recognizer.recognize_google(audio, language='en-US')
        print(f"You: {user_input}")
        process_input(user_input)

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")

    except sr.RequestError:
        speak("Sorry, my speech service is down.")
