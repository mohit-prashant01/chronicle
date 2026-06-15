from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root()-> dict[str,str]:
    return{"message":"Chronicles API is running"}