import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_title_list = []
for movie in movies:
    movie_title = movie.getText().split()
    movie_title_new = ""
    for x in range(1, len(movie_title)):
        movie_title_new += movie_title[x] + " "
    movie_title_list.append(movie_title_new)

movies_numbers = [int(movie.getText().split()[0][:-1]) for movie in movies]

for x in range(len(movies_numbers) - 1, 0, -1):
    movie_write = f"{movies_numbers[x]}) {movie_title_list[x]}"
    with open("movies.txt", "a", encoding="utf8") as file:
        file.write(movie_write)
        file.write("\n")

