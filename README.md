# BookClub [![Build Status](https://travis-ci.org/stephenfeagin/BookClub.svg?branch=master)](https://travis-ci.org/stephenfeagin/BookClub)

**Django app for book reviews and discussions**

This project is a web app that allows users to share the books that they are reading, 
create lists of books they have already read or are planning to read, and write reviews
of books. Future iterations will allow for creation of groups, whereby users can discuss
books together and plan future readings.

## Tech Stack

BookClub is built primarily with Django (Python 3.6+), using Bootstrap for some basic styling.

## Installation

To install this application, first clone the git repository:

```bash
git clone https://github.com/stephenfeagin/BookClub.git
```

Then, create a virtual environment and install the dependencies:

```bash
cd BookClub
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Then deploy it using Django's built-in server:

```bash
python3 manage.py runserver
```
