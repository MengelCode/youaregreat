# !/usr/bin/python3
import secrets
from sys import argv
from time import sleep
from os import name, system

# Possible mantras which can be printed on-screen.
# This list contains positive affirmations.
messages_en = [
    "You are great, because you are who you are.",
    "You are a valuable human being.",
    "Do not give up. Even if it seems to be the only way out.",
    "When you expect it the least, the most miracles will happen.",
    "You will never be truly alone.",
    "You are beautiful.",
    "When others insult you: They are the weak ones, not you.",
    "Right now, there is somebody who believes in you.",
    "Think about your achievements.",
    "You are great!",
    "Not overestimating yourself is good. But underestimation won't do you any good either.",
    "Nothing did stop you completely. It will stay like this.",
    "Even in the greatest darkness, there is some light.",
    "Seek the society of people who appreciate you, avoid those of people who do not.",
    "You also have skills and qualities.",
    "You most likely accomplished something today. Even if it is just something tiny.",
    "If you see this, you most likely mastered some challenges in the past.",
    "You deserve to be appreciated. Do not let somebody tell you something else.",
    "There is nothing like a 'normal' person. Be yourself, do not wear a theatre mask.",
    "Seeking help from others is no sign of weakness.",
    "Allow yourself to be happy and sad alike.",
    "Emotions are part of your nature.",
    "Everyone has bad days. But those days will eventually pass and good ones will come.",
    "There is nobody exactly like you again. You are a unique treasure.",
    "The sun will always return.",
    "The only human who never makes a mistake is the human who never does anything.",
    "Everyone was once a novice.",
    "Even if it does not look like it, somebody does care for you.",
    "Sometimes you have to wait for a while, but at some point, feelings of accomplishment will return to you.",
    "It is sometimes very hard to be honest. But it will pay off in the end.",
    "Everyone is a star. We all just need to find our way to shine.",
    "You have potential! You will eventually find a way to use it.",
]

use_notify = len(argv) > 1 and argv[1] == "-n"
use_xmessage = len(argv) > 1 and argv[1] == "-xm"

while True:
    if name == "nt":
        system("cls")

    else:
        system("clear")

    randomIndex = secrets.randbelow(len(messages_en))
    if use_xmessage:
       system("xmessage -buttons 'Thank you!':0 -nearmouse -timeout 65 '" + messages_en[randomIndex] + "'")
    elif use_notify:
        system("notify-send 'You are great!' " + "'" + messages_en[randomIndex] + "'")
    else:
        print(messages_en[randomIndex])
    sleep(300)
