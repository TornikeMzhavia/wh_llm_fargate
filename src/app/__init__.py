from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db_layer import UserQuestion, QuestionRating, get_db
from app.llm import llm_mockup

from datetime import datetime
from typing import Annotated, Union

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def get_root():
    return {"message": "FastAPI LLM mockup API running in a Docker container"}

class UserQuestionPost(BaseModel):
    user_id: int
    question: str
    
class QuestionRatingPost(BaseModel):
    question_id: int
    rating: int

@app.post("/question")
async def add_question(user_question:UserQuestionPost, 
                       token: Annotated[str, Depends(oauth2_scheme)],
                       db: AsyncSession = Depends(get_db)):
    llm_model = llm_mockup()
    
    user_question.request_timestamp = datetime.now()
    
    answer = None
    error_message = None
    try:
        answer = llm_model.predict_mockup(user_question.question)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
    
    user_question = UserQuestion(user_id=user_question.user_id,
                                 question=user_question.question, 
                                 answer=answer, 
                                 answer_timestamp=datetime.now())
    
    db.add(user_question)
    await db.commit()
    print("Question stored in the database")
    
    return {"answer": answer, "question_id": user_question.id, "error_message": error_message}

@app.post("/rate")
async def add_question_rating(question_rating:QuestionRatingPost, 
                              token: Annotated[str, Depends(oauth2_scheme)],
                              db: AsyncSession = Depends(get_db)):
    question_rating = QuestionRating(question_id=question_rating.question_id, 
                                     rating=question_rating.rating)
    
    db.add(question_rating)
    await db.commit()
    print("Question rating stored in the database")
    
    return {"rating_id": question_rating.id}
