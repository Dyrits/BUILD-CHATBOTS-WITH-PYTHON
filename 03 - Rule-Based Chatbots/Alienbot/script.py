# importing regex and random libraries
import re
import random


class AlienBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = ("Why are you here?",
                        "Are there many humans like you?",
                        "What do you consume for sustenance?",
                        "Is there intelligent life on this planet?",
                        "Does Earth have a leader?",
                        "What planets have you visited?",
                        "What technology do you have on this planet?")

    def __init__(self):
        self.intents = {
            r'.*your planet.*': self.describe_planet_intent,
            r'.*why are.*': self.answer_why_intent,
            r'.*cube.*(?P<number>\d+).*': self.cubed_intent
        }

    def greet(self):
        self.name = input("Hello there! What's your name? \n")
        will_help = input(
            f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? \n")
        if will_help.lower() in self.negative_responses:
            return self.exit()
        self.chat()

    def exit(self):
        print(f"Okay {self.name}, have a nice Earth day! \n")

    def make_exit(self, reply):
        for word in self.exit_commands:
            if reply in word:
                return self.exit()

    def chat(self):
        while not self.make_exit(reply := input(random.choice(self.random_questions)).lower()):
            self.match_reply(reply)

    def match_reply(self, reply):
        for regex_pattern, intent in self.intents.items():
            if found_match := re.match(regex_pattern, reply, re.IGNORECASE):
                print(intent(found_match.group(1)) if found_match.groups() else intent())
            else:
                print(self.no_match_intent())

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.",
                     "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace.",
                     "I am here to collect data on your planet and its inhabitants.",
                     "I heard the coffee is good.")
        return random.choice(responses)

    def cubed_intent(self, number):
        return f"The cube of {number} is {int(number) ** 3}. Isn't that cool?"

    def no_match_intent(self):
        responses = ("Please tell me more.",
                     "Tell me more!",
                     "Why do you say that?",
                     "I see. Can you elaborate?",
                     "Interesting. Can you tell me more?",
                     "I see. How do you think?",
                     "Why?",
                     "How do you think I feel when you say that?"
                     )
        return random.choice(responses)


AlienBot().greet()
