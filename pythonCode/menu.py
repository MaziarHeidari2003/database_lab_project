from settings import *
from helper_methods import *

def starting_point_menu():
  print("Welcome to muzmusic weblog")
  print("Did you know if the count of one of your post likes become more than 10< you will be a Celebrity? Now you are just a regular person. so come on! Post something!")
  print()

  while(True):

    print("You already have an account?Enter 1 to signin!")
    print("Join us to share some music,Enter 2 to Signup")
    while(True):

      try:
        choice = int(input("Signup or Signin? "))
        if(choice==2 or choice==1):
          break
        else:
          print("Invalid input try again")  

      except:
        print("Invalid input try again")  

    if choice==2:
      password=input("Enter your password: ")    
      email=input("Enter your email: ")
      firstname=(input("Enter your first name: ")).capitalize()    
      lastname=(input("Enter your last name: ")).capitalize()
      bio=input("Enter your bio: ")
      image=input("Enter your image file address: ") 
      cursor.execute("signup ?, ?, ?, ?, ?, ?", (password, email, firstname, lastname, bio, image))
      connection.commit()
      print()
      print("You are signed up succesfully")
      #cursor.execute("SELECT id FROM user1 WHERE email = ?", (email,))
      #user_id = cursor.fetchone() # now i know which user is logged in
      break

    elif choice==1:
      email=input("Enter your email: ")
      password=input("Enter your password: ")
      try:
        cursor.execute("Signin ?, ?", (email,password))
        connection.commit()
        print()
        print("You are signed in succesfully")
        break
      except:
        print()
        print("User not found")
  cursor.execute("SELECT id FROM user1 WHERE email = ?", (email,))
  user_id = cursor.fetchone() # now i know which user is logged in 
  cursor.execute("SELECT status FROM user1 WHERE email = ?", (email,))
  user_status=cursor.fetchone()
  print(f"Status: You are a {user_status[0]} person!")
  print() 
  return user_id[0]  



def user_options(user_id):
  cursor.execute("Select first_name from user1 where id=?",(user_id,))
  first_name_as_tuple = cursor.fetchone() # now i know which user is logged in  
  first_name=first_name_as_tuple[0]
  con=True
  while(con):

    print("1: Posting new content")
    print("2: Reading others contents")
    print("3: Reading the the contents from a special category")
    print("4: Reading the the contents from a special user")
    print("5: Search for a special title or content or keyword")
    print("6: View all the comments related to a post")
    print("7: Exit")

    while(True):
      try:
        choice_after_login=input("So what to do? ")
        if(choice_after_login in ['1','2','3','4','5','6','7']):
          break
        else:
          print(f"Invalid input try again dear {first_name}")  

      except:
          print(f"Invalid input try again dear {first_name}")  


    if(choice_after_login=='1'):
      post_publish(user_id,first_name)

    elif(choice_after_login=='2'):
      view_posts(user_id)
      
      
    elif(choice_after_login=='3'):
      cat_view_post(user_id,first_name)

    elif(choice_after_login=='4'):
      name_tuple=clean_full_name()
      author_post_view(user_id,name_tuple)
      

    elif(choice_after_login=='5'):
      search_post_view(user_id)

      
    elif(choice_after_login=='6'):
        view_comments(user_id)
        
  
     

    elif (choice_after_login=='7'):
      con=False
      print(f"Take care dear {first_name}")