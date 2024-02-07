from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    # Validate parameters and can be accessed as attributes
    # schema for the request body using the pydantic BaseModel
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    # optional field for rating


while True:
        try:
            conn = psycopg2.connect(host='localhost', database='fastapi',user='waltermitty', password='walter8236', cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connected successfully")
            break
        except Exception as error:
            print("Error connecting to database")
            print("Error: ", error)
            time.sleep(10)

my_posts = [{"title": "My First Post",
            "content": "This is the content of my first post", "id": 1},
            {"title": "My Second Post",
            "content": "This is the content of my second post",
                "id": 2}]


def get_post_by_id(id: int):
    for post in my_posts:
        if post['id'] == id:
            return post
    return None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
# async def create_post(payload: dict = Body(...)):
# Extracting the data from the request body one by one
async def create_post(post: Post):
    # print(new_post)
    # print(new_post.title)
    # print(new_post.published)
    # print(new_post.dict())
    # return {"data": f"{new_post.dict()}"}
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
    # print(payload)
    # return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
# title str, content str


@app.get("/posts/{id}")
# async def get_post(id: int, response: Response):
async def get_post(id: int):
    post = get_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id {id} not found"}
    return {"post_details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    post = get_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    my_posts.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def find_index_post(id: int):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index
    return None


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, post: Post):
    post_index = find_index_post(id)
    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[post_index] = post_dict
    return Response(status_code=status.HTTP_202_ACCEPTED)
