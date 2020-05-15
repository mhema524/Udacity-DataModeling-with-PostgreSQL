# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table_drop"
song_table_drop = "DROP TABLE IF EXISTS song_table_drop"
artist_table_drop = "DROP TABLE IF EXISTS artist_table_drop"
time_table_drop = "DROP TABLE IF EXISTS time_table_drop"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
              songplay_id SERIAL PRIMARY KEY,
              start_time time,
              user_id int,
              level varchar(10),
              song_id varchar(25),
              artist_id varchar(25),
              session_id int,
              location text,
              user_agent text);

""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar(20), last_name varchar(20), gender char(1), level varchar(20));
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year int,
    duration numeric)
""")


artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (
         artist_id varchar PRIMARY KEY,
         name varchar,
         location text,
         latitude float,
         longitude float);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time time, hour int, date int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING

""")

user_table_insert = ("""
INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level)
        VALUES(%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artist (
      artist_id,
      name,
      location,
      latitude,
      longitude)
      VALUES (%s, %s, %s, %s, %s)
      ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (
         start_time,
         hour,
         date,
         week,
         month,
         year,
         weekday)
         VALUES(%s, %s, %s, %s, %s, %s, %s)
         ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT 
t1.song_id,
t2.artist_id
FROM songs t1
JOIN artist t2 
ON t1.artist_id = t2.artist_id 
WHERE t1.title = %s
and t2.name = %s
and t1.duration = %s;

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]