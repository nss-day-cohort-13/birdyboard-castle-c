
import pickle
import sys
import uuid

class Board():

  def __init__(self):
    self.chirpData = {}
    self.deserializeUser()





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
      uid = str(uuid.uuid4())
      self.users[uid] = dict()
      print("Create a New Account to get chirpy!.")
      inp1 = input("Enter screen name: " )
      self.users[uid]['username'] = inp1
      inp2 = input("Enter full name: ")
      self.users[uid]['fullname'] = inp2
      self.serializeUser()
      print(self.users)

    if user_choice == "2":
      self.deserializeUser()
      print("Select a User to chirp it up with!.")
      print(self.userSelect())
      inp = int(input(">"))





    if user_choice == "3":
      print("Time to get chirpy! Select any chirp to get chirpin'.")
      inp = input(">")


    if user_choice == "4":
      print("Send a new public chirp!")
      inp = input(">")


    if user_choice == "5":
      print("Send a new private chirp!")
      inp = input(">")


    if user_choice != "6":
      self.show_menu()



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
      pickle.dump(self.users, u)

  def deserializeUser(self):
    try:
      with open('userData.txt', 'rb+') as u: #rb in read binary
        self.users = pickle.load(u)

    except EOFError:
      self.users = {}

    except FileNotFoundError:
      self.users = {}

  def userSelect(self):
    d = self.users
    for key, value in d.items():
      return d





if __name__ == '__main__':
  board = Board()
  board.show_menu()
