I did all i could do to connect mysql to django but I fialed. I felt I knew Nothing about frameworks or database, so i had to pull myself up for the love of god! 
These lines were really helpful:
import pyodbc 
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=ASSHOLE\\MYSQLSERVER;'
                      'Database=muzmusic;'
                      'UID=sa;'
                      'PWD=maziare112233@@!!;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()

My project is like a weblog about music, you can authenticate and publish posts and see others post and comment on them or like them and ...
By them way I had to know lots of sql for this project!!!!!!!
