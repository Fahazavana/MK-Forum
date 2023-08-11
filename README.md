# Mk-forum (Mathematika sy Kajy Forum)

Mk-forum is a web forum project created to gain hands-on experience in web development, specifically back-end development using Python/Django and related technologies. It is an improved version of the original [Kajy](https://github.com/Fahazavana/Kajy) web forum.

The aim of this project is to create a simple forum dedicated to mathematics and related topics.

## Technologies Used

* Python 3
* Django 4
* MySQL/Sqlite3
* HTML/CSS/JS
* Bootstrap 5
* Mathjax to render mathematical text.

## Features

Mk-forum includes the following features:

* User: Auth system, as the user can manage their account: create, update profile information,  change profile picture.
* Posts: Create, Read, Update (modify), and Delete
* Comments: Users can create, update and delete a 
comment on post
* Reactions: Users can react to posts or a  comment (Up or down)

*Next task: permit to the user to delete their profile picture, notification on comment or on react on Post/Comment*
## Getting Started

To get started with Mk-forum, you will need Python 3 installed on your machine. You also need to install the required packages by running `pip install -r requirements.txt` in your command line interface. Next, create an `.env` file following the `.env_template`. Once you have these prerequisites, you can clone the repository and run the server using the following command: `python manage.py runserver`.

This will start the server at `http://localhost:8000/`. You can then navigate to this URL in your web browser to access the forum.

## Contributing

Contributions to this project are welcome and encouraged. If you notice any issues or have any suggestions for improvement, please create a pull request or submit an issue.
