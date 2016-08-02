import pickle
import sys
import uuid

class Board():

  def __init__(self):
    self.uData = {}
    self.chirpData = {}


  def show_menu(self):

    print('what would you like to do?')
    print("1. New User Account")
    print("2. Select User")
    print("3. View Chirps")
    print("4. Public Chirp")
    print("5. Private Chirp")
    print("6. Exit")
    user_choice = input(">")

    if user_choice == "1":
      self.deserializeUser()
      print("Create a New Account to get chirpy!.")
      inp1 = input("Enter screen name: " )
      self.uData.setdefault("username:", []).append(inp1)
      inp2 = input("Enter full name: ")
      self.uData.setdefault("fullname:", []).append(inp2)
      self.uData.setdefault("ID:", []).append(uuid.uuid4())
      self.serializeUser()
      print(self.uData)

    if user_choice == "2":
      self.deserializeUser()
      print("Select a User to chirp it up with!.")
      self.usernameSelect()
      inp = int(input(">"))
      self.loadUser(inp)




    # if user_choice == "3":
    #   print("Time to get chirpy! Select any chirp to get chirpin'.")
    #   inp = input(">")


    # if user_choice == "4":
    #   print("Send a new public chirp!")
    #   inp = input(">")


    # if user_choice == "5":
    #   print("Send a new private chirp!")
    #   inp = input(">")


    # if user_choice != "6":
    #   self.show_menu()
  # def serializeChirp(self):
  #   with open('chirps.txt', 'wb+') as u:
  #     pickle.dump(self.chirpData, u)

  # def deserializeChirp(self):
  # try:
  #   with open('chirps.txt', 'rb+') as u: #rb in read binary
  #     self.chirpData = pickle.load(u)

  # except: EOFError


  def serializeUser(self):
    with open('userData.txt', 'wb+') as u:
      pickle.dump(self.uData, u)

  def deserializeUser(self):
    try:
      with open('userData.txt', 'rb+') as u: #rb in read binary
        self.uData = pickle.load(u)

    except: EOFError

  def usernameSelect(self):
    d = self.uData
    users = d['username:']
    for k, v in enumerate(users, start = 1):
      print(k,v)
      return (k,v)

  def fullnameSelect(self):
    newL = []
    d = self.uData
    users = d['fullname:']
    for k, v in enumerate(users, start = 1):
      print (k,v)
      return (k,v)


  # def loadUser(self, inp):
  #   d = self.uData
  #   users = d['username:']
  #   for k, v in enumerate(users, start = 1):
  #     if k == inp:
  #       return k
  #       print('hi')



if __name__ == '__main__':
  board = Board()
  board.show_menu()
