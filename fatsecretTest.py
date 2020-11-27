from fatsecret import Fatsecret

clientID = 'cbf61802962b4846a6b493d8cac33880'
clientSecret = '624f154d6b5d4a5581cafd0312996927'

fs = Fatsecret(clientID, clientSecret)

auth_url = fs.get_authorize_url()

print("Browse to the following URL in your browser to authorize access:\n{}".format(auth_url))

pin = input("Enter the PIN provided by FatSecret: ")
session_token = fs.authenticate(pin)

foods = fs.profile_get()
print(foods)