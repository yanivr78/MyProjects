# Beginning
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9995'

# We will store the regular expression method in a normal pattern with r, and we will search for
# digit digit digit - digit digit digit - digit digit digit digit
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# We will then use a search method for searching a string with the pattern above and will store it in mo (matched object)
mo = phoneNumRegex.search(message)
# Will print the matched number
print("The first occurrence: ", mo.group())

# Now we will print all of the occurrences
# by using findall
print("All occurrences: ", phoneNumRegex.findall(message))