from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Crash course")

@app.get("/")
def root():
    return{"messege":"Hello FastAPI"}

    @app.get("/Sri")
    def root():
        return{"messege":"Hello Srinithya"}

        # sending single parameter
        @app.get("/user/{user_id}")
        def user_name(user_id:int):
            return{"user_id":user_id, "type":str(type(user_id))}

            # sending multiple parameter

            @app.get("/search")
            def search(q: str, page: int=1, limit: int=10):
                return{"q":q, "page": page, "limit":limit}

                class userCreate(BaseModel):
                    name: str
                        email: str
                            age:int | None = None

                            @app.post("/users")
                            def create_user(payload: userCreate):
                                return{"created": True, "User": payload.model_dump()}

                                # curl -X POST http://127.0.0.1:8000/users \
                                # -H "Content-Type: application/json" \
                                # -d '{"name":"Sri","email":"Sri@demo.com","age":22}'


                                class ProductCreate(BaseModel):
                                    name: str = Field(min_length=2, max_length=50)
                                        price: float = Field(ge=0)
                                            stock: int= Field(ge=0)

                                            @app.post("/products")
                                            def create_product(p: ProductCreate):
                                                return p.model_dump()


                                                # curl -X POST http://127.0.0.1:8000/products \
                                                # -H "Content-Type: application/json" \
                                                # -d '{"name":"pen","price":10.5,"stock":100}'

                                                @app.post("/items", status_code=status.HTTP_226_IM_USED)
                                                def create_item():
                                                    return {"created": True}

                                                    FAKE_DB={1:"Sri", 2:"Varsh"}

                                                    @app.get("/user/db/{user_id}")
                                                    def User_from_DB(user_id: int):
                                                        if user_id not in FAKE_DB:
                                                                raise HTTPException(status_code =404, detail="User not found")
                                                                    return {"user_id": user_id, "Name":FAKE_DB[user_id]}