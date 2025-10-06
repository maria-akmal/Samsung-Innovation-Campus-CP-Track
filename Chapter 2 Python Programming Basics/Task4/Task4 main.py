import json
file = open("movies.json","r")
data = json.load(file)
while True:
    print("Tv Show")
    print("1.show all Tv shows")
    print("2.Search for a Tv show")
    print("3.Add a Tv shows")
    print("4.Remove a Tv shows")
    print("5.Close")
    choice = input("Enter your choice:")
    if choice == "1":
        for movie in data:
            print(movie["title"] , movie["year"] , movie["genre"])
    elif choice == "2":
        title = input("Title: ")
        year = int(input("Year: "))
        genre = input("Genre: ")
        found = False
        for movie in data:
             if movie["title"] == title and movie["year"] == year and movie["genre"] == genre:
                 print("Movie found" , movie["title"] , movie["year"] , movie["genre"])
                 found = True
                 break
    elif choice == "3":
        title = input("Title: ")
        year = input("Year: ")
        genre = input("Genre: ")
        movies = {
            "title": title,
            "year": year,
            "genre": genre
        }
        data.append(movies)
        file = open("movies.json", "w")
        json.dump(data, file)
        print("Movie data is saved ")
    elif choice == "4":
        title = input("Title: ")
        year = input("Year: ")
        genre = input("Genre: ")
        found = False
        for movie in data:
            if movie["title"] == title and movie["year"] == year and movie["genre"] == genre:
                data.remove(movie)
                file = open("movies.json", "w")
                json.dump(data, file)
                print("Movie data is removed ")
                found = True
                break
    elif choice == "5":
        print("Close")
        break
    else:
        print("Invalid input")