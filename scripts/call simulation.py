# call-simulation.py

import time

def call_scenario():
    print("You receive a phone call from someone claiming to be your company's IT support:")
    time.sleep(1)
    print("\n*** Call Transcript ***")
    print("IT Support: Hello, this is IT support. We noticed unusual activity in your account. Please confirm your username and password.")
    time.sleep(2)
    
    response = input("\nDo you give them your password? (yes/no): ").lower()
    
    if response == "yes":
        print("\nYou've fallen for a pretexting attack! The caller was not really from IT.")
    else:
        print("\nGreat! You did not fall for the attack.")

if __name__ == "_main_":
    call_scenario()