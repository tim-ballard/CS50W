## SQL Databases

This course is going to use PostgreSQL

##### OSX Management
``` bash
brew services start postgresql
brew services stop postgresql

# one off:
pg_ctl -D /usr/local/var/postgres start

# Terminal Interface
psql postgres

# Commands
\h # help
\l # list databases
\c <name> # Connect Database
```

Data types

* Integer
* Decimal
* Serial - Incrementing
* Varchar
* Timestamp
* Boolean
* ENUM


#### Create Table
``` SQL
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);
```

#### Constraints
* NOT NULL
* UNIQUE
* PRIMARY KEY
* DEFAULT
* CHECK

#### Insert
``` SQL
INSERT INTO flights (origin, destination, duration)
  VALUES ('New York', 'London', 415);
```

#### Select
``` SQL
SELECT * FROM flights
WHERE id = 3;
```

#### Functions
* SUM
* COUNT
* MIN
* MAX
* AVG
* ...


#### Update
``` SQL
UPDATE flights
  SET duration = 430
  WHERE origin = 'New York'
  AND destination = 'London';
```

#### Delete
``` SQL
DELETE from flights
WHERE destination = 'Tokyo';
```

### Limit
``` SQL
SELECT * FROM flights
ORDER BY duration ASC
LIMIT 3;
```

### Group By
``` SQL
SELECT origin, COUNT(*)
FROM flights
GROUP BY origin
HAVING COUNT(*) > 1;
```

### Foreign Key
``` SQL
CREATE TABLE passenger (
  ID SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights
);
```

### Joins
``` SQL
SELECT origin,
    destination,
    name
FROM flights
  JOIN passenger
    ON flights.id = passenger.flight_id;
```
As in T-SQL you can also:
* LEFT JOIN
* RIGHT JOIN

### Indexes
``` SQL
CREATE INDEX
```

### Nesting
``` SQL
SELECT *
FROM flights
WHERE id IN (SELECT flight_id
  FROM passenger
  GROUP BY flight_id
  HAVING COUNT(*) > 1);
```
