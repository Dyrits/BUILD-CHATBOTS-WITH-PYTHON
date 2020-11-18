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

    def __init__(self, name="Etcaetera"):
        self.username = None
        self.name = name
        self.intents = {
            r'.*your planet.*': self.describe_planet_intent,
            r'.*why are.*': self.answer_why_intent,
            r'.*cube.*?(\d+).*': self.cubed_intent
        }

    def greet(self):
        self.username = input("Hello there! What's your name? \n")
        will_help = input(f"Hi {self.username}, I'm {self.name}. I'm not from this planet. Will you help me learn about your planet? \n")
        return self.exit() if will_help.lower() in self.negative_responses else self.chat()

    def exit(self):
        print(f"Okay {self.username}, have a nice Earth day! \n")

    def make_exit(self, reply):
        for word in self.exit_commands:
            if reply in word:
                return self.exit() or True

    def chat(self):
        while not self.make_exit(reply := input(random.choice(self.random_questions) + "\n").lower()):
            self.match_reply(reply)

    def match_reply(self, reply):
        for regex_pattern, intent in self.intents.items():
            if found_match := re.match(regex_pattern, reply):
                parameters = found_match.groups()
                return intent(*parameters)
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (f"My planet, {self.username}, is an utopia of diverse organisms and species.",
                     "I am from Opidipus, the capital of the Wayward Galaxies. ")
        print(random.choice(responses))

    def answer_why_intent(self):
        responses = ("I come in peace.",
                     f"I am here to collect data on your planet and its inhabitants, including you {self.username}.",
                     "I heard the coffee is good.")
        print(random.choice(responses))

    def cubed_intent(self, number):
        print(f"The cube of {number} is {int(number) ** 3}. Isn't that cool, {self.username}?")

    def no_match_intent(self):
        responses = (f"Please {self.username} tell me more.",
                     "Tell me more!",
                     "Why do you say that?",
                     f"I see, {self.username}. Can you elaborate?",
                     "Interesting. Can you tell me more?",
                     "I see. How do you think?",
                     f"Why? {self.username}, why?",
                     "How do you think I feel when you say that?"
                     )
        print(random.choice(responses))


if __name__ == '__main__':
    AlienBot().greet()
