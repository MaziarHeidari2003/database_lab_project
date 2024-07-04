from settings import *


def clean_full_name():
    while(True):
      wanted_user=input("Which user are you interested in? Enter his/her firstname and lastname")
      parts=wanted_user.split()
      if len(parts) !=2:
        print("Invalid name!")
      else:
          break
    firstname=parts[0].capitalize()
    lastname= ' '.join([part.capitalize() for part in parts[1:]]) 


    return (firstname,lastname)



def like_post(user_id):
    while(True):
        try:
          post_id=int(input("Which post to like? Enter the id: "))
          break
        except:
          print("Invalid input")  
    cursor.execute(f"AddLike ?,?",(user_id,post_id))
    connection.commit()
    print("You just liked a post!")  





def add_comment(user_id):
      while(True):
        try:
          post_id=int(input("Which post to comment? Enter the id: "))
          break
        except:
          print("Invalid input")  
      comment_text=input("Enter your comment: ")  
      cursor.execute("AddComment ?,?,?",(user_id,post_id,comment_text))  
      connection.commit()
      print("You just added a comment!")



def things_todo_when_loggedin(user_id):
    print()
    print("Now you can like a post, comment in post or get back to the main options")
    print("1: Like")
    print("2: Comment")
    print("3: Enough likes or Comments in this page!")
    while(True):
      user_action=input("Choose 1 to like, 2 to comment and 3 to leave this page: ")
      if(user_action=='1'):
        like_post(user_id)
      elif(user_action=='2'):
        add_comment(user_id)
      elif(user_action=='3'):
        break
    print()  