# Use the latest version of the MySQL image as the base
FROM mysql:latest

# Set the MySQL root password (replace 'Sroot' with your desired password)
ENV MYSQL_ROOT_PASSWORD=Sroot

# Copy the SQL initialization script to the container
COPY ./movie.sql /docker-entrypoint-initdb.d/

