
import pickle
import sys
import uuid

class Board():

  def __init__(self):
    # self.user = {}
    # # self.chirps = {}
    # self.chirps = self.deserializeChirps()
    # self.user = self.deserializeUser()
    uid = str(uuid.uuid4())



  def show_menu(self):
    global userID
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
      self.user[uid] = dict()
      print("Create a New Account to get chirpy!.")
      inp1 = input("Enter screen name: ")
      self.user[uid]['username'] = inp1
      inp2 = input("Enter full name: ")
      self.user[uid]['fullname'] = inp2
      self.serializeUser()
      print(self.user)



    if user_choice == "2":
      self.deserializeUser()
      print("Select a User to chirp it up with!.")
      self.showUser()
      inp3 = input(">")
      userID = self.addUserID(inp3)
      print(userID)



    if user_choice == "3":
      self.deserializeChirps()
      print("Time to get chirpy! Select any chirp to get chirpin'.")
      print('>>>>>PUBLIC<<<<<')
      self.showAllPublicChirps()
      print('>>>>>PRIVATE<<<<<')
      self.showAllPrivateChirps()



    if user_choice == "4":
      self.deserializeChirps()
      uid = str(uuid.uuid4())
      self.chirps[uid] = dict()
      print("Write a new public chirp!")
      inp4 = input(">")
      self.chirps[uid]['chirp'] = inp4
      self.chirps[uid]['uid'] = userID
      self.chirps[uid]['private'] = False
      self.chirps[uid]['recipient'] = None
      self.serializeChirp()
      print(self.chirps)



    if user_choice == "5":
      self.deserializeChirps()
      uid = str(uuid.uuid4())
      self.chirps[uid] = dict()
      print("Write a new private chirp!")
      inp5 = input(">")
      self.chirps[uid]['chirp'] = inp5
      self.chirps[uid]['uid'] = userID
      self.chirps[uid]['private'] = True
      print("Who you chirpin at?")
      self.showUser()
      inp6 = input(">")
      userID = self.addUserID(inp6)
      self.chirps[uid]['recipient'] = userID
      self.serializeChirp()
      print(self.chirps)



    if user_choice != "6":
      self.show_menu()



  def serializeChirp(self):
    with open('chirps.txt', 'wb+') as u:
      pickle.dump(self.chirps, u)

  def deserializeChirps(self):
    try:
      with open('chirps.txt', 'rb+') as u: #rb in read binary
        self.chirps = pickle.load(u)

    except EOFError:
      self.chirps = {}

    except FileNotFoundError:
      self.chirps = {}


      return self.chirps



  def serializeUser(self):
    with open('userData.txt', 'wb+') as u:
      pickle.dump(self.user, u)

  def deserializeUser(self):
    try:
      with open('userData.txt', 'rb+') as u: #rb in read binary
        self.user = pickle.load(u)

    except EOFError:
      self.user = {}

    except FileNotFoundError:
      self.user = {}

      return self.user



  def showUser(self):
    u = self.user
    for k,v in u.items():
      print(v['username'])



  def addUserID(self, inp):
    u = self.user
    for k,v in u.items():
      if inp == v['username']:
        return k

  def showAllPublicChirps(self):
    c = self.chirps
    for k,v in c.items():
      if v['private'] == False:
       print(v['chirp'])

  def showAllPrivateChirps(self):
    c = self.chirps
    for k,v in c.items():
      if v['private'] == True:
       print(v['chirp'])

  # def showAllChirps(self):
  #   c = self.chirps
  #   for k,v in c.items():

  #     print(v['chirp'])


# Chirps are separated into public and private chirps.
#  Only the two users involved in a private chirp can
#   see it in their Private Chirps section.



#when a chirp is selected it takes you to that chirp's comment thread.
#Tweedleedee: Anybody know a good Thai restaraunt in the area?
# Fuzzy: Smiling Elephant is really good
# BiffBoffin: The pad krapow is amazing!
# ...
# 1. Reply
# 2. Back
# >



if __name__ == '__main__':
  board = Board()
  board.show_menu()
