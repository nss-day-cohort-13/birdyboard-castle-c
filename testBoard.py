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


  # def test_user_ID(self):
    # self.assertEqual(self.board.create_ID(1), 1)

  def test_user_full_name(self):
    self.assertEqual(self.board.fullnameSelect(), (1, 'castle crawford'))

  def test_user_screen_name(self):
    self.assertEqual(self.board.usernameSelect(), (1, 'RooR'))


  # def test_user_select(self):
  #   self.assertEqual(self.board.select_user("RooR"), "RooR")


  # def test_chirp_public(self):
  #   self.assertEqual(self.board.public_chirp("RooR", "Rawr", "Roar"), "RooR", "Rawr", "Roar")


  # def test_chirp_private(self):
  #   self.assertEqual(self.board.private_chirp("RooR", "Rawr"), "RooR", "Rawr")



if __name__ == '__main__':
  unittest.main()
