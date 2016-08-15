
import pickle
import sys
import uuid
from serial import *
from collections import OrderedDict

class Board():

  def __init__(self):
    self.users = []
    self.chirps = []
    self.convos = []
    # self.chirps = deserializeChirps(self)
    # self.user = self.deserializeUser()
    # uid = str(uuid.uuid4())



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
      global userID
      deserializeUsers(self)
      user = dict()
      uid = str(uuid.uuid4())
      user[uid] = dict()
      print("Create a New Account to get chirpy!.")
      inp1 = input("Enter screen name: ")
      user[uid]['username'] = inp1
      inp2 = input("Enter full name: ")
      user[uid]['fullname'] = inp2
      self.users.append(user)
      serializeUsers(self)
      print(self.users)



    if user_choice == "2":
      deserializeUsers(self)
      print("Select a User to chirp it up with!.")
      self.showUser()
      inp3 = input(">")
      userID = self.addUserID(inp3)
      print(userID)



    if user_choice == "3":
      deserializeChirps(self)
      deserializeConvos(self)
      print("Time to get chirpy! Select any chirp to get chirpin'.")
      print('>>>>>PUBLIC<<<<<')
      self.showAllPublicChirps()
      print('>>>>>PRIVATE<<<<<')
      self.showAllPrivateChirps()
      inp7 = input(">")
      self.addConvoID(inp7)
      print(self.addConvoID(inp7))
      print(self.chirps)
      # print(self.users)



    if user_choice == "4":
      deserializeChirps(self)
      chirp = dict()
      uid = str(uuid.uuid4())
      chirp[uid] = dict()
      print("Write a new public chirp!")
      inp4 = input(">")
      chirp[uid]['chirp'] = inp4
      chirp[uid]['uid'] = userID
      chirp[uid]['private'] = False
      chirp[uid]['recipient'] = None
      self.chirps.append(chirp)
      self.createConvos(chirp)
      serializeChirps(self)



    if user_choice == "5":
      deserializeChirps(self)
      chirp = dict()
      uid = str(uuid.uuid4())
      chirp[uid] = dict()
      print("Write a new private chirp!")
      inp5 = input(">")
      chirp[uid]['chirp'] = inp5
      chirp[uid]['uid'] = userID
      chirp[uid]['private'] = True
      print("Who you chirpin at?")
      self.showUser()
      inp6 = input(">")
      userID = self.addUserID(inp6)
      chirp[uid]['recipient'] = userID
      self.chirps.append(chirp)
      self.createConvos(chirp)
      serializeChirps(self)





    # if user_choice == "7":
    #   deserializeConvo(self)
    #   uid = str(uuid.uuid4())
    #   self.convos[uid] = list()
    #   self.convos[uid].append(userID)
    #   serializeConvo(self)
    #   print(self.convos)

    if user_choice != "6":
      self.show_menu()






  def showUser(self):
    u = self.users
    for user in u:
      for k,v in user.items():
        print(v['username'])





  def addUserID(self, inp):
    u = self.users
    for user in u:
      for k,v in user.items():
        if inp == v['username']:
          return k


  def showAllPublicChirps(self):
    # pubChirps = []
    c = self.chirps
    for chirp in c:
      for k,v in chirp.items():
        if v['private'] == False:
          print(v['chirp'])
         # pubChirps.append(v['chirp'])
         # print(pubChirps)



  def showAllPrivateChirps(self):
    c = self.chirps
    for chirp in c:
      for k,v in chirp.items():
        if v['private'] == True:
         print(v['chirp'])


#if return value is of chirp is equal to users

  # def checkUserID(self):
  #   c = self.chirps
  #   for k,v in c.items():
  #     if v['uid'] != None and v['recipient'] != None:
  #       print(v['chirp'])
  def addConvoID(self, inp):
    c = self.convos
    for convo in c:
      for k,v in convo.items():
        # if inp == v['chirp']:
        for x,y in v.items():
          if inp == y['chirp']:
            return x


  def createConvos(self, chirp):
    deserializeConvos(self)
    convo = dict()
    uid = str(uuid.uuid4())
    convo[uid] = chirp
    self.convos.append(convo)
    serializeConvos(self)






    # for chirps
    # if private = true
    # return user id and recipient id
    # if user id or recipient id
    # equal to input
    # and input == user select
    # show private chirps

    # else if private = false
    # show public chirps



   # when a chirp is selected return convo uid and display related chirps
   #print chirps
   #reply - creates a new chirp and appends to list of chirps on convo
   #back - returns user to chirp menu




  # def x(self):
  #   deserializeConvo(self)
  #   c = self.convos
  #   for k,v in c.items():
  #     print(k,v)

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

