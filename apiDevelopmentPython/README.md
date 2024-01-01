# PYTHON API DEVELOPMENT

## Explaination for the simple code

```from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

- `app = FastAPI()` => app is the name of our api
- `@app.get("/")` => is decorator to make api with get method with path(example for this is a root path)
- `async` => to make the function asynchronous(i.e independent from other functions during execution). It is optional.
- `def root()` => Normal function. Name of the function should be descriptive.
- `return {"message": "Hello World"}` => return as json

## To run the api live server

- `uvicorn nameofthefile:nameoftheserver`
- Example for the above assuming code in the main.py file
	- `uvicorn main:app`
	
- To avoid restarting your server every time you change anything you can use --reload option
- `uvicorn main:app --reload`

## CRUD

1. Create - POST         => /posts       @app.post("/posts")
2. Read   - GET		 => /posts/:id   @app.get("/posts/{id}")
	  - GET		 => /posts	 @app.get("/posts")
3. Update - PUT/PATCH	 => /posts/:id	 @app.put("/posts/{id}")
4. Delete - DELETE	 => /posts/:id	 @app.delete("/posts/{id}")

## HTTP response status codes

- HTTP response codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
1. Information reesponses (100 - 199)
2. Successful responses (200 – 299)
3. Redirection messages (300 – 399)
4. Client error responses (400 – 499)
5. Server error responses (500 – 599)
