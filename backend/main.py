from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from langchain_community.chat_models import ChatOpenAI

import os

# FastAPI app initialization
app = FastAPI()

# Database setup
DATABASE_URL = "secret"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    chapters = relationship("Chapter", back_populates="course")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="chapters")
    topics = relationship("Topic", back_populates="chapter")

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    chapter = relationship("Chapter", back_populates="topics")

Base.metadata.create_all(bind=engine)

# Hugging Face Chat Model Setup

chat_model = ChatOpenAI(model_name="tiiuae/falcon-7b-instruct", system_prompt="Generate structured and precise course content with clear chapter titles and detailed topic descriptions.", openai_api_key="secret")

# Pydantic models
class CourseRequest(BaseModel):
    name: str

class ChapterRequest(BaseModel):
    course_id: int
    title: str

class TopicRequest(BaseModel):
    chapter_id: int
    title: str

@app.post("/create_course/")
def create_course(course: CourseRequest, db: Session = Depends(get_db)):
    new_course = Course(name=course.name)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"course_id": new_course.id, "name": new_course.name}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/generate_chapters/{course_name}")
def generate_chapters(course_name: str):
    try:
        prompt = f"Generate major chapters for a course on {course_name}."
        response = chat_model.predict(prompt)
        chapters = response.split("\n")
        return {"course_name": course_name, "chapters": chapters}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating chapters: {str(e)}")

@app.get("/generate_content/{chapter_title}")
def generate_content(chapter_title: str):
    prompt = f"Generate topics and their descriptions for the chapter {chapter_title}."
    response = chat_model.predict(prompt)
    topics = response.split("\n")
    return {"chapter_title": chapter_title, "topics": topics}
