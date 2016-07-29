
class Board():

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
      print("Create a New Account to get chirpy!.")
      inp = (input("Enter full name >" )
      inp1 = (input("Enter screen name >" )

    if user_choice == "2":
      print("Select a User.")
      inp = (input(">")


    if user_choice == "3":
      print("Time to get chirpy! Select any chirp to get chirpin'")
      inp = (input(">")


    if user_choice == "4":
      print("Time to get chirpy in public! Select any public chirp to get chirpin'")
      inp = (input(">")


    if user_choice == "5":
      print("Time to get chirpy in private! Select any private chirp to get chirpin'")
      inp = (input(">")


    if user_choice != "6":
      self.show_menu()







if __name__ == '__main__':
  board = Board()
  board.show_menu()
