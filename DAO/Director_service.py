from util.DBConn import DBConnection

class DirectorService(DBConnection):
    def display_director(self):
        try:
            self.cursor.execute("select * from Directors")
            directors=self.cursor.fetchall()
            for director in directors:
                print(director)
        except Exception as e:
            print(e)
    
    def add_director(self,new_director):
        try:
            self.cursor.execute("insert into directors(directorId,name) values(?,?)",(new_director.directorId,new_director.name))
            self.conn.commit()
        except Exception as e:
            print(e)

    def update_director(self,directorId,name):
        try:
            self.cursor.execute("update directors SET ?,? WHERE DirectorId=?",
                        (directorId,name)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)