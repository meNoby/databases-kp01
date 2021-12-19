import psycopg2
from timeit import default_timer as timer
from psycopg2 import Error


class authors:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.country = ""

    def create(self, name, country):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO authors (name, country) VALUES (%s, %s)"""
            item_tuple = (name, country)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Author inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            select_query = """SELECT * from authors WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result:", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, name, country):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            update_query = """Update authors 
                                SET name = (%s),
                                    country = (%s) 
                                WHERE id = %s"""
            item_tuple = (name, country, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Author updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            cursor.execute("Delete from authors WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Author deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, gen_num):

        if (gen_num < 1):
            print('Invalid value')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()

            generate_query = """INSERT INTO authors (name, country)
                                    SELECT md5(random()::text), md5(random()::text)
                                    FROM generate_series(1, %s)"""
            item_tuple = gen_num,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Author generated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def searchAuthorsBooks(self, name, year):

        sttime = timer()

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            select_query = """ SELECT name, year, title 
                               FROM authors, books
                               WHERE year > %s AND name LIKE %s AND books.author_id = authors.id
                               ORDER BY year DESC"""
            item_tuple = (year, '%' + name + '%')
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
            error()
        finally:
            if connection:
                cursor.close()
                connection.close()

                endtime = timer()

                print("Search operation lasted " + str((endtime - sttime) * 1000) + " ms")


class books:

    def __init__(self):
        self.id = 0
        self.title = ""
        self.year = 0
        self.author_id = -1
        self.subscription_id = -1

    def create(self, title, year, author_id, subscription_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO books (title, year, author_id, subscription_id) VALUES (%s, %s, %s, %s)"""
            item_tuple = (id, title, year, author_id, subscription_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Book inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            select_query = """SELECT * from books WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, title, year, author_id, subscription_id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            update_query = """Update books 
                              SET title = (%s),
                                  year = (%s), 
                                  author_id = (%s),
                                  subscription_id = (%s)
                               WHERE id = (%s)"""
            item_tuple = (title, year, author_id, subscription_id, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Book updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            cursor.execute("Delete from books WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, gen_num):

        if (gen_num < 1):
            print('Invalid input')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()

            generate_query = """INSERT INTO books (title, year, author_id, subscription_id)
                                SELECT md5(random()::text), (1600 + trunc(random()*421)::int), (1 + floor(random()*((SELECT id FROM authors ORDER BY id DESC LIMIT 1) - (SELECT id FROM authors ORDER BY id LIMIT 1) + 1) + (SELECT id FROM authors ORDER BY id LIMIT 1))::int), (trunc(random()*(SELECT id FROM subscriptions ORDER BY id DESC LIMIT 1))::int)
                                FROM generate_series(1, %s)"""
            item_tuple = gen_num,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Book generated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


class readers:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.read_count = 0
        self.subscription_id = -1

    def create(self, name, subscription_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO readers (name, subscription_id) VALUES (%s, %s, %s)"""
            item_tuple = (id, name, subscription_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Reader inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            select_query = """SELECT * from readers WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, name, subscription_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            update_query = """Update readers 
                              SET name = (%s),
                                  subscription_id = (%s)
                                  WHERE id = (%s)"""
            item_tuple = (name, subscription_id, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Reader updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            cursor.execute("Delete from readers WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Reader deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, gen_num):

        if (gen_num < 1):
            print('Invalid input')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()

            generate_query = """INSERT INTO readers (name, subscription_id)
                                    SELECT md5(random()::text), (1 + (trunc(random()*0.9*(SELECT id FROM subscriptions ORDER BY id DESC LIMIT 1))::int))
                                    FROM generate_series(1, %s)"""
            item_tuple = gen_num,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Reader generated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


class subscriptions:

    def __init__(self):
        self.id = 0
        self.price = 0

    def create(self, price):

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO subscriptions (price) VALUES (%s)"""
            item_tuple = (price)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Subscription inserted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            select_query = """SELECT * from subscriptions WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, price):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            update_query = """Update subscriptions 
                              SET price = (%s),
                              WHERE id = (%s)"""
            item_tuple = (price, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Subscription updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()
            cursor.execute("Delete from subscriptions WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Subscription deleted")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, gen_num):

        if (gen_num < 0):
            print('Invalid input')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgrepass",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Library")
            cursor = connection.cursor()

            generate_query = """INSERT INTO subscriptions (price)
                                    SELECT (trunc(random()*1000)::int)
                                    FROM generate_series(1, %s)"""
            item_tuple = gen_num,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Subscription generated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


