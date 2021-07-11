import json
import os
import pika

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = USER = os.getenv('DB_URI', "postgresql://dev:dev@localhost:5432/dev")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Mails(Base):
    __tablename__ = "mails"

    id = Column(Integer, primary_key=True, index=True)
    mail = Column(String, default='')
    text = Column(String, default='')


@app.get("/")
async def root():
    return {"message": "K8 Examples"}


def create_tables():
    Mails.__table__.create(engine)


@app.get("/getmails")
async def list_mail():
    session = SessionLocal()
    records = session.query(Mails).all()
    result = {}
    for r in records:
        result[r.id] = {
            'mail': r.mail,
            'text': r.text
        }
    return result


@app.get("/savemail/{mail}/{text}")
async def list_mail(mail, text):
    session = SessionLocal()
    session.add(Mails(mail=mail, text=text))
    session.commit()
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBIT_MQ_HOST', 'localhost')))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps({
            "mail": mail,
            "text": text
        }),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return {"done": "yes"}

create_tables()
