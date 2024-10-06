user_name = input("Enter your name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
user_choice = input(">>> ")
while user_choice != "Q":
   if user_choice == "H":
       print(f"Hello {user_name}")
   elif user_choice == "G":
       print(f"Good Bye, {user_name}")
   else:
       print("Invalid choice")
   print("(H)ello, $(G)oodbye, $(Q)uit")
   user_choice = input(">>> ")
print("Finished")