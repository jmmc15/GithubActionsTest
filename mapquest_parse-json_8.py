import urllib.parse
import requests
import colorama
from colorama import Fore, Back, Style

import unittest

colorama.init(autoreset=True)

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "NGO5fCSo59YyPyHEbC3q01BKlhM9knpU" 

while True:
    orig = input(Fore.CYAN + "Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input(Fore.CYAN + "Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    #define metrics input if KM / Liters or Miles /Gallons
    Metrics = input("What metrics do you choose? Press M for miles and gallons, Press K for kilometers and liters: ")
    if Metrics != "m" and Metrics != "k" and Metrics != "M" and Metrics != "K":
        print("Please choose either M or K")
        print("=============TERMINATING PROGRAM=============")
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print(Fore.GREEN + "URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print(Fore.GREEN + "API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print(Fore.BLUE + "Directions from " + (orig) + " to " + (dest))
        print(Fore.BLUE + "Trip Duration:   " + (json_data["route"]["formattedTime"]))
        #check user input for metrics choice
        if Metrics == "M" or Metrics == "m":
            print(Fore.BLUE + "Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        elif Metrics == "K" or Metrics == "k":  
            print(Fore.BLUE + "Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        # if Metrics == "M" or Metrics == "m":
        #     print(Fore.BLUE + "Fuel Used (Gal): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]))))
        # elif Metrics == "K" or Metrics == "k":
        #     print(Fore.BLUE + "Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        #function to check if there is toll road
        def myFunction(): 
            if json_data["route"]["hasSeasonalClosure"] == 1:
                return Fore.BLUE + "Yes"
            else:
                return Fore.BLUE + "No"
        print(Fore.BLUE + "Has Seasonal Closure:  ",myFunction())
        
        print("=============================================")
        #adding numbers for direction while checking metric choice
        count = 1
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            if Metrics == "M" or Metrics == "m":
                print(Fore.CYAN + str(count), ": ", end='')
                print((Fore.CYAN + each["narrative"]) + " (" + str("{:.2f}".format((each[ "distance"])) + " miles)"))
                count = count + 1
            elif Metrics == "K" or Metrics == "k":
                print(Fore.CYAN + str(count), ": ", end='')
                print((Fore.CYAN + each["narrative"]) + " (" + str("{:.2f}".format((each[ "distance"])*1.61) + " km)"))
                count = count + 1
        print("=============================================\n")
    #handling errors for MapQuest API
    elif json_status == 402:
        print("**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print(Fore.RED + "For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")