# Piclo bidding challenge :tada: :battery: :chart_with_upwards_trend: :metal:

## High Level Design

![HLD](/diagrams/HL%20Diagram.png "HLD")

## Class Diagram

![Class Diagram](/diagrams/Class%20Diagram.png "Class Diagram")

## Relationship Diagram

![Relationship Diagram](/diagrams/Relationship%20Diagram.png "Relationship Diagram")

## Running the project:

1. Backend:

   - cd backend
   - pip3 install django
   - pip3 install djangorestframework
   - python manage.py migrate
   - python manage.py createsuperuser --username admin --email admin@gmail.com
   - create .env file and add username, password, and django secret key.
   - generate authentication token by either curl -d "username=admin&password=admin" -X POST http://localhost:8000/api/api-token-auth/ or python manage.py drf_create_token username.
   - python manage.py runserver

2. Frontend

   - cd frontend/bidding
   - npm install
   - add generated token to the AuthStr constant in the app.js
   - npm start

The pull request implements the following tasks.

## Tasks

1. Set up an application where all data (`data/*.json`) can be loaded and
   stored in a database.
2. Build an API which aligns to that data, and its associated business logic.
   Include any validation you deem relevant.
3. In the frontend, consume the competitions endpoint - we're only interested
   in competitions that have **successful** bids.
4. On a single page, for each competition, display its name, buyer and a
   count of bids per seller.
5. Update the README with any provisioning steps for running the code and/or
   tests

## Business Logic

Dummy data for `buyers`, `sellers`, `competitions` and `bids` can be found in
the `data` folder.

The following logic closely mirrors that of our production system. Some of it
may not be relevant.

The [Piclo platform](https://picloflex.com) allows **buyers** (system operators) to advertise **competitions** for procuring flexibility from **sellers** (flex providers). Sellers can then submit **bids** against competitions.

The following relations are in place:

- a buyer has many competitions
- a competition has many bids
- a seller has many bids

A bid is **successful** if the following is true:

- its `offered_capacity` is equal to or greater than the competition's `minimum_capacity`
- its `accepted` state is true
- its associated `seller`'s `verified` state is true
- it was created within the associated competition's `open` and `closed` dates

A competition has the following states:

- _pending_ when the competition's `open` and `closed` date/times are in the
  future
- _open_ when the `open` value is in the past, but `closed` is in the future
- _closed_ when `open` and `closed` are in the past

Assume competitions' `open` / `closed` date/times are always sequential

Capacity values use MW units

## Task

<<<<<<< HEAD
Dummy data for `buyers`, `sellers`, `competitions` and `bids` can be found in the `data` folder.
=======
Dummy data from backend `buyers`, `sellers`, `competitions` and `bids` endpoints can be found in the `data` folder.

> > > > > > > 4b2d6c7... task done

Complete the tasks for the role you are applying for. This is more than two hours' work. Feel free to focus on those tasks you feel best demonstrate your skillset (e.g. you make prefer to start with/focus on the UI components).

### Frontend track

1. Build a data structure representing a list of **successful** bids by ID.
2. Build a data structure which to represent **closed** competitions, containing:

- The competition's `name` and that of its associated **buyer**
- the total value of successful bids in the competition
- the total volume of `offered_capacity` for successful bids

3. Build a data structure to represent competitions including its `name` and a value representing a percentage of **successful** bids
4. Build a list of the top 10 buyers by number of competitions (irrespective of status)
5. Display this data on a single page. We've intentionally left this vague.
6. Update the README with any provisioning steps for running the code and/or tests

Assume you have lazy backend colleagues and data returned from the backend has not yet implemented the above logic (aside from competitions' `open` and `closed` dates being sequential)

### Fullstack track

1. Set up an application where all data (`data/*.json`) can be loaded and stored in a database.
2. Build an API which aligns to that data, and its associated business logic. Include any validation you deem relevant.
3. In the frontend, consume the competitions endpoint - we're only interested in competitions that have **successful** bids.
4. On a single page, for each competition, display its name, buyer and a count of bids per seller.
5. Update the README with any provisioning steps for running the code and/or tests

# Submitting your solutions

1. Perform a code review of the existing PR as you would against a production
   system.
2. Once you have completed the code review, create a new branch based on the
   existing pull request.
3. Work on the new branch committing early and often.
4. Create a pull request describing your solution, including any relevant
   design decisions.

Things we'll be considering:

- Tests
- Scalability
- Security
- Prioritisation (hint: descoping is fine)
- Communication and documentation
