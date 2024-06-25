from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic import BaseModel
from datetime import datetime

# SQLALCHEMY 
# setting up the sqlite database for example purposes
engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", connect_args={"check_same_thread": False})
SessionLocal = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)


class UserQuestion(Base):
    __tablename__ = "user_questions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column()
    question: Mapped[str] = mapped_column()
    request_timestamp: Mapped[datetime] = mapped_column()
    answer_timestamp: Mapped[datetime] = mapped_column()


class QuestionRating(Base):
    __tablename__ = "question_ratings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column()
    rating: Mapped[int] = mapped_column()
    timestamp: Mapped[str] = mapped_column(default=datetime.now())
    deleted: Mapped[bool] = mapped_column(default=False)

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()