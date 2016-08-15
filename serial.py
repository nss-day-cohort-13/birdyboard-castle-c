import pickle

def serializeUsers(self):
  with open('userData.txt', 'wb+') as u:
    pickle.dump(self.users, u)

def deserializeUsers(self):
  try:
    with open('userData.txt', 'rb+') as u: #rb in read binary
      self.users = pickle.load(u)

  except EOFError:
    self.users = []

  except FileNotFoundError:
    self.users = []



def serializeChirps(self):
  with open('chirps.txt', 'wb+') as u:
    pickle.dump(self.chirps, u)

def deserializeChirps(self):
  try:
    with open('chirps.txt', 'rb+') as u: #rb in read binary
      self.chirps = pickle.load(u)

  except EOFError:
    self.chirps = []

  except FileNotFoundError:
    self.chirps = []



def serializeConvos(self):
  with open('convos.txt', 'wb+') as u:
    pickle.dump(self.convos, u)

def deserializeConvos(self):
  try:
    with open('convos.txt', 'rb+') as u: #rb in read binary
      self.convos = pickle.load(u)

  except EOFError:
    self.convos = []

  except FileNotFoundError:
    self.convos = []
