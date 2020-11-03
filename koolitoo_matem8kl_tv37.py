#Matemaatika TV 8. klassile ül 37

class_names = [
"kaspar",
"sigrid",
"chrisette",
"hanna",
"priscilla",
"kaito",
"sebastian",
"sandra",
"alice",
"mark",
"hermann",
"annabel",
"roland",
"sander",
"carmela",
"tuudur jakob",
"liisi",
"tuuli",
"dominik lukas",
"mia marleen",
"holger",
"victoria",
"mikk",
"salme",
"maksim",
"gustav paul",
"aurelia", 
"taavi",
"kertu olivia",
"rei helin",
"rasmus erich",
"robin"
]


class_names_short = [
"kaspar",
"sigrid",
"chrisette",
"hanna",
"priscilla",
"kaito",
"sebastian",
"sandra",
"alice",
"mark",
"hermann",
"annabel",
"roland",
"sander",
"carmela",
"tuudur",
"liisi",
"tuuli",
"dominik",
"mia",
"holger",
"victoria",
"mikk",
"salme",
"maksim",
"gustav",
"aurelia", 
"taavi",
"kertu",
"rei",
"rasmus",
"robin"
]

def get_longest_name(db):
    longest = []
    longest_int = 0
    for name in db:
        if len(name) >= longest_int:
            longest.append(name+"-"+"{}".format(len(name)))
            longest_int = len(name)
    print(longest_int, longest)



def getNumberForName(name, compare):
    n = 0
    letters = []
    new_name = list(name)
    new_compare = list(compare)
    for letter in new_name:
        if letter in new_compare:
            n+=1
            letters.append(letter)
            new_compare.remove(letter)
            print(list(new_compare))
    print(n, letters)      



def getNumber(name, database):
    number_list = []
    for compare in database:
        n = 0
        letters = []
        new_name = list(name)
        new_compare = list(compare)
        for letter in new_name:
            if letter in new_compare:
                n+=1
                letters.append(letter)
                new_compare.remove(letter)
        print(n, letters, compare)      
        number_list.append(n)
    print(sorted(number_list,key=int, reverse=True))


def who_has_the_best_tie():
    for name in class_names:
        print("Järgneb info õpilasele {}".format(name))
        getNumber(name, class_names)



    
name = input("Sisesta enda nimi: ")
db = input("Kasuta täispikki nimesid? (J/e) ")
if db == "e":
    getNumber(name.lower(), class_names_short)
else:
    getNumber(name.lower(), class_names)

