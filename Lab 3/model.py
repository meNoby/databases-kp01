import psycopg2
import timeit
from psycopg2 import Error
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import session, sessionmaker, relationship
from sqlalchemy.sql.sqltypes import Float

Base = declarative_base()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Library")
Base.metadata.bind = engine
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
engine.connect()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(90))
    country = Column(String(60))
    books = relationship('Book')
    __table_args__ = {'extend_existing': True}


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String(90))
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    __table_args__ = {'extend_existing': True}


class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(60))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    __table_args__ = {'extend_existing': True}


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    price = Column(Float)
    __table_args__ = {'extend_existing': True}


class authors:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.country = ""

    def create(self, name, country):
        try:
            session = Session()
            session.add(Author(name=name, country=country))
            session.commit()
            print("Author was inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def update(self, id, name, country):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query.get(id)
            t.name = name
            t.country = country
            session.add(t)
            session.commit()
            print("Author was updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def delete(self, id):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Author).get(id)
            session.delete(t)
            session.commit()
            print("Author was deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)


class books:

    def __init__(self):
        self.id = 0
        self.title = ""
        self.year = 0
        self.author_id = -1
        self.subscription_id = -1

    def create(self, title, year, author_id, subscription_id):
        try:
            session = Session()
            session.add(Book(title=title, year=year, author_id=author_id, subscription_id=subscription_id))
            session.commit()
            print("Book was inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def update(self, id, title, year, author_id, subscription_id):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Book).get(id)
            t.title = title
            t.year = year
            t.author_id = author_id
            t.subscription_id = subscription_id
            session.add(t)
            session.commit()
            print("Book was updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def delete(self, id):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Book).get(id)
            session.delete(t)
            session.commit()
            print("Book was deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)


class readers:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.subscription_id = -1

    def create(self, name, subscription_id):
        try:
            session = Session()
            session.add(Reader(name=name, subscription_id=subscription_id))
            session.commit()
            print("Reader was inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def update(self, id, name, subscription_id):
        if (id < 1):
            print('Invalid id entered')
            return
        try:
            t = session.query(Reader).get(id)
            t.name = name
            t.subscription_id = subscription_id
            session.add(t)
            session.commit()
            print("Reader was updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def delete(self, id):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Reader).get(id)
            session.delete(t)
            session.commit()
            print("Reader was deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)


class subscriptions:

    def __init__(self):
        self.id = 0
        self.price = 0

    def create(self, price):
        try:
            session = Session()
            session.add(Subscription(price=price))
            session.commit()
            print("Subscription was inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def update(self, id, price):

        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Subscription).get(id)
            t.price = price
            session.add(t)
            session.commit()
            print("Subscription was updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

    def delete(self, id):
        if (id < 1):
            print('Invalid id')
            return
        try:
            t = session.query(Subscription).get(id)
            session.delete(t)
            session.commit()
            print("Subscription was deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)

class Index:

    def test():
        start = timeit.timeit()
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="postgrepass",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="Library")
            cursor = connection.cursor()
            select_query = """CREATE INDEX ON authors USING BTREE(id); 
                            CREATE INDEX book_name ON books USING gin (to_tsvector('english', code)); 
                            SELECT authors.name, authors.country, books.title from authors, books
                            WHERE authors.id = 1 AND books.author_id = 1;"""
            cursor.execute(select_query)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                end = timeit.timeit()
                print("Time for operation " + str(end - start))

class Trigger:

    def create():
        connection = psycopg2.connect(user="postgres",
                                      password="postgrepass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="Library")
        try:

            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS book_logs;
                        CREATE TABLE book_logs(id integer NOT NULL, old_title text, new_title text, author_id integer);
                        CREATE OR REPLACE FUNCTION log_book() RETURNS trigger AS $BODY$
                        BEGIN
                            IF NEW.title IS NULL THEN
                                RAISE EXCEPTION 'Name cannot be null';
                            END IF;
                            IF NEW.author_id IS NULL THEN
                                RAISE EXCEPTION 'Book cannot have null author_id';
                            END IF;
                            INSERT INTO book_logs VALUES(OLD.id, OLD.title, NEW.title, NEW.author_id);
                            RETURN NEW;
                        END;
                    $BODY$ LANGUAGE plpgsql;
                    DROP TRIGGER IF EXISTS book_subj ON subjects;
                    CREATE TRIGGER book_subj AFTER UPDATE OR INSERT ON books
                        FOR EACH ROW EXECUTE PROCEDURE book_subj();"""
            cursor.execute(query)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()