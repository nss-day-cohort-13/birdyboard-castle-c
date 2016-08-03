import unittest
from board import *
import uuid

class TestBoard(unittest.TestCase):

# http://i.imgur.com/lZ0bxod.gifv  <--- uber lolz

# 1. New User Account
# 2. Select User
# 3. View Chirps
# 4. Public Chirp
# 5. Private Chirp
# 6. Exit
  @classmethod
  def setUp(self):
    self.board = Board()
    self.board.deserializeUser()
    self.board.deserializeChirp()
    self.test_username = "roor"
    self.test_fullname = "castle"
    self.test_chirp = "hi"
    self.test_private = False
    self.test_recipient = None



  def test_testUserCreation(self):
    self.assertEqual(self.board.testUserCreation(self.test_username, self.test_fullname,), ('roor', 'castle'))
    # tests to make sure user object has username and fullname keys and values


  def test_testPublicChirpCreation(self):
    self.assertEqual(self.board.testChirpCreation(self.test_chirp, self.test_private, self.test_recipient), ('hi', False, None))
    #tests to make sure the public chirp object has chirp(message), private, recipient keys and values


if __name__ == '__main__':
  unittest.main()
