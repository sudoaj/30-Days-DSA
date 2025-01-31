Here’s how the project should be run after cloning:

How to Run the Project
	1.	Clone the Repository

cd 30-Days-DSA/Day02_Jan17_2025/Wordle


	2.	Set Up the Environment
	•	Create a virtual environment:

pipenv shell



	•	Install dependencies:

pip install -r requirements.txt


Optional: Single Command for All Steps

You can run all the setup steps at once using the 0_RUNPROJ.sh script:

./0_RUNPROJ.sh

This script will:
	1.	Reset the database and migrations.
	2.	Create the superuser.
	3.	Generate users and players.
	4.	Add a daily word.
	5.	Start the Django development server.

Default Project Credentials
	•	Superuser:
	•	Username: aj
	•	Email: wordle@wordle.com
	•	Password: wordle2020
	•	Check the console output of ./3_create_user.sh for usernames and passwords.


or run it individually (chnage details if needed)

	3.	Reset Database and Migrations
	•	Run the reset script to remove previous migrations and reset the database:

./1_reset_migrations.sh


	4.	Create a Superuser
	•	Use the script to create a superuser with predefined credentials:

./2_create_super_user.sh


	•	Default credentials:
	•	Username: aj
	•	Email: wordle@wordle.com
	•	Password: wordle2020

	5.	Create Users
	•	Generate 10 creative users for testing:

./3_create_user.sh


	6.	Create Players
	•	Assign players to the users:

./4_create_player.sh


	7.	Create a Daily Word
	•	Add a valid 5-letter word for the daily game:

./5_create_words.sh


	8.	Run the Development Server
	•	Start the Django development server:

python manage.py runserver 127.0.0.1:8000


	9.	Access the Application
	•	Open the browser and navigate to http://127.0.0.1:8000/admin. to login with the default details 
,
Key Points from the Scripts
	•	Database Reset (1_reset_migrations.sh):
	•	Deletes all migration files except __init__.py.
	•	Removes the SQLite database and recreates migrations.
	•	Superuser Creation (2_create_super_user.sh):
	•	Automates the creation of a superuser with predefined credentials.
	•	User Creation (3_create_user.sh):
	•	Creates 10 users with random details like username, email, and password.
	•	Player Assignment (4_create_player.sh):
	•	Maps each user to a Player instance with random game stats.
	•	Daily Word Setup (5_create_words.sh):
	•	Adds a new daily word from a predefined list of 5-letter English words.

