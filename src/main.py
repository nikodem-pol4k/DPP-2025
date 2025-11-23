from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "files", "movies.csv")

app = FastAPI()

class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def movies():
    movies = []
    with open(FILE_PATH, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movie = Movie(
                movieId=row["movieId"],
                title=row["title"],
                genres=row["genres"]
            )
            movies.append(movie.__dict__)
    return movies

