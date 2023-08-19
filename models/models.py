from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(16), nullable=False)

    idea = relationship("Idea", backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Idea(Base):
    __tablename__ = "idea"

    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    activity = Column(String(100), nullable=False)
    accessibility = Column(Float, nullable=False)
    price = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"<Idea {self.type} {self.activity}>"


"""

class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    descriptions = Column(Text)
    created_at = Column(DateTime, server_dafeult=func.now())
    updated_at = Column(DateTime, serve_default=func.now(), onupdate=func.now())

    students = relationship("Student", backref='group', lazy=True)

    def __repr__(self):
        return f"<Grouip {self.name}>"


class Sudent(Base):
    __tablename__ = "sudent"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    male = Column(Boolean, nullable=False, default=True)
    group_id = Column(Integer, ForeignKey("group.id"))

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"

"""
