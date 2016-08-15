import unittest
from board import *
import uuid

class TestBoard(unittest.TestCase):

# http://i.imgur.com/lZ0bxod.gifv  <--- uber lolz

  @classmethod
  def setUp(self):
    self.board = Board()
    self.TestBoard = TestBoard()
    self.user
    self.convo = {}
    self.chirp = {}
    self.uid = str(uuid.uuid4())


    self.test_username = "roor"
    self.test_fullname = "castle"
    self.test_chirp = "hi"
    self.test_private = False
    self.test_recipient = None



  def userCreation(self, inp1, inp2):
    # tests to make sure user object has username and fullname keys and values
    self.user[self.uid] = dict()
    testUN = self.user[self.uid]['username'] = inp1
    testFN = self.user[self.uid]['fullname'] = inp2
    return testUN, testFN


  def test_testUserCreation(self):
    self.assertEqual(self.TestBoard.userCreation(self.test_username, self.test_fullname), ('roor', 'castle'))
    # tests to make sure user object has username and fullname keys and values


  def chirpCreation(self, inp1, inp2, inp3):
    #tests to make sure the chirp object has chirp(message), private, recipient keys and values
    self.chirp[self.uid] = dict()
    testChirp = self.chirp[self.uid]['chirp'] = inp1
    testPrivate = self.chirp[self.uid]['private'] = inp2
    testRecipient = self.chirp[self.uid]['recipient'] = inp3
    return testChirp, testPrivate, testRecipient


  def test_testChirpCreation(self):
    self.assertEqual(self.TestBoard.chirpCreation(self.test_chirp, self.test_private, self.test_recipient), ('hi', False, None))
    #tests to make sure the chirp object has chirp(message), private, recipient keys and values


  def convoCreation(self, inp1):
    # tests to make sure convo object has convoname and fullname keys and values
    self.convo[self.uid] = dict()
    testID = self.convo[self.uid]['convoname'] = [chirpID]
    return testUN, testFN

  def test_testconvoCreation(self):
    self.assertEqual(self.TestBoard.convoCreation(self.test_convoname, self.test_fullname), ('roor', 'castle'))
    # tests to make sure us



if __name__ == '__main__':
  unittest.main()
