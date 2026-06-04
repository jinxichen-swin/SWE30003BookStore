from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import ForeignKey
from database.models.user import User
from sqlalchemy import create_engine, Engine
import bcrypt

class UserManager():
    def __init__(self, engine: Engine):
        self.engine = engine

    def register_user(self, firstname: str, surname: str, email: str, password: str) -> User:
        with Session(self.engine,expire_on_commit=False) as session:
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            user = User(firstname=firstname, surname=surname, email=email, password=hashed_password)
            session.add(user)
            session.commit()
            return user

#Get User
    def get_user(self, user_id: int) -> User:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(User).filter(User.email == email).first()
        

    #IDK, maybe useful??
    def get_user_by_firstname(self, firstname: str) -> list[User]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(User).filter(User.firstname == firstname).all()

    def get_user_by_surname(self, surname: str) -> list[User]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(User).filter(User.surname == surname).all()

#Update

    def update_profile(self, user_id: int, firstname: str = None, surname: str = None, email: str = None, password: str = None) -> User:
        with Session(self.engine,expire_on_commit=False) as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                if firstname:
                    user.firstname = firstname
                if surname:
                    user.surname = surname
                if email:
                    user.email = email
                if password:
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    user.password = hashed_password
                session.commit()
            return user


    # def update_user_email(self, user_id: int, email: str) -> User:
    #     with Session(self.engine,expire_on_commit=False) as session:
    #         user = session.query(User).filter(User.id == user_id).first()
    #         if user:
    #             user.email = email
    #             session.commit()
    #         return user
        
    # def update_firstname(self, user_id: int, firstname: str) -> User:
    #     with Session(self.engine,expire_on_commit=False) as session:
    #         user = session.query(User).filter(User.id == user_id).first()
    #         if user:
    #             user.firstname = firstname
    #             session.commit()
    #         return user
        
    # def update_surname(self, user_id: int, surname: str) -> User:
    #     with Session(self.engine,expire_on_commit=False) as session:
    #         user = session.query(User).filter(User.id == user_id).first()
    #         if user:
    #             user.surname = surname
    #             session.commit()
    #         return user
        
    # def update_password(self, user_id: int, password: str) -> User:
    #     with Session(self.engine,expire_on_commit=False) as session:
    #         user = session.query(User).filter(User.id == user_id).first()
    #         if user:
    #             user.password = password
    #             session.commit()
    #         return user
        
        

#Statistic
    def get_all_users(self) -> list[User]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(User).all()
    


#Delete

    def delete_user(self, user_id: int) -> None:
        with Session(self.engine,expire_on_commit=False) as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()


#Login
    def login(self, email:str, password: str) -> User | None:
        with Session(self.engine, expire_on_commit=False) as session:
            user = session.query(User).filter(User.email == email).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return user
        return None