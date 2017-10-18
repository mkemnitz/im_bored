import random

def open_and_read_file(filename):
    """Opens filename as a file object and returns list of contents."""
    
    file_class = open(filename)
    file_list = file_class.read().split("\n")
    file_class.close()
    
    return file_list

def greet_user():
    """Prints intro greeting"""
    print
    print "I heard you were bored."
    print
    print "I'm here to help!"
    print
    print "What is your age?"
    print
    

def age_input(message):
    """Forces user to enter number"""
    try:
      age = int(raw_input(message))
      return age
    except:
      return age_input("Enter a number: ")

def generate_suggestion():
    """Generates suggestion based on user age"""
    age = age_input("Enter age: ")
    if age <= 5:
        age_5_younger = open_and_read_file("age_5_younger.txt")
        print "Why don't you {}?".format(random.choice(age_5_younger))
        print

    elif (age > 5) and (age < 20):
        age_5_to_20 = open_and_read_file("age_5_to_20.txt")
        print "Why don't you {}?".format(random.choice(age_5_to_20))
        print

    elif age >= 20:
        age_20_plus = open_and_read_file("age_20_plus.txt")
        print "Why don't you {}?".format(random.choice(age_20_plus))
        print
    
def ask_to_continue():
    """Ask user to continue"""

    bored = raw_input("Do you want another suggestion?(yes/no) ").lower()

    if bored == 'no':
        print
        print "Great have fun!"
        return False

    return True
    
def run_im_bored():
    """Runs the i'm bored game"""
    
    greet_user()
    
    bored = True
    
    while bored:
        generate_suggestion()
        bored = ask_to_continue()

run_im_bored()
