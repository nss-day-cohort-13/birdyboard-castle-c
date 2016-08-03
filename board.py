
import pickle
import sys
import uuid

class Board():

  def __init__(self):
    self.deserializeUser()
    self.uid = str(uuid.uuid4())





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
      self.user[self.uid] = dict()
      print("Create a New Account to get chirpy!.")
      inp1 = input("Enter screen name: ")
      self.user[self.uid]['username'] = inp1
      inp2 = input("Enter full name: ")
      self.user[self.uid]['fullname'] = inp2
      self.serializeUser()
      print(self.user)

    if user_choice == "2":
      self.deserializeUser()
      print("Select a User to chirp it up with!.")
      self.showUser()
      inp = input(">")
      userID = self.userSelect(inp)





    if user_choice == "3":
      self.deserializeChirp()
      print("Time to get chirpy! Select any chirp to get chirpin'.")
      print('>>>>>PUBLIC<<<<<')
      self.showPublicChirp()


    if user_choice == "4":
      self.deserializeChirp()
      self.chirp[self.uid] = dict()
      print("Send a new public chirp!")
      inp = input(">")
      self.chirp[self.uid]['chirp'] = inp
      self.chirp[self.uid]['uid'] = userID
      self.chirp[self.uid]['private'] = False
      self.chirp[self.uid]['recipient'] = None
      self.serializeChirp()
      print(self.chirp)


    if user_choice == "5":
      print("Send a new private chirp!")
      inp = input(">")


    if user_choice != "6":
      self.show_menu()



  def serializeChirp(self):
    with open('chirps.txt', 'wb+') as u:
      pickle.dump(self.chirp, u)

  def deserializeChirp(self):
    try:
      with open('chirps.txt', 'rb+') as u: #rb in read binary
        self.chirp = pickle.load(u)

    except EOFError:
      self.chirp = {}

    except FileNotFoundError:
      self.chirp = {}


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

  def showUser(self):
    u = self.user
    for k,v in u.items():
      print(v['username'])
      # return(v['username'])

  # def showFullName(self):


  def userSelect(self, inp):
    u = self.user
    for k,v in u.items():
      if inp == v['username']:
        return k

  def showPublicChirp(self):
    c = self.chirp
    for k,v in c.items():
      print(v['chirp'])


  # def testUserCreation(self, inp1, inp2):
    # tests to make sure user object has username and fullname keys and values
    # self.user[self.uid] = dict()
    # testUN = self.user[self.uid]['username'] = inp1
    # testFN = self.user[self.uid]['fullname'] = inp2
    # return testUN, testFN


  # def testChirpCreation(self, inp1, inp2, inp3):
    #tests to make sure the chirp object has chirp(message), private, recipient keys and values
    # self.chirp[self.uid] = dict()
    # testChirp = self.chirp[self.uid]['chirp'] = inp1
    # testPrivate = self.chirp[self.uid]['private'] = inp2
    # testRecipient = self.chirp[self.uid]['recipient'] = inp3
    # return testChirp, testPrivate, testRecipient



      # return list of usernames if username is selected send value to key in chirp

    # if user input equal to value being returned add ID  to ID key in chirp
    # if private is selected private equals true, if not false return value and add to private key in chirp
    # if users selects a reciepent return reciepent ID and add to reciepent key in chirp






if __name__ == '__main__':
  board = Board()
  board.show_menu()
