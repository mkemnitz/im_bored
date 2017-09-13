import random
# This is a program that will suggest activities to do when you're bored.
print
print "I heard you were bored."
print
print "I'm here to help!"
print
print "What is your name?"

#Ask name

name = raw_input(">>")

print
print "Hello {}! How old are you?".format(name)

#Ask age

def age_input(message):
   try:
      age = int(input(message))
      return age
   except:
      return age_input("Enter a number: ")

age = age_input("Enter age: ")

print
print "Ok, I see you are {} years old.".format(age)
print
print "I'm trying to think of something you might like to do..."
print

# Lists of activities by age

age_5_younger = ["play with legos", "paint", "ride your scooter",
                "read a picture book", "draw a picture of mommy"]
age_5_to_20 = ["read a book", "paint a picture", "ride your bike", "jump rope",
                "draw a picture of dragon"]
age_20_plus = ["do some knitting", "paint with watercolors", "go for a bike ride", "yoga"]

# Random choice of the lists of activiites by age

rand_item5 = random.choice(age_5_younger)
rand_item_5_to_20 = random.choice(age_5_to_20)
rand_item_20 = random.choice(age_20_plus)

#Determine which list to choose by age and provide to user

if age <= 5:
    print "Why don't you {}?".format(rand_item5)
    # del age_5_younger
    # print age_5_younger

elif (age > 5) and (age < 20):
    print "Why don't you {}?".format(rand_item_5_to_20)

elif age >= 20:
    print "Why don't you {}?".format(rand_item_20)

print

# Ask user if they like that option and if not, provide another

user_still_bored = True

while user_still_bored:
    print "Do you like that option?  Type y or n"
    user_likes = raw_input(">>")

    if user_likes == "y":
        print "Great, have fun!"
        user_still_bored = False
    elif user_likes == "n":
        print "Ok let's give you another option"
    else:
        print "Please type y or n"
