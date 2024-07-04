from settings import *
from helper_methods import things_todo_when_loggedin

cursor.execute("Select p.id, p.title,p.content,c.category_name from Post as p join user1 as u on p.author=u.id join category as c on p.category=c.id where u.first_name=? and last_name=?",('maziar','heidari'))
if(cursor.fetchall() !=None):    
        for row in cursor.fetchall():
         print(row)
        things_todo_when_loggedin(1)
else:
        print('No posts where found!')  
      
