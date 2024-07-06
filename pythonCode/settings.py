import pyodbc 



connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=ASSHOLE\\MYSQLSERVER;'
                      'Database=muzmusic;'
                      'UID=sa;'
                      'PWD=maziare112233@@!!;'

                      'Trusted_Connection=yes;')



cursor = connection.cursor()


