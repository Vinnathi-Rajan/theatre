USE theatre;

CREATE TABLE Movie (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    duration INT,
    release_date DATE,
    director VARCHAR(255),
    rating DECIMAL(3, 1)
);

CREATE TABLE Screening (
    screening_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    screen_id INT,
    screening_type VARCHAR(50),
    screening_time DATETIME,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    UNIQUE(movie_id, screen_id, screening_time)
);

CREATE TABLE Selling (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    screening_id INT,
    customer_id INT,
    sale_date DATETIME,
    total_amount DECIMAL(10, 2),
    ticket_quantity INT,
    FOREIGN KEY (screening_id) REFERENCES Screening(screening_id)
);

CREATE TABLE SeatingBooking (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    screening_id INT,
    seat_id INT,
    customer_id INT,
    booking_date DATETIME,
    booking_status VARCHAR(50),
    FOREIGN KEY (screening_id) REFERENCES Screening(screening_id),
    UNIQUE(screening_id, seat_id)
);

INSERT INTO Movie (title, genre, duration, release_date, director, rating)
VALUES
    ('The Shawshank Redemption', 'Drama', 142, '1994-10-14', 'Frank Darabont', 9.0),
    ('The Godfather', 'Crime, Drama', 175, '1972-03-24', 'Francis Ford Coppola', 9.3),
    ('The Dark Knight', 'Action, Crime, Drama', 152, '2008-07-18', 'Christopher Nolan', 9.5);

INSERT INTO Screening (movie_id, screen_id, screening_type, screening_time)
VALUES
    (1, 1, '2D', '2024-06-23 18:00:00'),
    (2, 2, '2D', '2024-06-23 20:30:00'),
    (3, 1, 'IMAX', '2024-06-24 15:00:00');

INSERT INTO Selling (screening_id, customer_id, sale_date, total_amount, ticket_quantity)
VALUES
    (1, 101, '2024-06-23 16:30:00', 25.00, 2),
    (2, 102, '2024-06-23 19:45:00', 30.00, 1),
    (3, 103, '2024-06-24 14:00:00', 40.00, 2);

INSERT INTO SeatingBooking (screening_id, seat_id, customer_id, booking_date, booking_status)
VALUES
    (1, 101, 101, '2024-06-23 15:45:00', 'confirmed'),
    (1, 102, 102, '2024-06-23 15:50:00', 'confirmed'),
    (2, 201, 102, '2024-06-23 19:30:00', 'pending'),
    (3, 101, 103, '2024-06-24 13:45:00', 'confirmed'),
    (3, 102, 103, '2024-06-24 13:50:00', 'confirmed');
  