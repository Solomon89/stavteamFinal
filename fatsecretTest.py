
clientID = 'cbf61802962b4846a6b493d8cac33880'
clientSecret = '5e03859dd82543c891331a172c630d7f'

from fatsecret import Fatsecret

fs = Fatsecret(clientID, clientSecret)

auth_url = fs.get_authorize_url()

print("Browse to the following URL in your browser to authorize access:\n{}".format(auth_url))

pin = input("Enter the PIN provided by FatSecret: ")
session_token = fs.authenticate(pin)

foods = fs.foods_get_most_eaten()
print("Most Eaten Food Results: {}".format(len(foods)))