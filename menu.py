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
        if(choice_after_login in ['1','2','3','4','5','6',7]):
          break
        else:
          print(f"Invalid input try again dear {first_name}")  

      except:
          print(f"Invalid input try again dear {first_name}")  


  
    if(choice_after_login=='1'):
      title=input("Your post title: ")
      content=input("Your post content: ")
      image=input("Your image file address: ")
      category=input("Your category: ")
      author_id=user_id # well im not gonna take users id as an input, imma find it myself
      cursor.execute(f"insertpost ?,?,?,?,?", (title,content,image,category,author_id))
      connection.commit()
      print(f"Congrats {first_name}!You just created a new post!")
      print()
      

    elif(choice_after_login=='2'):
      cursor.execute("Select id,title,content,category,published_date from post")
      for row in cursor.fetchall():
        print(row)
      print()  
      cnt=0
      for row in cursor.fetchall():
        cnt+=1
        print(row)
      if cnt !=0:  
        things_todo_when_loggedin(user_id)
      else:
        print()
        print("No posts were found")  
        print()
      
      
    elif(choice_after_login=='3'):
      category=input(f"What category are you interested in, dear {first_name}?")
      cursor.execute("Select p.id, p.title,p.content,u.first_name from Post as p join Category as c on p.category=c.id join user1 as u on u.id=p.author where c.category_name= ?", (category,))
      cnt=0
      for row in cursor.fetchall():
        cnt+=1
        print(row)
      if cnt !=0:  
        things_todo_when_loggedin(user_id)
      else:
        print()
        print("No posts were found")  
        print()
      

    elif(choice_after_login=='4'):
      name_tuple=clean_full_name()
      cursor.execute("Select p.id, p.title,p.content,c.category_name from Post as p join user1 as u on p.author=u.id join category as c on p.category=c.id where u.first_name=? and last_name=?",(name_tuple[0],name_tuple[1]))
      cnt=0
      for row in cursor.fetchall():
        cnt+=1
        print(row)
      if cnt !=0:  
        things_todo_when_loggedin(user_id)
      else:
        print()
        print("No posts were found")  
        print()
     
      

    elif(choice_after_login=='5'):
      serach_string=input("So what are you looking for? ")
      cursor.execute(f"Searchposts ?",(serach_string,) )
      cnt=0
      for row in cursor.fetchall():
        cnt+=1
        print(row)
      if cnt !=0:  
        things_todo_when_loggedin(user_id)
      else:
        print()
        print("No posts were found")  
        print()

    elif(choice_after_login=='6'):
        view_comments(user_id)
        
  
     

    elif (choice_after_login=='7'):
      con=False
      print(f"Take care dear {first_name}")