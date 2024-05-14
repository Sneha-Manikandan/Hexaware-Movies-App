
# from Entity.Movie import Movie
# from Entity.__init__ import Director,Movie,Actor

from Entity import Director,Movie,Actor
from DAO import DirectorService,MovieService,ActorService


# server_name="LAPTOP-JS8BDPBR\MSSQLSERVER01"
# database_name="HexawareMoviesDB"

# conn_str = (
#     f"Driver={{SQL Server}};"
#     f"Server={server_name};"
#     f"Database={database_name};"
#     f"Trusted_Connection=yes;"
# )

# print(conn_str)

# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()
 
 
# cursor.execute("Select 1")
# print("Database connection is successful 🎊")



class MainMenu:  
    movie_service=MovieService() # no parameter needed since base and child class has no parameter
    director_service=DirectorService()
    actor_service=ActorService()
    def movie_menu(self):
            while True:
                print("""
                    1. View all movies
                    2. Add a movie
                    3. Delete a movie
                    4. Update movie
                    5. Exit
                    """)
                choice=int(input("Please choose what you want to do: "))
                if choice==1:
                    self.movie_service.read_movies()
                elif choice==2:
                    Title=input("Enter the title of the movie: ")
                    Year=input("Which year that movie was released? : ")
                    DirectorId=input("Give the id of the director who directed that movie: ")
                    new_movie=Movie(Title,Year,DirectorId)
                    self.movie_service.add_movies(new_movie)
                    self.movie_service.read_movies() # added oppenheimer
                elif choice==3:
                    self.movie_service.read_movies()
                    MovieId=input("Enter the MovieId you want to remove: ")
                    self.movie_service.remove_movies(MovieId)
                    self.movie_service.read_movies() # removed Oppenheimer coz commit is done
                elif choice==4:
                    MovieId=input("Enter the MovieId you want to update: ")
                    Title=input("Enter the title: ")
                    Year=input("Enter the year: ")
                    DirectorId=input("Enter DirectorId: ")
                    self.movie_service.update_movie(MovieId,Title,Year,DirectorId)
                    self.movie_service.read_movies()
                elif choice==5:
                    print("Thank You !!!")
                    break
                else:
                    print("Enter correct choice")


    def director_menu(self):
        while True:
            print("""
                  1. Display Directors
                  2. Add director
                  3. Remove Director
                  4. Update Director
                  5. Exit
                  """)
            choice=int(input("Enter the choice you want to do: "))
            if choice==1:
                self.director_service.display_director()
            elif choice==2:
                directorId=int(input("Enter the Director ID: "))
                name=input("Enter Director name: ")
                new_director=Director(directorId,name)
                self.director_service.add_director(new_director)
            elif choice==3:
                continue
            elif choice==4:
                directorId=int(input("Enter the Director ID you want to update: "))
                name=input("Enter Director name: ")
                self.director_service.update_director(directorId,name)
            elif choice==5:
                break
            else:
                print("Invalid")

    def actor_menu(self):
        pass

def main():
    while True:
            print("""
                1. Movie Management
                2. Director Management
                3. Actor Management
                4. Exit
                """)
            choice=int(input("Please choose what you want to do: "))
            if(choice==1):
                main_menu.movie_menu()
            elif(choice==2):
                main_menu.director_menu()
            elif(choice==3):
                main_menu.actor_menu()
            elif(choice==4):
                print("Thank You !!")
                main_menu.movie_service.close()
                main_menu.director_service.close()
                break
            else:
                print("Invalid! Enter proper choice")
   
        

if __name__=="__main__":
    print("WELCOME TO MOVIES APP")
    main_menu=MainMenu()
    main()
    