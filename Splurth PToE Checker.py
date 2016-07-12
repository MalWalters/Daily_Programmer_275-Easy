elements = open("Splurth PToE.txt").read().split()

def isValidSymbol(elementName, symbol):
    result = "True"
    # Check to see if both charcters of the Symbol are in the element name
    for char in symbol:
        if elementName.lower().find(char.lower()) == -1:
            return "False: " + char + " is not in " + elementName
    # Check order of letters in Symbol within element
    if elementName.lower().index(symbol[:1].lower()) > elementName.lower().rfind(symbol[-1:].lower()):
        result = "False"
    return result

for i in elements:
    print(i.split(",")[0] + ", " + i.split(",")[1] + " -> " + isValidSymbol(i.split(",")[0],i.split(",")[1]))
    
