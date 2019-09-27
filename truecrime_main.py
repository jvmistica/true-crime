from elastic import *


def display_prompt():
    print("\n----- OPTIONS -----")
    print("   v - view all")
    print("   s - search\n")
    
    return input("Option:").lower()

def display_result(result):
    for ndx, val in enumerate(result):
        print("\n----------\n")
        print("Story", ndx + 1, "of", val.get("total"))
        print("Subject:", val.get("subject"))
        print(val.get("story"))

def display_search():
    print("\n----- SEARCH -----")
    print("    s - search by story source")
    print("    n - search by subject name")
    print("    p - search for phrase(s) in stories\n")

    search = input("Search:").lower()
    if search == "s":
        search_term = input("Story Source:")
        display_result(es_search(source=search_term))
    elif search == "n":
        search_term = input("Subject Name:")
        display_result(es_search(subject=search_term))
    elif search == "p":
        search_term = input("Phrase(s) in Stories:")
        display_result(es_search(story=search_term))
    else:
        print("\nInvalid search option. Please try again.")
        display_search()


option = display_prompt()
if option == "v":
    display_result(es_search())
elif option == "s":
    display_search()
else:
    print("\nInvalid option. Please try again.\n")
    display_prompt()
