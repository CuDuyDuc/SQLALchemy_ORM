from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:14032001@localhost:5432/SQLALchemy', echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(50))
    
Base.metadata.create_all(engine)

# insert data
# while True:
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     email = input("Enter your email: ")
#     user = User(name = name, age = age, email = email)
#     session.add(user)
#     session.commit()
#     check_out = input("Do you want to continue entering? Y/N: ").lower()
#     if check_out=="n":
#         break

# Get all data

# users = session.query(User)
# for user in users:
#     print(user.name, user.age, user.email)

#---------------------------------------------------------------#
# Get data in order

# user = session.query(User).order_by(User.name)
# for u in user:
#     print(u.name)


#---------------------------------------------------------------#
# Get data by filtering

# user = session.query(User).filter(User.age == 24).first()
# print(user.name, user.age)

# user = session.query(User).filter(or_(User.name == "Duc", User.name == "Duy"))
# for u in user:
#     print(u.name, u.age)

#---------------------------------------------------------------#
# Count the number of result

# user_count = session.query(User).filter(or_(User.name == "Duc", User.name == "Duy")).count() 
# print(user_count)

#---------------------------------------------------------------#
# Update data

# user_Update = session.query(User).filter(User.name == "Duy").first()

# user_Update.name = "Huy"
# session.commit()

#---------------------------------------------------------------#
# Delete data

# user_Delete = session.query(User).filter(User.name == "Phat").first()

# session.delete(user_Delete)
# session.commit()