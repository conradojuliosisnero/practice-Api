from fastapi import FastAPI
from fastapi.responses import JSONResponse
from shemas.movies import Movie

app = FastAPI()
app.title = 'practica con fastapi'
app.version = "0.0.1"

peliculas = [{
    "id": 1,
    "nombre": "Soul",
    "año": 2020,
    "rating": 8.1,
    "categoria": "Animación"
  },
  {
    "id": 2,
    "nombre": "Nomadland",
    "año": 2020,
    "rating": 7.4,
    "categoria": "Drama"
  },
  {
    "id": 3,
    "nombre": "The Trial of the Chicago 7",
    "año": 2020,
    "rating": 7.8,
    "categoria": "Drama"
  },
  {
    "id": 4,
    "nombre": "Mank",
    "año": 2020,
    "rating": 7.0,
    "categoria": "Biografia"
  },
  {
    "id": 5,
    "nombre": "Minari",
    "año": 2020,
    "rating": 7.5,
    "categoria": "Drama"
  },
  {
    "id": 6,
    "nombre": "Promising Young Woman",
    "año": 2020,
    "rating": 7.5,
    "categoria": "Crimen"
  },
  {
    "id": 7,
    "nombre": "Judas and the Black Messiah",
    "año": 2021,
    "rating": 7.6,
    "categoria": "Biografia"
  },
  {
    "id": 8,
    "nombre": "The Father",
    "año": 2020,
    "rating": 8.3,
    "categoria": "Drama"
  },
  {
    "id": 9,
    "nombre": "Sound of Metal",
    "año": 2020,
    "rating": 7.8,
    "categoria": "Drama"
  },
  {
    "id": 10,
    "nombre": "Ma Rainey's Black Bottom",
    "año": 2020,
    "rating": 7.1,
    "categoria": "Drama"
  },
  {
    "id": 11,
    "nombre": "The Mauritanian",
    "año": 2021,
    "rating": 7.3,
    "categoria": "Drama"
  },
  {
    "id": 12,
    "nombre": "News of the World",
    "año": 2020,
    "rating": 6.8,
    "categoria": "Accion"
  },
  {
    "id": 13,
    "nombre": "One Night in Miami",
    "año": 2020,
    "rating": 7.2,
    "categoria": "Drama"
  },
  {
    "id": 14,
    "nombre": "The Midnight Sky",
    "año": 2020,
    "rating": 5.6,
    "categoria": "Drama"
  },
  {
    "id": 15,
    "nombre": "Pieces of a Woman",
    "año": 2020,
    "rating": 7.0,
    "categoria": "Drama"
  }
]


# ruta principal 
@app.get('/',tags=['Home'])
def get():
    return "Hola mundo XD"

# metodo get 
@app.get('/movie',tags=['peliculas'])
def get_movies():    
    return peliculas

# metodo get por id
@app.get('/movie/{id}',tags=['peliculas'])
def get_movie(id: int):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            return pelicula
    return JSONResponse(status_code=200,content={"message": 'no se encontro el recurso'})

# metodo get por categoria
@app.get('/movie/',tags=['peliculas por categoria'])
def get_movie_by_category(categoria: str):
    format_movie = categoria.capitalize()
    for pelicula in peliculas:
        if pelicula["categoria"] == format_movie:
            return pelicula
    return JSONResponse(status_code=200, content={"message": 'No se encontraron películas para la categoría proporcionada.'})

# metodo post 
@app.post('/movies',tags=['registro de peliculas'],status_code=200)
def create_movie(movie: Movie):
    peliculas.append(movie)
    return JSONResponse(status_code=201,content={"message":'registrado con exito'})

# metodo put 
@app.put('/movie/{id}',tags=['peliculas'],status_code=200)
def update_movie(id:int, movie:str):
    return JSONResponse(status_code=200,content={"message":'nose encontro el recurso'})

# metodo delete 
@app.delete('/movie/{id}',tags=['peliculas'],status_code=200)
def delete_movie():    
    return "peliculas"