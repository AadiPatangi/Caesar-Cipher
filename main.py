#Caesar Cipher
#Aadi Patangi
#11/2/2021
#inspired by my CS Teacher

def encrypt(letter, shift):   #defining a function
  alphabet = ("abcdefghijklmnopqrstuvwxyz")   #creating a variable with all the lowercase letters
  letter = letter.lower() # making entered message lowercase
  if letter in alphabet:  #creating the loop inside the function
    index = alphabet.index(letter)   #index is the first letter of message and letter keeps incrementing so index will keep going through the message
    newPosition = (index + shift) % 26  # newPosition gives the new position of the original letter plus the shift
    newLetter = alphabet[newPosition]   #newletter gives whole message combined with the shift
    return newLetter #returning newLetter which is basically the shifted message
  else:
    return letter    #if special characters or anything not in the alphabet is inputed, return the input as it can not be encrypted
print("Welcome to the Caesar Cipher Program by Aadi 😃 ")   #introducing program
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # I added this just for neatness
message = input("Please give me a message: ")  # getting input message to be encrypted
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # I also added this just for neatness
shift = int(input("Please enter the shift: ")) #getting input on how much to shift
#print(encrypt(message[0], shift))      # calling the function encrypt and this prints the first character encrypted
#this print statement made the program print inneccessary stuff so i removed this, i also edited this program to my liking :)
secret = " "      #creating empty variable
for char in message:  # defining a variable char that is in message
  newLetter = encrypt(char, shift)    #newletter is the encrypted character
  secret = secret + newLetter   #emepty variable is "" + the ecrypted charcter and char keeps incrementing so at the end of the loop, secret ill be the encryped message
print("Encryption: " + secret)  #printing the encrypted message 