from util.DBConn import DBConnection
class MovieService(DBConnection):
    # def __init__(self,conn):
    #     self.conn=conn
    #     self.cursor=conn.cursor()
    def read_movies(self):
        try:
            self.cursor.execute("select * from movies")
            movies=self.cursor.fetchall()
            for movie in movies:
                print(movie)
            # row one at a time
            # for row in cursor:
            #     print(row)  
        except Exception as e:
            print(e)

    # Task 1
    def add_movies(self,movie):
        try:
            self.cursor.execute("INSERT INTO Movies (Title, Year, DirectorId) VALUES(?,?,?)",
                        (movie.title, movie.year, movie.directorId)
                        )
            
            self.conn.commit() # Permanently store | no commit we can undo 
        except Exception as e:
            print(e)
       
    # Task 2
    def remove_movies(self,MovieId):
        try:
            self.cursor.execute("DELETE FROM Movies WHERE MovieId=?",
                        (MovieId)
                        )
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def update_movie(self,MovieId,Title,Year,DirectorId):
        try:
            self.cursor.execute("UPDATE Movies SET ?,?,? WHERE MovieId=?",
                        (MovieId,Title,Year,DirectorId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)
            
