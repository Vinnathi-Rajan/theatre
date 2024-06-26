from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

# Database connection configuration
config = {
    'user': 'root',
    'password': '#Sroot',
    'host': 'localhost',
    'database': 'theatre'
}

def get_db_connection():
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Movie")
    movies = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template('movies.html', movies=movies)

@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form['title']
    genre = request.form['genre']
    duration = int(request.form['duration'])
    release_date = request.form['release_date']
    director = request.form['director']
    rating = float(request.form['rating'])

    cnx = get_db_connection()
    cursor = cnx.cursor()
    insert_query = """
    INSERT INTO Movie (title, genre, duration, release_date, director, rating)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (title, genre, duration, release_date, director, rating))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('movies'))

@app.route('/delete_movie/<int:movie_id>')
def delete_movie(movie_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    delete_query = "DELETE FROM Movie WHERE movie_id = %s"
    cursor.execute(delete_query, (movie_id,))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('movies'))

@app.route('/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        duration = int(request.form['duration'])
        release_date = request.form['release_date']
        director = request.form['director']
        rating = float(request.form['rating'])

        cnx = get_db_connection()
        cursor = cnx.cursor()
        update_query = """
        UPDATE Movie
        SET title = %s, genre = %s, duration = %s, release_date = %s, director = %s, rating = %s
        WHERE movie_id = %s
        """
        cursor.execute(update_query, (title, genre, duration, release_date, director, rating, movie_id))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect(url_for('movies'))
    else:
        cnx = get_db_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Movie WHERE movie_id = %s", (movie_id,))
        movie = cursor.fetchone()
        cursor.close()
        cnx.close()
        return render_template('update_movie.html', movie=movie)

@app.route('/screenings')
def screenings():
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Screening")
    screenings = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template('screenings.html', screenings=screenings)

@app.route('/add_screening', methods=['POST'])
def add_screening():
    movie_id = int(request.form['movie_id'])
    screen_id = int(request.form['screen_id'])
    screening_type = request.form['screening_type']
    screening_time = request.form['screening_time']

    cnx = get_db_connection()
    cursor = cnx.cursor()
    insert_query = """
    INSERT INTO Screening (movie_id, screen_id, screening_type, screening_time)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (movie_id, screen_id, screening_type, screening_time))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('screenings'))

@app.route('/delete_screening/<int:screening_id>')
def delete_screening(screening_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    delete_query = "DELETE FROM Screening WHERE screening_id = %s"
    cursor.execute(delete_query, (screening_id,))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('screenings'))

@app.route('/update_screening/<int:screening_id>', methods=['GET', 'POST'])
def update_screening(screening_id):
    if request.method == 'POST':
        movie_id = int(request.form['movie_id'])
        screen_id = int(request.form['screen_id'])
        screening_type = request.form['screening_type']
        screening_time = request.form['screening_time']

        cnx = get_db_connection()
        cursor = cnx.cursor()
        update_query = """
        UPDATE Screening
        SET movie_id = %s, screen_id = %s, screening_type = %s, screening_time = %s
        WHERE screening_id = %s
        """
        cursor.execute(update_query, (movie_id, screen_id, screening_type, screening_time, screening_id))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect(url_for('screenings'))
    else:
        cnx = get_db_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Screening WHERE screening_id = %s", (screening_id,))
        screening = cursor.fetchone()
        cursor.close()
        cnx.close()
        return render_template('update_screening.html', screening=screening)

@app.route('/sellings')
def sellings():
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Selling")
    sellings = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template('sellings.html', sellings=sellings)

@app.route('/delete_selling/<int:selling_id>')
def delete_selling(selling_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    delete_query = "DELETE FROM Selling WHERE selling_id = %s"
    cursor.execute(delete_query, (selling_id,))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('sellings'))

@app.route('/seatings')
def seatings():
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM SeatingBooking")
    seatings = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template('seatings.html', seatings=seatings)

@app.route('/delete_seating/<int:seating_id>')
def delete_seating(seating_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    delete_query = "DELETE FROM SeatingBooking WHERE seating_id = %s"
    cursor.execute(delete_query, (seating_id,))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('seatings'))

if __name__ == '__main__':
    app.run(debug=True)
