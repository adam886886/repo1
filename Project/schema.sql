DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS calendar_events;
CREATE TABLE calendar_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_date TEXT NOT NULL,
    region TEXT NOT NULL,
    event TEXT NOT NULL
);

DROP TABLE IF EXISTS macrodata;
CREATE TABLE macrodata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT NOT NULL,
    event_name TEXT NOT NULL,
    reference_date TEXT NOT NULL,
    latest_value TEXT,
    previous_value TEXT,
    expected_value TEXT
);

DROP TABLE IF EXISTS recapdata;
CREATE TABLE recapdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    country TEXT NOT NULL,
    event TEXT NOT NULL,
    actual TEXT,
    expected TEXT,
    previous TEXT
);
