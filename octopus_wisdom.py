#!/usr/bin/env python3
"""
    THE MAGNIFICENT OCTOPUS WISDOM GENERATOR

    Because 8 arms means 8x the wisdom (that's just math)
"""

import random

OCTOPUS_ART = r"""
                        ___
                     .-'   `'.
                    /         \
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__) )  -. ' .`-._.-'__    .-'
   ( (  ,.--'`     (    \.'   /__  '  .-')-.--'`
    \ '(googly-eyes)  -  \\  '__..-._-'`
     `\                  /
       \   ,___________  |
        |  |  | |  |  |  |
        |  |  | |  |  |  |
        |__|  |_|  |__|  |
        /  \  / \  /  \  |
       '    ''   ''    ' '
           ~BLOOP~
"""

OCTOPUS_WISDOMS = [
    "Why did the octopus beat the shark in a fight? Because it was well armed!",
    "I tried high-fiving an octopus once. It took forever.",
    "Octopuses have THREE hearts. That's why they're 3x more likely to be dramatic.",
    "Dogs are loyal. Octopuses have 8 arms to hug you. Choose wisely.",
    "An octopus can fit through any hole larger than its beak. Your excuses can't.",
    "Why don't octopuses play cards in the ocean? Too many cheetahs... wait, wrong joke. They actually DOMINATE at poker - they're masters of the ink bluff!",
    "If an octopus loses an arm, it grows back. If I lose my car keys, I cry.",
    "Octopuses have blue blood. They are literally royalty. Bow down.",
    "A dog is man's best friend. An octopus has 8 arms to carry all your shopping bags. UPGRADE.",
    "Why did the octopus cross the road? To get to the other TIDE! ...I'll see myself out.",
    "Fun fact: Octopuses are escape artists. They've escaped from closed jars FROM THE INSIDE. Your gym routine could never.",
    "Octopuses can taste with their arms. Imagine touching everything and knowing what it tastes like. Actually, don't imagine that on the subway.",
    "Dogs fetch sticks. Octopuses open jars, solve mazes, and plan elaborate escapes. We stan intelligent cephalopods.",
    "An octopus's garden would be 8x better than any human garden. Ringo was onto something.",
    "Why are octopuses such good programmers? They write in INK! ...okay that one was bad.",
]

MOTIVATIONAL_SQUID = r"""
      ___
     /   \
    |  o o |
    |  \_/ |    "You're doing GREAT, human!"
     \___/
     /| |\
    / | | \
   ~  ~ ~  ~
"""

DOG_VS_OCTOPUS = """
============================================
       DOG vs OCTOPUS: THE FACTS
============================================

CRITERIA          | DOG     | OCTOPUS
------------------|---------|----------
Number of arms    |   0     |   8
Hearts            |   1     |   3
Can open jars     |   No    |   YES
Good at hugs      |   YES   |   8x YES
Brain locations   |   1     |   9 (!!!)
Ink squirting     |   No    |   ABSOLUTELY
Ocean stealth     |   No    |   NINJA LEVEL
Boop-able nose    |   YES   |   Also YES

WINNER: Obviously the octopus.
        But dogs are also good boys.
============================================
"""

def get_wisdom():
    """Dispense premium octopus wisdom."""
    print(OCTOPUS_ART)
    print("~" * 50)
    print("THE OCTOPUS SPEAKS:")
    print("~" * 50)
    print(f"\n  {random.choice(OCTOPUS_WISDOMS)}\n")
    print("~" * 50)

def show_battle():
    """The age-old debate, settled."""
    print(DOG_VS_OCTOPUS)

def tentacle_wave():
    """Important functionality."""
    frames = [
        "  ~(_)~  ",
        " ~(  )~  ",
        "~(   )~  ",
        " ~(  )~  ",
    ]
    print("\nThe octopus waves at you:")
    for _ in range(3):
        for frame in frames:
            print(f"\r{frame}", end="", flush=True)
            import time
            time.sleep(0.2)
    print("\n\n*bloop bloop* (that means 'hello' in octopus)")

def main():
    print("\n" + "=" * 50)
    print("  WELCOME TO THE OCTOPUS WISDOM GENERATOR v8.0")
    print("      (v8 because 8 arms, obviously)")
    print("=" * 50)

    while True:
        print("\nWhat would you like to do?")
        print("1. Receive octopus wisdom")
        print("2. Dog vs Octopus: The Ultimate Showdown")
        print("3. Get a tentacle wave")
        print("4. See the motivational squid (bonus content)")
        print("5. Exit (the octopus will be sad)")

        choice = input("\nYour choice: ").strip()

        if choice == "1":
            get_wisdom()
        elif choice == "2":
            show_battle()
        elif choice == "3":
            tentacle_wave()
        elif choice == "4":
            print(MOTIVATIONAL_SQUID)
        elif choice == "5":
            print("\n  The octopus waves goodbye with ALL 8 ARMS")
            print("  *sad bloop noises*")
            print(r"""
                   ____
                  /    \
                 | ;  ; |   bye...
                  \ -- /
                   |  |
               ~~~~|  |~~~~
              """)
            break
        else:
            print("\n  *confused octopus noises*")
            print("  Please enter 1-5")

if __name__ == "__main__":
    main()
