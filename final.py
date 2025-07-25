import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit
import speech_recognition as sr

class AssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Nova Assistant")
        master.configure(bg="#1f1f2e")  # Dark background

        # Style configuration
        label_font = ("Helvetica", 11, "bold")
        entry_font = ("Helvetica", 11)
        button_font = ("Helvetica", 10, "bold")
        text_bg = "#2c2c3c"
        text_fg = "#00ffcc"
        btn_bg = "#00bcd4"
        btn_fg = "white"

        # Output box
        self.output = scrolledtext.ScrolledText(master, width=70, height=18, font=("Courier New", 10), bg=text_bg, fg=text_fg, wrap=tk.WORD, bd=2)
        self.output.grid(row=0, column=0, columnspan=3, padx=15, pady=15)

        # Input label
        self.input_label = tk.Label(master, text="Type your command:", font=label_font, bg="#1f1f2e", fg="white")
        self.input_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        # Input entry
        self.input_entry = tk.Entry(master, width=45, font=entry_font, bg="#3e3e4d", fg="white", bd=2, insertbackground='white')
        self.input_entry.grid(row=1, column=1, padx=10, pady=5)

        # Send button
        self.send_button = tk.Button(master, text="Send", font=button_font, command=self.send_command, bg=btn_bg, fg=btn_fg, width=10)
        self.send_button.grid(row=1, column=2, padx=10, pady=5)

        # Voice button
        self.voice_button = tk.Button(master, text="🎤 Speak", font=button_font, command=self.voice_send_command, bg="#4caf50", fg="white", width=10)
        self.voice_button.grid(row=2, column=1, padx=10, pady=10)

        # Initialize TTS
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def take_command(self):
        query = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)
        return query

    def voice_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.output.insert(tk.END, "Listening...\n")
            self.output.see(tk.END)
            self.speak("Listening")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            self.output.insert(tk.END, "Recognizing...\n")
            self.output.see(tk.END)
            query = r.recognize_google(audio, language='en-in')
            self.output.insert(tk.END, f"User said: {query}\n")
            self.output.see(tk.END)
            return query.lower()

        except Exception:
            self.output.insert(tk.END, "Sorry, I didn't catch that. Please repeat...\n")
            self.output.see(tk.END)
            self.speak("Sorry, I didn't catch that. Please repeat")
            return "None"

    def voice_send_command(self):
        query = self.voice_command()
        if query != "None":
            self.input_entry.insert(0, query)
            self.send_command()

    def send_command(self):
        query = self.take_command()
        self.output.insert(tk.END, f"User said: {query}\n")
        self.output.see(tk.END)

        # === Functional Commands ===
        try:
            if 'wikipedia' in query:
                self.output.insert(tk.END, "Searching Wikipedia...\n")
                self.output.see(tk.END)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.output.insert(tk.END, "According to Wikipedia:\n" + results + "\n")
                self.output.see(tk.END)
                self.speak("According to Wikipedia")
                self.speak(results)

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif "tell me today weather" in query:
                webbrowser.open("https://www.google.com/search?q=weather")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                self.output.insert(tk.END, f"The current time is {strTime}\n")
                self.output.see(tk.END)
                self.speak(f"The current time is {strTime}")

            elif "which language is used to develop you" in query:
                self.output.insert(tk.END, "I am developed using Python!\n")
                self.output.see(tk.END)
                self.speak("I am developed using Python!")

            elif "who made you" in query:
                self.output.insert(tk.END, "I am developed by Anuj!\n")
                self.output.see(tk.END)
                self.speak("I am developed by Anuj!")

            elif "hello nova" in query:
                self.output.insert(tk.END, "Hello sir!\n")
                self.output.see(tk.END)
                self.speak("Hello sir!")

            elif "how are you" in query:
                self.output.insert(tk.END, "I am fine and what about you!\n")
                self.output.see(tk.END)
                self.speak("I am fine and what about you!")

            elif 'open stackoverflow' in query:
                webbrowser.open("https://www.stackoverflow.com")

            elif 'play music' in query:
                webbrowser.open("https://www.youtube.com/watch?v=691Gy98MWbw")

            elif 'open code' in query:
                os.startfile("C:\\Users\\aj954\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open telegram' in query:
                webbrowser.open("https://web.telegram.org/")

            elif 'open instagram' in query:
                webbrowser.open("https://www.instagram.com/")

            elif 'open linkedin' in query:
                webbrowser.open("https://www.linkedin.com/")

            elif 'open amazon' in query:
                webbrowser.open("https://www.amazon.com/")

            elif 'open flipkart' in query:
                webbrowser.open("https://www.flipkart.com/")

            elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'play my best song' in query:
                webbrowser.open("https://www.youtube.com/watch?v=a8CF5YudYUk")

            elif 'open chrome' in query:
                webbrowser.open("https://www.google.com/chrome/")

            elif 'tell me a joke' in query:
                joke = pyjokes.get_joke()
                self.output.insert(tk.END, f"Here's a joke for you: {joke}\n")
                self.output.see(tk.END)
                self.speak(f"Here's a joke for you: {joke}")

            elif 'send message on whatsapp' in query:
                self.output.insert(tk.END, "Please enter the phone number and message in the format: 'phone_number message'\n")
                self.output.see(tk.END)
                self.speak("Please enter the phone number and message in the format: 'phone_number message'")
                message_info = self.take_command().split()
                if len(message_info) >= 2:
                    phone_number = message_info[0]
                    message = ' '.join(message_info[1:])
                    pywhatkit.sendwhatmsg(phone_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
                    self.output.insert(tk.END, f"Message sent to {phone_number} successfully!\n")
                    self.output.see(tk.END)
                    self.speak(f"Message sent to {phone_number} successfully!")
                else:
                    self.output.insert(tk.END, "Invalid format. Please provide phone number and message.\n")
                    self.output.see(tk.END)
                    self.speak("Invalid format. Please provide phone number and message.")

            elif 'show me directions to' in query:
                destination = query.replace('show me directions to', '').strip()
                webbrowser.open(f"https://www.google.com/maps/dir/?api=1&destination={destination}")
        except Exception as e:
            self.output.insert(tk.END, f"Something went wrong: {str(e)}\n")
            self.output.see(tk.END)
            self.speak("Something went wrong")

# Launch the GUI
root = tk.Tk()
app = AssistantGUI(root)
root.mainloop()
