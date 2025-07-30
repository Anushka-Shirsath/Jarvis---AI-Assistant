import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia 
import pywhatkit as pwk
import user_config
import smtplib, ssl  
import huggingface_request as ai # hugging face # say this - "Jarvis ask AI what is the future of AI" 


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170 )


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def command():
    content = " "
    while content == " ":
       
       r = sr.Recognizer()
       with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)

       try:
        content = r.recognize_google(audio, language='en-in')
        print(" You Said...... " + content)
       except Exception as e:
        print("Please try again...")

   
    return content

jarvis_chat = []


def main_process():
   jarvis_chat = []
   while True:
      request = command().lower()
      if "hello" in request:
         speak("Welcome, How can i help you.")
      elif "play music" in request:
         speak("Playing music")
         song = random.randint(1,3)
         if song == 1:
            webbrowser.open("https://www.youtube.com/watch?v=yJg-Y5byMMw")
         elif song == 2:
            webbrowser.open("https://www.youtube.com/watch?v=RtW-9x_t6Ls")
         elif song == 3:
            webbrowser.open("https://www.youtube.com/watch?v=6QZVNjpkyLY")

      elif "say time" in request:
         now_time = datetime.datetime.now().strftime("%H:%M")
         speak("Current time is "+ str(now_time))

      elif "say date" in request:
         now_time = datetime.datetime.now().strftime("%d:%m")
         speak("Current date is "+ str(now_time))

      elif "new task" in request:
         task = request.replace("new task", " ")
         task = task.strip()
         if task != " ":
            speak("Adding task : "+ task)
            with open ("todo.txt", "a") as file:
               file.write(task + "\n") 

      elif "speak task" in request:
          with open ("todo.txt", "r") as file:
             speak("Work we have to do today is : " + file.read())

      elif "show work" in request:
         with open ("todo.txt", "r") as file:
             tasks = file.read()
         notification.notify(
            title = "Today's work",
            message = tasks         )
         
      elif "open youtube" in request:
         webbrowser.open("www.youtube.com")

         
      elif "open" in request:
         query = request.replace("open", " ")
         pyautogui.press("super")
         pyautogui.typewrite(query)
         pyautogui.sleep(1)
         pyautogui.press("enter")

      elif "wikipedia" in request:
         request = request.replace("jarvis ", " ")
         request = request.replace("search wikipedia ", " ")
         result = wikipedia.summary(request, sentences=2)
         speak(result)

      elif "search google" in request:
         request = request.replace("jarvis ", " ")
         request = request.replace("search google ", " ")
         webbrowser.open("https://www.google.com/search?q="+request)

      elif "send whatsapp" in request:
         pwk.sendwhatmsg("+910123456789", "Hi, How are you", 16, 44, 30) 

      # elif "send email" in request:
      #     pwk.send_mail("anu@gmail.com", user_config.gamil_password, "Hello", "Hello , How are you","anushka@gmail.com") 
      #     speak("Email sent")

      elif "send email" in request:
          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls()
          s.login("anushka@gmail.com", "axtf xnpn howd xhtr")  # App password
          message = """          
          This is the message.
   
          Thanks by Anushka.
          
          """
          s.sendmail("anushka@gmail.com", "anu@gmail.com", message) 
          s.quit()
          speak("Email sent")

      # Hugging Face   # say this - "Jarvis ask AI what is the future of AI" 
      elif "ask ai" in request:
           request = request.replace("ask ai", "").strip()
           jarvis_chat.append({"role": "user", "content": request})

           response = ai.send_request(jarvis_chat)
           print("🤖 AI says:", response)
           speak(response)



      # elif "ask ai " in request:
      #    jarvis_chat = []
      #    request = request.replace("jarvis ", "")
      #    request = request.replace("ask ai ", "")
      #    jarvis_chat.append({"role": "user","content": request})

      #    response = ai.send_request({"messages": jarvis_chat})
      #    speak(response)
      #    response = ai.send_request(jarvis_chat)
      #    speak(response)

      # else:
        
      #    request = request.replace("jarvis ", " ")
     
         
      #    jarvis_chat.append({"role": "user","content": request})
      #    print(jarvis_chat)
      #    response = ai.send_request(jarvis_chat)

      #    jarvis_chat.append({"role": "assistant","content": response})
      #    print(jarvis_chat)
      #    speak(response)

main_process()

         
