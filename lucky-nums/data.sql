-- In terminal
-- psql < mars_db.sql  (Mac)
-- psql -f mars_db.sql (PC)


DROP DATABASE IF EXISTS lucky_num_db;

CREATE DATABASE lucky_num_db;

\c lucky_num_db


CREATE TABLE photos (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    year INTEGER NOT NULL,
    color TEXT NOT NULL,
);






