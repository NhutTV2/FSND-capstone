# Casting Agency Capstone

## Project information

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Installing Dependencies

### Install Postgres

The prerequisite to running the app locally is to have a PostgreSQL database available in your local, and the Postgres server must be up and running. Verify the Portgres installation, and start the Postgres server using:

```bash
# Mac/Linux
# Install Postgres using Brew. Reference: https://wiki.postgresql.org/wiki/Homebrew
brew install postgresql
# Verify the installation
postgres --version
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop
```

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

### Set up the environment variables

After you have looked at the starter files, set up the environment variables as:

```bash
# You should have setup.sh and requirements.txt available
chmod +x setup.sh
source setup.sh
# The setup.sh will run the following:
# export DATABASE_URL="postgresql://postgres@localhost:5432/postgres"
# export EXCITED="true"
# Change the DATABASE_URL, as applicable to you.
echo $DATABASE_URL
# postgresql://postgres@localhost:5432/postgres
echo $EXCITED
# true
```

## Local run

### Create databases

Create database `postgres` for app and `fsnd_capstone_test` for testing. Open your terminal and run 2 commands below:

```bash
createdb postgres
createdb fsnd_capstone_test
```

### Run application

From within the project directory, run:

```bash
python3 app.py
```

### Run unit test

From within the project directory, run:

```bash
python3 test_app.py
```

### Get JWT Token

Access login link below to go to login page of Auth0:

```
https://dev-3iqx43uaov68pisd.us.auth0.com/authorize?audience=coffee-shop&response_type=token&client_id=qVLW9l1c0uCZg4a5sOe2MVYHEOj50y58&redirect_uri=http://fsnd-capstone.com/login-success
```

Executive Producer account:

```
# Email
manager123@gmail.com
# Password
manager123@
```

Casting Director account:

```
# Email
casting123director@gmail.com
# Password
casting123director@
```

Casting Assistant account:

```
# Email
casting123assistant@gmail.com
# Password
casting123assistant@
```

## API Documentation

### `GET '/movies'`

- Fetches a dictionary of movies
- Request Arguments: None
- Returns: An array of movies information

```json
{
  "success": true,
  "movies": [
    {
      "id": 1,
      "title": "You",
      "release_date": "2012-12-12"
    }
  ]
}
```

### `GET '/actors'`

- Fetches a dictionary of actors
- Request Arguments: None
- Returns: An array of actors information

```json
{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "Le Thi An",
      "gender": "female",
      "age": 25,
      "movie_id": 1
    }
  ]
}
```

### `POST '/movies'`

- Sends a post request in order to add a new movie
- Request Body:

```json
{
  "title": "You",
  "release_date": "2013-11-13"
}
```

- Returns: New movie information

```json
{
  "success": true,
  "movies": [
    {
      "id": 1,
      "title": "You",
      "release_date": "2013-11-13"
    }
  ]
}
```

### `POST '/actors'`

- Sends a post request in order to add a new actor
- Request Body:

```json
{
  "name": "Le Thi An",
  "gender": "female",
  "age": 25,
  "movie_id": 1
}
```

- Returns: New actor information

```json
{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "Le Thi An",
      "gender": "female",
      "age": 25,
      "movie_id": 1
    }
  ]
}
```

### `PATCH '/movies'`

- Sends a patch request in order to update a new movie info
- Request Body:

```json
{
  "title": "You",
  "release_date": "2013-11-13"
}
```

- Returns: Updated movie information

```json
{
  "success": true,
  "movies": [
    {
      "id": 1,
      "title": "You",
      "release_date": "2013-11-13"
    }
  ]
}
```

### `PATCH '/actors'`

- Sends a patch request in order to update an actor information
- Request Body:

```json
{
  "name": "Le Thi An",
  "gender": "female",
  "age": 25,
  "movie_id": 1
}
```

- Returns: Updated actor information

```json
{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "Le Thi An",
      "gender": "female",
      "age": 25,
      "movie_id": 1
    }
  ]
}
```

### `DELETE '/movies/${id}'`

- Deletes a specified movie using the id of the movie
- Request Arguments: `id` - integer
- Returns: deleted movie id

### `DELETE '/actors/${id}'`

- Deletes a specified actor using the id of the actor
- Request Arguments: `id` - integer
- Returns: deleted actor id
