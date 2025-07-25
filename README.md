# Nova Virtual Desktop Assistant 💬🧠

Nova is a desktop-based **virtual assistant** built using **Python**. It can respond to voice and text commands to perform tasks like searching Wikipedia, opening websites, telling jokes, giving weather updates, and even sending WhatsApp messages.

---

## 🚀 Features

- 🧠 Voice & Text command input
- 🗣️ Text-to-Speech using `pyttsx3`
- 🔍 Wikipedia search
- 🌐 Opens websites like YouTube, Google, Gmail, StackOverflow, etc.
- 🕒 Tells current time
- 😂 Tells random jokes (via `pyjokes`)
- ☁️ Shows weather (via Google search)
- 📤 Send WhatsApp messages (using `pywhatkit`)
- 🖥️ GUI Interface using Tkinter

---

## 📁 Project Files

| File           | Description                                |
|----------------|--------------------------------------------|
| `final.py`     | Main assistant with GUI + voice commands   |
| `Prototype.py` | Simplified version (GUI only)              |
| `sample.py`    | CLI-based voice assistant (no GUI)         |

---

## 🛠️ How to Run the Project

### 1. Install Required Libraries

Make sure Python is installed. Then open terminal (or CMD) and run:

```bash
pip install pyttsx3 wikipedia pyjokes pywhatkit SpeechRecognition


Optional: You may also need pyaudio for microphone input
Install it using:
pip install pipwin
pipwin install pyaudio

2. Run the Assistant
python final.py

🧪 Sample Commands You Can Try
    -"Search Virat Kohli on Wikipedia"
    -"Open YouTube"
    -"Tell me today weather"
    -"Tell me a joke"
    -"Send message on WhatsApp"
    -"What’s the time"
    -"Who made you?"

🧑‍💻 Developer
Anuj Kumar Jha

📄 License
This project is licensed under the MIT License — free to use and modify.
