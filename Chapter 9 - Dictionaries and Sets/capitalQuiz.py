'''
Capital Quiz
'''
import random as r

def grader(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
def capital():
    # Dictionary containing the US states as keys, and capitals as values
    dct_states = {1:"Alabama", 2:"Alaska", 3:"Arizona", 4:"Arkansas", 5:"California", 6:"Colorado", 7:"Connecticut", 8:"Delaware",
                9:"Florida", 10:"Georgia", 11:"Hawaii", 12:"Idaho", 13:"Illinois", 14:"Indiana", 15:"Iowa", 16:"Kansas",
                17:"Kentucky", 18:"Lousiana", 19:"Maine", 20:"Maryland", 21:"Massachusetts", 22:"Michigan", 23:"Minnesota",
                24:"Mississippi", 25:"Missouri", 26:"Montana", 27:"Nebraska", 28:"Nevada", 29:"New Hampshire", 30:"New Jersey", 31:"New Mexico",
                32:"New York", 33:"North Carolina", 34:"North Dakota", 35:"Ohio", 36:"Oklahoma", 37:"Oregon", 38:"Pennsylvania", 39:"Rhode Island",
                40:"South Carolina", 41:"South Dakota", 42:"Tennessee", 43:"Texas", 44:"Utah", 45:"Vermont", 46:"Virginia", 47:"Washington",
                48:"West Virginia", 49:"Wisconsin", 50:"Wyoming"}

    dct_capital = {1:"Montgomery", 2:"Juneau", 3:"Phoenix", 4:"Little Rock", 5:"Sacramento", 6:"Denver", 7:"Hartford", 8:"Dover",
                9:"Tallahassee", 10:"Atlanta", 11:"Honolulu", 12:"Boise", 13:"Springfield", 14:"Indianapolis", 15:"Des Moines", 16:"Topeka",
                17:"Frankfort", 18:"Baton Rouge", 19:"Augusta", 20:"Annapolis", 21:"Boston", 22:"Lansing", 23:"Saint Paul", 24:"Jackson",
                25:"Jefferson City", 26:"Helena", 27:"Lincoln", 28:"Carson City", 29:"Concord", 30:"Trenton", 31:"Santa Fe", 32:"Albany",
                33:"Raleigh", 34:"Bismarck", 35:"Columbus", 36:"Oklahoma City", 37:"Salem", 38:"Harrisburg", 39:"Providence", 40:"Columbia",
                41:"Pierre", 42:"Nashville", 43:"Austin", 44:"Salt Lake City", 45:"Montpelier", 46:"Richmond", 47:"Olympia", 48:"Charleston", 
                49:"Madison", 50:"Cheyenne"}

    # Get user input
    qtty_question = 0
    correct_answer = 0
    invalid_answer = 0

    while True:
        randomNum = r.randint(1, 50)
        user_answer = input(f"\nEnter the capital of {dct_states[randomNum]}: (0 to end) ")
        qtty_question += 1
        if user_answer == dct_capital[randomNum]:
            print("You got it right!")
            correct_answer += 1
        elif user_answer == "0":
            break
        else:
            print(f"Sorry pal! That's not right. The correct answer is {dct_capital[randomNum]} ")
            invalid_answer += 1
    percentage = correct_answer / qtty_question * 100
    grade = grader(percentage)

    print(f"You answered {qtty_question} and got {correct_answer} correct answers. That's {percentage:,2f} of the quiz.\nYou grade is {grade}")
    
def countries ():
    qtty_question = 0
    correct_answer = 0
    invalid_answer = 0
        
    dct_countries = {    "United States of America": "North America", "Canada": "North America","Mexico": "North America",
    "Panama": "South America", "Brazil": "South America", "Bolivia": "South America", "Argentina": "South America", "Ecuador": "South America",
    "Chile": "South America", "Russia": "Europe", "France": "Europe", "Germany": "Europe", "United Kingdom": "Europe", "Italy": "Europe",
    "China": "Asia", "India": "Asia", "Japan": "Asia", "Australia": "Australia", "New Zealand": "Australia", "South Africa": "Africa",
    "Egypt": "Africa", "Nigeria": "Africa", "Kenya": "Africa", "Morocco": "Africa", "Ghana": "Africa", "Saudi Arabia": "Asia",
    "Vietnam": "Asia", "South Korea": "Asia", "Greece": "Europe", "Jamaica": "North America", "Cuba": "North America", "Honduras": "North America",
    "Peru": "South America", "Spain": "Europe", "Philippines": "Asia", "Indonesia": "Asia", "Netherlands": "Europe", "Switzerland": "Europe",
    "Sweden": "Europe", "Norway": "Europe", "Guatemala": "North America", "Costa Rica": "North America", "Belize": "North America", "Venezuela": "South America",
    "Colombia": "South America", "Paraguay": "South America", "Uruguay": "South America", "Bahrain": "Asia", "Qatar": "Asia", "Thailand": "Asia",
    "Turkey": "Asia", "Iran": "Asia", "Iraq": "Asia", "Pakistan": "Asia", "Bangladesh": "Asia", "Afghanistan": "Asia", "South Sudan": "Africa",
    "Kenya": "Africa", "Ethiopia": "Africa", "Uganda": "Africa", "Rwanda": "Africa", "Tanzania": "Africa", "Spain": "Europe", "Portugal": "Europe",
    "Poland": "Europe", "Austria": "Europe", "Ireland": "Europe", "Switzerland": "Europe", "Belgium": "Europe", "Netherlands": "Europe", "Denmark": "Europe",
    "Norway": "Europe", "Sweden": "Europe", "Finland": "Europe", "Greece": "Europe", "Ukraine": "Europe", "Romania": "Europe", "Hungary": "Europe",
    "Bulgaria": "Europe", "Czech Republic": "Europe", "Slovakia": "Europe", "Serbia": "Europe", "Croatia": "Europe", "Slovenia": "Europe", "Bosnia and Herzegovina": "Europe",
    "Montenegro": "Europe", "Macedonia": "Europe", "Albania": "Europe", "Kosovo": "Europe", "Latvia": "Europe", "Lithuania": "Europe", "Estonia": "Europe",
    "Iceland": "Europe", "Mongolia": "Asia", "Kazakhstan": "Asia", "Uzbekistan": "Asia", "Tajikistan": "Asia", "Kyrgyzstan": "Asia", "Turkmenistan": "Asia",
    "Jordan": "Asia", "Lebanon": "Asia", "Israel": "Asia", "Palestine": "Asia", "Syria": "Asia", "Cyprus": "Asia", "Gaza Strip": "Asia", "West Bank": "Asia",
    "Yemen": "Asia", "Oman": "Asia", "United Arab Emirates": "Asia", "Saudi Arabia": "Asia", "Qatar": "Asia", "Kuwait": "Asia", "Iraq": "Asia",
    "Iran": "Asia", "Pakistan": "Asia", "Afghanistan": "Asia", "India": "Asia", "Nepal": "Asia", "Sri Lanka": "Asia", "Maldives": "Asia", "Bhutan": "Asia",
    "South Korea": "Asia", "North Korea": "Asia", "Mongolia": "Asia", "Japan": "Asia", "Bangladesh": "Asia", "Myanmar": "Asia", "Laos": "Asia",
    "Vietnam": "Asia", "Cambodia": "Asia", "Thailand": "Asia", "Malaysia": "Asia", "Singapore": "Asia", "Brunei": "Asia", "Timor-Leste": "Asia",
    "Philippines": "Asia", "Indonesia": "Asia", "Papua New Guinea": "Australia", "Fiji": "Australia", "Solomon Islands": "Australia", "New Zealand": "Australia",
    "South Africa": "Africa", "Zimbabwe": "Africa", "Zambia": "Africa", "Botswana": "Africa", "Mozambique": "Africa",
    "Madagascar": "Africa", "Angola": "Africa", "Congo": "Africa", "Cameroon": "Africa", "Central African Republic": "Africa",}
        
    
    while True:
        country, continent  = r.choice(list(dct_countries.items()))

        user_answer = input(f"\nEnter in which continent {country} is: (0 to end) ")
        qtty_question += 1
        if user_answer == continent:
            print("You got it right!")
            correct_answer += 1
        elif user_answer == "0":
            break
        else:
            print(f"Sorry pal! That's not right. The correct answer is {continent} ")
            invalid_answer += 1
    
    percentage = correct_answer / qtty_question * 100
    grade = grader(percentage)

    print(f"You answered {qtty_question} and got {correct_answer} correct answers. That's {percentage:2f} of the quiz. \nYou grade is {grade}")

def main():
    print("\t *** WELCOME TO GABRIEL'S GEOGRAPHY QUIZ! ***")
    print("Are you ready to have your continents, countries, and capitals knowlegde tested?")
    print("Wait no more! Get your map ready (If you are allowed to, of course)")
    print("\t 1. To find where the country is located")
    print("\t 2. To find where the capital is located")
    
    while True:
        try:
            user_input = int(input("Which would you like to start with?(0 to cancel): "))
            if user_input == 0:
                exit()
            elif user_input == 1:
                countries()
                break
            elif user_input == 2:
                capital()
                break
            else:
                user_input = int(input("Invalid Input. Try again!: "))
        except ValueError as err:
            print(err, "You must enter an integer number.")
        else:
            print("Starting your quiz in 3...2...1...\n")

if __name__ == "__main__":
    main()