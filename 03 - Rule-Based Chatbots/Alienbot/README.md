# [Alienbot](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/rule-based-chatbots/projects/python-chatbot-alienbot) 

## Table of contents
- [Related content](#related-content)
- [General information](#general-information)
- [Technologies](#technologies)
- [Status](#status)
  - [Features](#features)
  - [Changelog](#changelog)
  - [To-do](#to-do)
 - [Contributing](#contributing)
- [Contact](#contact)

## Related content
**Website:** [Codecademy](https://www.codecademy.com/)  
**Skill Path:** [Build Chatbots with Python](https://www.codecademy.com/learn/paths/build-chatbots-with-python) <sup>PRO</sup>  
**Content:** 3. Rule-Based Chatbots / Rule-Based Chatbots / [Alienbot](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/rule-based-chatbots/projects/python-chatbot-alienbot)

## General information

### Description by [Codecademy](https://www.codecademy.com/)

The 1950s ushered in a slew of UFO sightings and excitement about outer space. Incidentally, the decade also brought about a new idea of artificial intelligence. The computer scientist Alan Turing proposed that if a computer was able to fool a human into believing it was human, the computer would be considered “intelligent.”

While your bot may not pass a true Turing test, perhaps it could pass an “E.T.uring” test if you can successfully fool a human into believing that your chatbot is, in fact, an alien.

We’ve added a class called AlienBot to get you started; you’ll be digging into the main chatbot functionality. Take a look at what you have in **script.py**:
- the `regex` and `random` libraries are imported
- a tuple of negative responses (you can add more!)
- a tuple of commands for a user to exit the program
- a tuple of random starter questions an alien might ask (feel free to add more)
- a tuple of dictionaries called `alienbabble` with the chatbot’s main intent-utterance matching pairs — you’ll add to this later!
- several methods for core chatbot functionality:
- `.greet()` will greet the user
- `.make_exit()` will check if a user has used an exit command
- `.chat()` will run the program allowing users to chat with the alien you created
- `.match_reply()` will match the response pairs in `alienbabble` for you
- several methods associated with user intents
    - `.describe_planet_intent()` will include responses about the alien’s planet
    - `.answer_why_intent()` will include responses for why the alien is visiting
    - `.cubed_intent()` is a method that returns the cube of a number, because these aliens are very good at math
    - `.no_match_intent()` will respond with something general when none of the other intents are matched

As you add to the chatbot, you can check the functionality by:
1. Pressing the **Save** button
2. Running the following from the terminal, with:
```
python3 script.py
```

## Technologies
- [Python](https://www.python.org/) (3.8)
    - [re](https://github.com/python/cpython/blob/3.9/Lib/re.py) - Regular expression operations

## Status
Project (1.0) completed the 18/11/2020. 

### Features
All the required features (as described in [General information](#general-information)) have been implemented.

### Changelog
<details markdown="block">
<summary>Version 1.0 (18/11/2020)</summary>

The key and value of the `alienbabble` dictionary have been inverted.  
The values have been modified to refer directly to the methods related to the intent.  
The `alienbabble` dictionary has been renamed `intents`.

</details>

### To-do
The project will not be reworked.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate (if any).

## Contact
Created by [Dylan J. Gerrits](https://github.com/Dyrits).
