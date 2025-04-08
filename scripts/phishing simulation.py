
import time

def phishing_scenario():
    print("You have received an email from what looks like your bank:")
    time.sleep(1)
    print("\n*** Email ***")
    print("From: support@yourbank.com")
    print("Subject: Immediate Action Required - Verify Your Account Now!")
    print("Message: Please click the link below to verify your account and prevent it from being suspended.")
    time.sleep(2)
    
    response = input("\nDo you click the link? (yes/no): ").lower()
    
    if response == "yes":
        print("\nYou've been phished! The link took you to a fake website.")
    else:
        print("\nGood choice! You did not fall for the phishing attempt.")

if __name__ == "_main_":
    phishing_scenario()