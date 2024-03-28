from fastapi import FastAPI
import router.studentroutes as studentroutes
import router.user_routes as userroutes

import uvicorn




app = FastAPI()
app.include_router(studentroutes.router)
app.include_router(userroutes.router)



@app.get("/")
def home():
    return {"msg" : "wel come....!"}





if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True

    )