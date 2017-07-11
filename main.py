# For default user the app import the details from spy_details.py
from spy_details import spy, Spy, ChatMessage, friends
# importing steganography
from steganography.steganography import Steganography
# importing datetime
from datetime import datetime

# Status message for Bishop
STATUS_MESSAGES = ['My name is Bishop', 'Bishop, the Superhero.', 'X-Men, Team of legends']

# Printing Hello and starting the SpyChat
print "Hello! Let\'s get started"

# Do you want to continue with the default user or create their own
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


def add_status():

    updated_status_message = None

    # If the user selects the option to add a status the app should display the current status message
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    # The app ask the user if they want to choose from the older status updates or create a new status update
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    # If the user wants to select from the older status updates, show him the same and get the user input.
    elif default.upper() == 'Y':

        # After the user selects from the older status updates set it as the current one
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:

            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:

        # print updated status message
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

# function add_friend to handle the case when user selects to add a friend
def add_friend():
    # The function should ask the user for the name, age and rating of their spy friend
    new_friend = Spy('','',0,0.0)

    # The function converts the data as appropriate
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    # The function should add the friend to various lists only if name is not empty, age is greater than 12 and rating of the friend spy is greater than or equal to the user spy rating.
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    # If any of the above conditions are not met it displays an appropirate message
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    # The function should return and print the number of friends the user has
    return len(friends)

# A method called select_a_friend to choose from the list of spy friends added by the user.
def select_a_friend():
    item_number = 0

    # The method print out all the friends of the user
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name, friend.age, friend.rating)
        item_number = item_number + 1

    # The user is asked to select from one of the friends
    friend_choice = raw_input("Choose from your friends")

    # The method return the index of the selected friend
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

# Method called send_message. It should call the select_a_friend method to get which friend is to be communicated with.
def send_message():

    friend_choice = select_a_friend()

    # Ask the user for the name of the image they want to encode the secret message with
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"

    # Ask the user for the secret message they want to hide.
    text = raw_input("What do you want to hide? ")

    # Using the Steganography library hide the message inside the image.
    Steganography.encode('images.jpg', output_path, text)

    new_chat = ChatMessage(text, True)

    # Append the chat message to 'chats' key for the friends list.
    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"

# Write a method called read_message. It should call the select_a_friend method to get which friend is to be communicated with.
def read_message():

    sender = select_a_friend()
    # Ask the user for the name of the image they want to decode the message from.
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    # Append the chat dictionary to chats key for the particular friend.
    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

# A method to read the entire chat history of a particular friend.
def read_chat_history():

    #  It call select_a_friend method to get which friend is to be communicated with.
    read_for = select_a_friend()

    # It should print the chat history for that particular friend
    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    # The age of the user is greater than 12 and less than 50
    if spy.age > 12 and spy.age < 50:

        # an appropriate final welcome message with the name, salutation, age and rating of the spy.
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        # The app display a menu with following choices: 1) Add a status update 2) Add a friend 3) Send a secret message 4) Read a secret message 5) Read chats from a user 6) Close application

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()

                # The menu should be displayed until the user chooses the menu option to Close the application
                else:
                    show_menu = False
    # if condition not satisfied then it should display an appropriate message and exit.
    else:
        print 'Sorry you are not of the correct age to be a spy'

        if existing == "Y":
    start_chat(spy)
elif existing == "N":

    spy = Spy('','',0,0.0)

# For custom user app ask for the name of the user
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if (spy.name).isalpha() == True:

        # The app ask for the salutaion the user wants to be used in front of their name.
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        # Ask the user for their age and convert it to integer type
        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)
        if spy.age > 12 and spy.age < 50:

            # Ask the user for their rating and convert it to float
            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)

            # Based on spy rating it displays an appropriate message using at least one if, elif and else sequence
            if spy.rating > 4.5:
                print 'Great going!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'Do better'
            else:
                print 'We can always use somebody to help in the office.'
            start_chat(spy)
        else:
            print 'Sorry you are not of the correct age to be a spy'
    # If user has entered an invalid name as input then it display a warning message and finish execution
    else:
        print 'Please add a valid and appropriate spy name'
else:
    print "Wrong input! The program will terminate now."

