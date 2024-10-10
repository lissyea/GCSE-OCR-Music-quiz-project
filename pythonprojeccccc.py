import random
import ast

def register():
    with open("usernamestasks.txt", "a") as accounts_file:
        print("")
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        
        accounts_file.write(f"{username}:{password}\n")
        print("Registration successful! You can now log in.")
        print("")

def authentification():
    auth = False
    while not auth:
        name = input("Username: ")
        passw = input("Password: ")
        
        with open("usernamestasks.txt", "r") as accounts_file:
            for line in accounts_file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(":")
                if len(parts) != 2:
                    continue

                username, password = parts
                
                if name == username and passw == password:
                    auth = True
                    break
        
        if not auth:
            print("Incorrect username or password, please try again.")
    
    print("Welcome!")
    print("")

    return name

def songsquiz():
    scoring = 0

    for i in range(0,3):
        with open("songlyrics.txt", "r") as song_file:
            songs = []
            for line in song_file:
                song = ast.literal_eval(line.strip())
                songs.append(song)
        
        song = random.choice(songs)
        
        print(f"Lyrics: {song[1]}")  # shows lyrics
        
        quiz_type = random.choice(["artist", "title"])
        
        if quiz_type == "artist":
            answer = input("Who is the artist of this specific song? ")
            if answer.lower() == song[0].lower():
                print("Correct, the artist is", song[0])
                scoring += 1
            else:
                print(f"Wrong! The correct one is {song[0]}")
        
        elif quiz_type == "title":
            answer = input("What is the title of this song? ")
            if answer.lower() == song[2].lower():
                print("Correct, the song title is indeed", song[2])
                scoring += 1
            else:
                print(f"Incorrect! It is {song[2]}")

    return scoring

def scoresystem(name, scoring):
    with open("songscores.txt", "a") as finalscore:
        finalscore.write(f"Username: {name}, Score: {scoring}\n")                        
        
