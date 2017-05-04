for x in range(0,100):
    if x % 5 == 0:
        message = "%s is divisible by 5."
        print(message % x)

#integer variables
x = 20

#string variables
text = "I like coding."

#lists
groceries = ["apples", "bananas", "milk", "eggs"]

#boolean variables
#These can be set to equal True or False

#wearingHat = False
#wearingBlack = True

#print(wearingHat)


print("Is it raining today?")

#Evaluator not cooperating
#Continue here next week

#userInput = str(input())
#goodWeather = string
#if userInput == "yes" or "Yes" or "y" or "Y":
#    goodWeather = True
#elif userInput == "No" or "no" or "n" or "N":
#    goodWeather = False
#else:
#    print("...")

#if goodWeather is True:
#    print("You should take an umbrella with you today.")
#elif goodWeather is False:
#    print("You don't need to lug an umbrella around.")
#else:
#    print("I don't know what you mean.")
print("Enter a 1 for yes and a 0 for no")
userInput = int(input())
if userInput == 1:
    goodWeather = True
    print("Better take an umbrella")
elif userInput == 0:
    goodWeather = False
    print("No need for an umbrella")
#The above works, therefore, the issue must have something to do
#with using a string to get a user input vs a number to relate
#the boolean variable goodWeather to
