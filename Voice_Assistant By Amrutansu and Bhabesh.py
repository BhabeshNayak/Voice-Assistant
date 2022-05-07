import pyttsx3                          # text to speech conversion 
import speech_recognition as sr         # recognising human speech
import datetime                         # To work with the date as well as time 
import wikipedia                        # To get full access Wikipedia using page() functon 
import webbrowser                       # calling the open() function will open the url  
import os                               # To provide funtions for creating and removing a directory,fetching its contents,changing and identifying the current directory
import sys                              # It provides functioos and variables which are used to manipulate different parts of the Python runtime environment
import random                           
import requests                         # Allows to send HTTP requests, in return gets all response data 
import pywhatkit                        # Allows to send messages in whatsapp
import smtplib                          # Used to send emails
import getpass                          # Helps us to add password for security 
import wolframalpha                     # Its's an api which can compute answers using Wolfram's algorithms
from googletrans import Translator      # Tranlates words,phrase into 100+ languages

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[4].id)
engine.setProperty('voices', voices[4].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Boss.")
        speak("Good Morning Boss.")
    elif hour>=12 and hour<18:
        print("Good Afternoon Boss.")
        speak("Good Afternoon Boss.")
    else:
        print("Good Evening Boss.")
        speak("Good Evening Boss.")
    print("I am F.R.I.D.A.Y, your virtual assistant.\n")
    speak("I am FRIDAY, your virtual assistant.")

def response():
    while True:
        print("Please type 'y' whenever you want my help.")
        speak("Please type y whenever you want my help.")
        r=input("Please type your response: ")
        response=r.lower()
        if response=="y" or response=="yes":
            main()
        else:
            print("Invalid Keyword!")
            speak("Invalid Keyword!")
            continue
    
def takeCommand():
    #It takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        print("Please say that again, Boss")
        speak("Please say that again, Boss")
        return "None"
    return query

def openApp(query):
    try:
        try:
            app=query
            path="C:\\Users\\amrut\\Desktop\\"+app
            os.startfile(path)
            print("Opening "+app)
            speak("Opening "+app)
        except:
            path="C:\\Users\\Public\\Desktop\\"+app
            os.startfile(path)
            print("Opening "+app)
            speak("Opening "+app)
    except:
        print("Application Not Found")
        speak("Application Not Found")
        print("Do you want to type the name of an existing application to open it. (Yes/No)")
        speak("Do you want to type the name of an existing application to open it. (Yes or No)")
        query1=takeCommand().lower()
        if "yes" in query1:
            print("Please enter the name of the application")
            speak("Please enter the name of the application")
            query2=input("Enter the name of the application: ")
            openApp(query2)

def WolframAlpha(query):
    f=open("E:\\WolframAlpha.txt","r")
    app_id=f.readline()
    f.close()  
    client=wolframalpha.Client(app_id)
    res=client.query(query)
    answer=next(res.results).text
    print(answer+"\n")
    speak(answer)

def getEmail():
    services_available=['hotmail','gmail','yahoo','outlook']
    while True:
        print("Please type your email address, Boss")
        speak("Please type your email address, Boss")
        my_email=input("Enter your email: ")
        if '@' in my_email and '.com' in my_email:
            sym_pos=my_email.find("@")
            dc_pos=my_email.find(".com")
            sp=my_email[sym_pos+1:dc_pos]
            if sp in services_available:
                return my_email, sp
                break
            else:
                print("Service unavailable for "+sp)
                speak("Service unavailable for "+sp)
                print("Services are only available for "+services_available)
                speak("Services are only available for "+services_available)
        else:
            print("Invalid Email! Please try again!")
            speak("Invalid Email! Please try again!")
            continue

def smtp_domain(serviceProvider):
    if serviceProvider=="gmail":
        return "smtp.gmail.com"
    if serviceProvider=="outlook" or serviceProvider=="hotmail":
        return "smtp-mail.outlook.com"
    if serviceProvider=="yahoo":
        return "smtp.mail.yahoo.com"

def sendEmail(receiver_email,subject,message,content):
    my_email,serviceProvider=getEmail()
    print("Please type your email account password, Boss. For security reasons, your typed password will not be visible.")
    speak("Please type your email account password, Boss. For security reasons, your typed password will not be visible.")
    my_password=getpass.getpass("Enter the password: ")

    try:
        smtp_dom=smtp_domain(serviceProvider)
        server=smtplib.SMTP(smtp_dom, 587)
        server.ehlo()
        server.starttls()
        server.login(my_email,my_password)
    except:
        if serviceProvider=="gmail":
            print("Login unsuccessful! Please allow less secure apps permission. If you have already allowed, then please try again")
            speak("Login unsuccessful! Please allow less secure apps permission. If you have already allowed, then please try again")
            webbrowser.open("https://myaccount.google.com/lesssecureapps")
        else:
            print("Login Unsuccessful! Please try again!")
            speak("Login Unsuccessful! Please try again!")      
    else:
        print("Login Successful.")
        speak("Login Successful.")
        print("Sending the email to "+receiver_email+" with Subject: "+subject+"  and Message: "+message)
        speak("Sending the email to "+receiver_email+" with subject "+subject+" and message "+message)
        server.sendmail(my_email,receiver_email,content)
        print("Email sent successfully.")
        speak("Email sent successfully.")

def main():
    print("I am online and ready.")
    speak("I am online and ready.")
    print("Boss please tell me how can I help you.")
    speak("Boss please tell me how can I help you.")

    while True:
        query=takeCommand().lower()                             #Logic for executing tasks based on query

        if "wait" in query and "friday" in query:
            print("Ok Boss.")
            speak("Ok Boss.")
            response()
        
        elif "what" in query and "your name" in query:
            print("My name is F.R.I.D.A.Y. I am your voice assistant. How can I help you?")
            speak("My name is FRIDAY. I am your voice assistant. How can I help you?")

        elif ("who" in query and ("created you" in query or "your creator" in query)) or ("name" in query and "your creator" in query) or ("whom" in query and ("you created" in query)):
            print("I was created by Amrutansu Samanta.")
            speak("I was created by Aamrutaansu Saamaanta.")     #For pronunciation
            continue

        elif ("who" in query and ("designed you" in query or "your designer" in query)) or ("name" in query and "your designer" in query) or ("whom" in query and "you designed" in query):
            print("I was designed by Amrutansu Samanta.")
            speak("I was designed by Aamrutaansu Saamaanta.")    #For pronunciation
            continue

        elif ("who" in query and ("programmed you" in query or "your programmer" in query)) or ("name" in query and "your programmer" in query) or ("whom" in query and "you programmed" in query):
            print("I was programmed by Amrutansu Samanta.")
            speak("I was programmed by Aamrutaansu Saamaanta.")  #For pronunciation
            continue

        elif "translate" in query:
            languages_dict={"Afrikaans":"af","Albanian":"sq","Amharic":"am","Arabic":"ar","Armenian":"hy","Azerbaijani":"az","Basque":"eu","Belarusian":"be","Bengali":"bn","Bosnian":"bs","Bulgarian":"bg","Catalan":"ca","Cebuano":"ceb","Chinese":"zh-CN","Corsican":"co","Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Esperanto":"eo","Estonian":"et","Finnish":"fi","French":"fr","Frisian":"fy","Galician":"gl","Georgian":"ka","German":"de","Greek":"el","Gujarati":"gu","Haitian Creole":"ht","Hausa":"ha","Hawaiian":"haw","Hebrew":"he","Hindi":"hi","Hmong":"hmn","Hungarian":"hu","Icelandic":"is","Igbo":"ig","Indonesian":"id","Irish":"ga","Italian":"it","Japanese":"ja","Javanese":"jv","Kannada":"kn","Kazakh":"kk","Khmer":"km","Kinyarwanda":"rw","Korean":"ko","Kurdish":"ku","Kyrgyz":"ky","Lao":"lo","Latin":"la","Latvian":"lv","Lithuanian":"lt","Luxembourgish":"lb","Macedonian":"mk","Malagasy":"mg","Malay":"ms","Malayalam":"ml","Maltese":"mt","Maori":"mi","Marathi":"mr","Mongolian":"mn","Myanmar (Burmese)":"my","Nepali":"ne","Norwegian":"no","Nyanja":"ny","Odia":"or","Pashto":"ps","Persian":"fa","Polish":"pl","Portuguese":"pt","Punjabi":"pa","Romanian":"ro","Russian":"ru","Samoan":"sm","Scots Gaelic":"gd","Serbian":"sr","Sesotho":"st","Shona":"sn","Sindhi":"sd","Sinhala":"si","Slovak":"sk","Slovenian":"sl","Somali":"so","Spanish":"es","Sundanese":"su","Swahili":"sw","Swedish":"sv","Tagalog":"tl","Tajik":"tg","Tamil":"ta","Tatar":"tt","Telugu":"te","Thai":"th","Turkish":"tr","Turkmen":"tk","Ukrainian":"uk","Urdu":"ur","Uyghur":"ug","Uzbek":"uz","Vietnamese":"vi","Welsh":"cy","Xhosa":"xh","Yiddish":"yi","Yoruba":"yo","Zulu":"zu"}
            print("Do you want to type or speak the text to be translated?")
            speak("Do you want to type or speak the text to be translated.")
            query1=takeCommand().lower()
            if "type" in query1:
                print("Please type the text to be translated.")
                speak("Please type the text to be translated.")
                text=input("Enter the text: ")
                print("Which language do you want this text to be converted to?")
                speak("Which language do you want this text to be converted to?")
                dest_language=input("Enter the destination language: ")
                dest_language=dest_language.capitalize()
                dest_language_id=languages_dict[dest_language]
            elif "speak" in query1:
                print("Please say the text to be translated.")
                speak("Please say the text to be translated.")
                text=takeCommand()
                print("Which language do you want this text to be converted to?")
                speak("Which language do you want this text to be converted to?")
                dest_language=takeCommand().capitalize()
                dest_language_id=languages_dict[dest_language]
            else:
                print("Invalid Statement! Please try again.")
                speak("Invalid Statement! Please try again.")
                continue
            translator = Translator(service_urls=['translate.googleapis.com'])
            t=translator.translate(text, dest=dest_language_id)
            print("Source language:",t.src)
            speak("Source language:"+t.src)
            print("Destination language:",t.dest)
            speak("Destination language:"+t.dest)
            print("Translated Text: "+t.text)
            speak("Translated Text: "+t.text)
            print("Pronunciation: ",t.pronunciation)
            speak("Pronunciation: "+t.pronunciation)

        elif "wikipedia" in query or "who is" in query or "who was" in query:
            print("Searching Wikipedia...\n")
            speak("Searching Wikipedia")
            try:
                query=query.replace("wikipedia", "")
                query=query.replace("who is ", "")
                query=query.replace("who was ", "")
                results=wikipedia.summary(query, sentences=3)
                print("According to Wikipedia,")
                speak("According to Wikipedia")
                print(results+"\n")
                speak(results)                
            except:
                print("Result not found.\n")                
                speak("Result not found.")

        elif "weather" in query:
            f=open("E:\\Openweathermap.txt","r")
            user_api=f.readline()
            f.close()
            print("Do you want to type the name of the city or speak it.")
            speak("Do you want to type the name of the city or speak it.")
            query1=takeCommand().lower()
            if "type" in query1:
                print("Please type the name of the city to know the weather.")
                speak("Please type the name of the city to know the weather.")
                location=input("Enter the name of the city: ")
                location=location.capitalize()
            elif "speak" in query1:
                print("Please tell the name of the city to know the weather.")
                speak("Please tell the name of the city to know the weather.")            
                location=takeCommand().capitalize()
            else:
                print("Invalid Statement! Please try again.")
                speak("Invalid Statement! Please try again.")
                continue
                
            try:
                complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
                api_link = requests.get(complete_api_link)
                api_data = api_link.json()
                #create variables to store and display data
                temp_city = ((api_data['main']['temp']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                print ("-------------------------------------------------------------")
                print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
                print ("-------------------------------------------------------------")
                print ("Current temperature is      : {:.2f} deg C".format(temp_city))
                print ("Current weather description :",weather_desc)
                print ("Current Humidity            :",hmdt, '%')
                print ("Current wind speed          :",wind_spd ,'kmph\n')
                speak("Currently in "+location+", the temperature is, {:.2f} ".format(temp_city)+" degrees celsius, with "+weather_desc+", with humidity, "+str(hmdt)+" percent, and wind speed, "+str(wind_spd)+" kilometres per hour ")
            except:
                print("Cannot find the weather of the requested city.\n")
                speak("Cannot find the weather of the requested city.")

        elif "open youtube" in query:
            print("Opening Youtube.\n")
            speak("Opening Youtube.")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            print("Opening Google.\n")
            speak("Opening Google.")
            webbrowser.open("google.com")

        elif "open" in query and "website" in query:
            print("Do you want to type the Website URL or speak it.")
            speak("Do you want to type the Website URL or speak it.")
            query1=takeCommand().lower()
            if "type" in query1:
                print("Please type the name of the website.")
                speak("Please type the name of the website.")
                website_url=input("Enter the Website URL: ")
                website_url=website_url.replace(" ","")
            elif "speak" in query1:
                print("Please say the name of the website.")
                speak("Please say the name of the website.")
                website_url=takeCommand().lower()
                website_url=website_url.replace(" ","")
            else:
                print("Invalid Statement!. Please try again.")
                speak("Invalid Statement!. Please try again.")
            print("Opening the Website URL.")
            speak("Opening the Website URL.")
            webbrowser.open(website_url)

        elif "open" in query or ("open" in query and ("app" in query or "application" in query)):
            query=query.replace("open ","")
            openApp(query)

        elif "play music" in query or "play song" in query:
            print("Playing Music.\n")
            speak("Playing Music.")
            music_dir="E:\\Games 1\\Downloaded Songs\\Favourites"
            songs=os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,(len(songs)-1))]))

        elif ("play" in query and ("music" not in query and "song" not in query)) or "on youtube" in query:
            query=query.replace("play","")
            query=query.replace("on youtube","")
            query=query.replace("youtube","")
            query=query.capitalize()
            print("Playing",query,"on YouTube.\n")
            speak("Playing "+query+" on YouTube.")
            pywhatkit.playonyt(query)

        elif "the time" in query:
            strTime=str(datetime.datetime.now())
            hour=strTime[11:13]
            minute=strTime[14:16]
            second=strTime[17:19]
            time=hour+":"+minute+":"+second
            print("Boss the time is", time)
            speak("Boss the time is "+hour+" hours "+minute+" minutes "+second+" seconds.")

        elif "the date" in query:
            strDate=str(datetime.datetime.now())
            date=strDate[8:10]
            month=strDate[5:7]
            monthlist={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
            monthname=monthlist[month]
            year=strDate[0:4]
            print("Boss the date is "+date+" "+monthname+" "+year)
            speak("Boss the date is "+date+" "+monthname+" "+year)

        elif "the day" in query or ("what" in query and "today" in query):
            day=datetime.datetime.today().weekday()
            day_dict={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
            if day in day_dict.keys(): 
                day_of_the_week=day_dict[day] 
                print("Boss today is",day_of_the_week) 
                speak("Boss today is " + day_of_the_week)

        elif "send" in query and "whatsapp message" in query:
            print("Do you want to type the number of the Receiver or speak it?")
            speak("Do you want to type the number of the Receiver or speak it?")
            query1=takeCommand().lower()
            if "type" in query1:
                print("Please type the WhatsApp number of the Receiver.")
                speak("Please type the WhatsApp number of the Receiver.")
                Num=input("Enter the receiver's WA Number: ")
                if len(Num)==10:
                    WA_No="+91"+Num
                else:
                    WA_No=Num
            elif "speak" in query1:
                print("Please say the WhatsApp number of the Receiver.")
                speak("Please say the WhatsApp number of the Receiver.")
                query2=takeCommand().lower()
                query2=query2.replace(" ","")
                if len(query2)==10:
                    WA_No="+91"+query2
                else:
                    WA_No=query2
            else:
                print("Invalid Statement! Please try again.")
                speak("Invalid Statement! Please try again.")
                continue
            
            print("Please confirm the WhatsApp number of the receiver, Boss. (Yes/No)")
            speak("Please confirm the WhatsApp number of the receiver, Boss. (Yes or No)")
            print("Given WhatsApp number: ",WA_No) 
            speak("Given WhatsApp number is"+WA_No)

            query1=takeCommand().lower()
            if "no" in query1 or "negative" in query1:
                print("Ok Boss.")
                speak("Ok Boss.")
                continue
            print("Do you want to type the message or speak it?")
            speak("Do you want to type the message or speak it?")
            query1=takeCommand().lower()
            if "type" in query1:
                print("What message do you want to send?")
                speak("What message do you want to send?")
                message=input("Enter the message: ")
            elif "speak" in query1:
                print("What message do you want to send?")
                speak("What message do you want to send?")
                query1=takeCommand()
                message=query1
            else:
                print("Invalid Statement! Please try again.")
                speak("Invalid Statement! Please try again.")
                continue
            print("Please confirm the message, Boss. (Yes/No)")
            speak("Please confirm the message, Boss. (Yes or No)")
            print("Given Message: ",message)
            speak("The given message is "+message)

            query1=takeCommand().lower()
            if "no" in query1 or "negative" in query1:
                print("Ok Boss.")
                speak("Ok Boss.")
                continue
            print("Do you want to type the time of the scheduled message or speak it?")
            speak("Do you want to type the time of the scheduled message or speak it?")
            query2=takeCommand().lower()
            if "type" in query2:
                print("Please type the time at which you want to send the message. Please select a time not less than 3-4 minutes after current time.")
                speak("Please type the time at which you want to send the message. Please select a time not less than 3-4 minutes after current time.")
                print("Please type the hour of the day.")
                speak("Please type the hour of the day.")
                hour=int(input("Hour: "))
                print("Please type the minute of the day.")
                speak("Please type the minute of the day.")
                minute=int(input("Minute: "))
            elif "speak" in query2:
                print("At what time do you want to send the message. (24 Hour Format). Please select a time not less than 3 minutes after current time.")
                speak("At what time do you want to send the message, in 24 Hour Format. Please select a time not less than 3 minutes after current time.")
                time=takeCommand().lower()
                time=time.replace(" ","")
                time=list(time)
                hour=int(time[0]+time[1])
                minute=int(time[2]+time[3])
            else:
                print("Invalid Statement! Please try again.")
                speak("Invalid Statement! Please try again.")
                continue
            print("Please confirm the time, Boss. (Yes/No)")
            speak("Please confirm the time, Boss. (Yes or No)")
            print("The desired time is "+str(hour)+":"+str(minute))
            speak("The desired time is "+str(hour)+" hours and "+str(minute)+" minutes")

            query1=takeCommand().lower()
            if "no" in query1 or "negative" in query1:
                print("Ok Boss.")
                speak("Ok Boss.")
                continue
            print("The web browser will automatically open one minute before the scheduled time and the message will be automatically sent to",WA_No,"at",str(hour)+":"+str(minute)+". Please don't close the program, Boss.")
            speak("The web browser will automatically open one minute before the scheduled time and the message will be automatically sent to "+WA_No+" at "+str(hour)+" hours and "+str(minute)+" minutes. Please don't close the program, Boss.")
            print("Please scan the QR Code in the browser using the WhatsApp Web option in your smartphone, if prompted to do so.")
            speak("Please scan the QR Code in the browser using the WhatsApp Web option in your smartphone, if prompted to do so.")
            pywhatkit.sendwhatmsg(WA_No,message,hour,minute,60)
            print("Message Sent.")
            speak("Message Sent.")

        elif "send" in query and ("email" in query or "gmail" in query or "mail" in query):
            try:
                smtplib.SMTP()
                print("Please type the email address of the receiver.")
                speak("Please type the email address of the receiver.")
                receiver_email=input("Enter the receiver's email address: ")
                print("Please confirm the receiver's email address. (Yes/No)")
                speak("Please confirm the receiver's email address. (Yes or No)")
                print("The given email address is: ",receiver_email)
                speak("The given email address is: "+receiver_email)
                query1=takeCommand().lower()
                if "no" in query1 or "negative" in query1:
                    print("Ok Boss.")
                    speak("Ok Boss.")
                    continue
                print("Do you want to type the message or speak it?")
                speak("Do you want to type the message or speak it?")
                query1=takeCommand().lower()
                if "type" in query1:
                    print("Please type the subject.")
                    speak("Please type the subject.")
                    subject=input("Enter the subject: ")
                    print("What message do you want to send?")
                    speak("What message do you want to send?")
                    message=input("Enter the message: ")
                elif "speak" in query1:
                    print("Please say the subject.")
                    speak("Please say the subject.")
                    subject=takeCommand()
                    print("What message do you want to send?")
                    speak("What message do you want to send?")
                    message=takeCommand()
                else:
                    print("Invalid Statement! Please try again.")
                    speak("Invalid Statement! Please try again.")
                    continue
                content=("Subject: "+subject+"\n\n"+message)
                print("Please confirm the content. (Yes/No)")
                speak("Please confirm the content. (Yes or No)")
                print("The given content is:\n",content)
                speak("The given content is: "+content)
                query1=takeCommand().lower()
                if "no" in query1 or "negative" in query1:
                    print("Ok Boss.")
                    speak("Ok Boss.")
                    continue
                print("Please login to your email account first, Boss. ")
                speak("Please login to your email account first, Boss. ")
                sendEmail(receiver_email,subject,message,content)
            except Exception as e:
                print(e)
                print("Unable to send the email!")
                speak("unable to send the email!")

        elif "search " in query or "what " in query or "who " in query or "tell " in query:
            query=query.replace("search ","")
            print("Searching "+query+" on Google.\n")
            speak("Searching "+query+" on Google.")
            pywhatkit.search(query)
            try: 
                WolframAlpha(query)
            except:
                pass

        elif ("make" in query or "create" in query) and "note" in query:
            f1=open("Note_By_FRIDAY.txt","a")
            print("Would you like to type the note or speak it.")
            speak("Would you like to type the note or speak it.")
            query1=takeCommand().lower()
            if "type" in query1:
                print("What would you like to note, Boss?")
                speak("What would you like to note? Boss")
                note=input("Enter the note: ")
                f1.write(note+"\n\n")
            elif "speak" in query1:
                print("What would you like to note, Boss?")
                speak("What would you like to note? Boss")
                note=takeCommand()
                f1.write(note+"\n\n")
            else:
                print("Invalid Statement!. Please try again.")
                speak("Invalid Statement!. Please try again.")
                continue
            f1.close()
            print("Note composed.")
            speak("Note composed.")

        elif "read" in query and "note" in query:
            f2=open("Note_By_FRIDAY.txt","r")
            contents=f2.read()
            print(contents)
            speak(contents)

        elif "hi " in query or "hello" in query:
            print("Hello Boss. How can I help you?\n")
            speak("Hello Boss. How can I help you?")

        elif "thank you" in query or "thanks" in query:
            print("Most Welcome Boss. It is my pleasure to help you.\n")
            speak("Most Welcome Boss. It is my pleasure to help you.")

        elif "how are you" in query or "what's up" in query:
            print("Thanks for asking me Boss. I am doing good.\n")
            speak("Thanks for asking me Boss. I am doing good.")

        elif ("you are" in query and ("intelligent" in query or "good" in query or "nice" in query or "talented" in query)) or ("your voice" in query and ("nice" in query or "good" in query)):
            print("Thanks a lot for the compliment, Boss. It means a lot for me.\n")
            speak("Thanks a lot for the compliment, Boss. It means a lot for me.")

        elif "good morning" in query:
            print("A Very Good Morning Boss. Hope your day goes well. How can I help you.\n")
            speak("A Very Good Morning Boss. Hope your day goes well. How can I help you.")

        elif "good afternoon" in query:
            print("A Very Good Afternoon Boss. Hope everything is going on well. How can I help you.\n")
            speak("A Very Good Afternoon Boss. Hope everything is going on well. How can I help you.")

        elif "good evening" in query:
            print("Good Evening Boss. Hope your day went well. How can I help you.\n")
            speak("Good Evening Boss. Hope your day went well. How can I help you.")

        elif "good night" in query:
            print("Good Night Boss. Hope tomorrow will be another good day for you.\n")
            speak("Good Night Boss. Hope tomorrow will be another good day for you.")

        elif "quit" in query or "exit" in query or "close" in query:
            print("Thank you Boss for interacting with me.\n")
            speak("Thank you Boss for interacting with me.")
            sys.exit()
        
        elif "shut down windows" in query or "shutdown windows" in query:
            print("All unsaved data will be lost. Are you sure you want to shut down windows? (Yes/No)")
            speak("All unsaved data will be lost. Are you sure you want to shut down windows? (Yes or No)")
            query1=takeCommand().lower()
            if "yes" in query1:
                print("Thank you Boss for interacting with me.")
                speak("Thank you Boss for interacting with me.")
                print("Closing all programs and shutting down Windows.\n")
                speak("Closing all programs and shutting down Windows.")
                os.system("shutdown /s /t 00")
                sys.exit()

        elif "restart windows" in query:
            print("All unsaved data will be lost. Are you sure you want to restart windows? (Yes/No)")
            speak("All unsaved data will be lost. Are you sure you want to restart windows? (Yes or No)")
            query1=takeCommand().lower()
            if "yes" in query1:
                print("Thank you Boss for interacting with me.")
                speak("Thank you Boss for interacting with me.")
                print("Closing all programs and restarting Windows.\n")
                speak("Closing all programs and restarting Windows.")
                os.system("shutdown /r /t 00")
                sys.exit()

        elif "hibernate windows" in query:
            print("Are you sure you want to hibernate windows? (Yes/No)")
            speak("Are you sure you want to hibernate windows? (Yes or No)")
            query1=takeCommand().lower()
            if "yes" in query1:
                print("Saving current profile and hibernating windows.")
                speak("Saving current profile and hibernating windows.")
                os.system("shutdown /h")

        elif "log off windows" in query or "logoff windows" in query:
            print("All unsaved data will be lost. Are you sure you want to log off windows? (Yes/No)")
            speak("All unsaved data will be lost. Are you sure you want to log off windows? (Yes or No)")
            query1=takeCommand().lower()
            if "yes" in query1:
                print("Thank you Boss for interacting with me.")
                speak("Thank you Boss for interacting with me.")
                print("Closing all programs and logging off windows.")
                speak("Closing all programs and logging off windows.")
                os.system("shutdown /l")
                sys.exit()

        elif "friday" in query:
            print("Yes Boss, I am at your service. Please tell me how can I help you.")
            speak("Yes Boss, I am at your service. Please tell me how can I help you.")

        elif "advanced search" in query or "advance search" in query:
            try:
                print("What do you want to advance search?")
                speak("What do you want to advance search?")
                query2=takeCommand()
                print("Searching...")
                speak("Searching")
                WolframAlpha(query2)
            except:
                print("Invalid Command!")
                speak("Invalid Command!")

        else:
            print("Unknown Command! Please say another command Boss.")
            speak("Unknown Command! Please say another command Boss.")

f=open("Note_By_FRIDAY.txt","w")
f.write("NOTE:\n")
f.close()            
wishMe()
response()