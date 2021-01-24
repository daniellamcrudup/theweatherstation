
def weather_report():

    print("Here are some simple explanations of the weather.")
    print("If the weather is sunshine, you may be feeling happy, excited, or joyful.")
    print("If the weather is rain, you may be feeling sad, tired, or upset.")
    print("If the weather is clouds, you may be feeling anxious, nervous, or worried.")
    print("If the weather is hail, you may be feeling angry, irritated, or annoyed.")
    print("...")
    print("So, what's the weather today?")
    weather = input("Sunshine, rain, clouds, or hail? ")
    print("...")
    if weather.lower() == "sunshine" :
        print("The weather is sunny?")
        print("That's great!")
        print("Express how you're feeling through art or music!")
    elif weather.lower() == "rain" :
        print("The weather is rainy?")
        print("I'm sorry to hear that.")
        print("Make time to do something you enjoy, like reading a book!")
    elif weather.lower() == "clouds" :
        print("The weather is cloudy?")
        print("I'm sorry to hear that.")
        print("Talk about your feelings with a trusted adult.")
    elif weather.lower() ==  "hail" :
        print("The weather is hailing?")
        print("I'm sorry to hear that.")
        print("Maybe try writing how you feel on a piece of paper, and then ripping the paper up!")


if __name__ == '__main__':
    print("This is a simple mood check-in for children.")
    print("Adult supervision is recommended.")
    print("...")

    print("Welcome to the weather station!")
    print("You must be our new assistant!")
    name = input("What's your name? ")
    print("...")
    print("Well, hello, " + name + "! Let's start the weather report!")
    print("...")  

    weather_report() 
    print("...")    

    checkin = input("How do you feel now? ")
    checkin = checkin.lower()
    print("You feel " + checkin + "?")
    print("No matter how you feel, it's important to acknowledge your feelings.")
    print("Thank you for talking about your feelings and reporting the weather with me!")
    close=input("You may now exit.") 
