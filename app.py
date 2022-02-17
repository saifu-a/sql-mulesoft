import sqlite3

conn = sqlite3.connect('movies.db')
cur = conn.cursor()

# Create table
cur.execute(
    '''
        CREATE TABLE IF NOT EXISTS Movies (
            name text,
            actor text,
            actress text,
            director text,
            year_of_release text
        )

    '''
)
# Insert values into table
cur.execute(
    '''INSERT INTO Movies VALUES ('Dhoom 1', 'Surya Batra', 'Madhumita', 'Saif','2023')''')
cur.execute(
    '''INSERT INTO Movies VALUES ('Dhoom 2', 'Vikram Batra', 'Madhumita', 'Saif','2024')''')
cur.execute(
    '''INSERT INTO Movies VALUES ('Dhoom 3', 'Karan Batra', 'Madhumita', 'Saif','2026')''')
cur.execute(
    '''INSERT INTO Movies VALUES ('Dhoom 4', 'Surya Batra', 'Madhumita', 'Saif','2027')''')
cur.execute(
    '''INSERT INTO Movies VALUES ('Dhoom 5', 'Vikram Batra', 'Madhumita', 'Saif','2029')''')

conn.commit()

# Get all values from table
cur.execute('''SELECT * FROM Movies''')
print("\nAll Movies\n")
for movie in cur.fetchall():
    print(movie)

# Get actor name from the user
actor_name = input('\nEnter the name of the actor: ')

# Get all the movies of the actor
cur.execute("SELECT * FROM Movies WHERE actor='{}'".format(actor_name))
print("\nMovies with {} as the actor\n".format(actor_name))
for movie in cur.fetchall():
    print(movie)

conn.close()
