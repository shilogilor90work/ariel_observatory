# Ariel_observatory

Final project in ariel university

By Shilo gilor & Amiel Liberman

## How to use this git?

1) Open AWS account for free

2) Make a ubuntu server

3) How to connect to a ubuntu server on AWS

4) Installing programs

5) Git clone 

6) Common commands

7) Q&A

### Open AWS account for free

A link of step by step how to make a AWS account:

https://www.youtube.com/watch?v=gA9pl-A9gDM

### Make a ubuntu server

A link of step by step how to make a ubuntu server:

https://www.youtube.com/watch?v=4JL_iTanFtQ

Few notes:

1) In min 5:25 add an HTTP(port 80) HTTPS(port 443) and SSH(port 22) 

2) Download and save the key to login later

### How to connect to a ubuntu server on AWS

In the last minutes in the youtube link there are 2 ways to go into the server.

I will show one more way to log in with putty:

1) Go into this link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

2) Download putty.exe

3) Download pageant.exe

4) Add the key download and add it to pageant

5) Open putty and put the IP( you have in the AWS EC2 Dashboard -> Instances -> Public IPv4 address)

6) Press open

7) Write in the terminal: "ubuntu"


### Installing programs

Now we need to install some software for the first time you login

Copy paste it into terminal and let it install 

This will take some time with some installing  

1) sudo apt-get update

2) sudo apt install python3-pip

3) pip3 --version

4) sudo pip3 install Django==2.1.*

5) sudo apt install git-all

6) Install chrome it have some steps as:

6.a) sudo apt update

6.b) sudo apt install unzip libnss3 python3-pip

6.c) cd /tmp/

6.d) sudo wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip

6.e) sudo unzip chromedriver_linux64.zip

6.f) sudo mv chromedriver /usr/bin/chromedriver

6.g) chromedriver --version (make sure its not an error)

7) sudo apt-get install libxss1 libappindicator1 libindicator7

8) wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

9) sudo apt install ./google-chrome*.deb

10) sudo apt-get install -f

11) pip3 install selenium – user

12) pip3 install django-celery

### Git clone

To copy the git to the server copy paste this code:

git clone https://github.com/shilogilor90work/ariel_observatory.git


###  Common commands

Where is the app is running and where you need to run it:

cd ariel_observatory/weather

To run the server :

sudo python3 manage.py runserver 0.0.0.0:80

When you run the server and you get a message to makemigrations do the code here:

1) python3 manage.py makemigrations

2) python3 manage.py migrate

Try code in python on the server :

python3 manage.py shell

when you fisrt time using the server you will need to create red/green/yellow in the shell:

1) from forecast.models import Rules

2) Rules.objects.create(status_type="Red")

3) Rules.objects.create(status_type="Yellow")

4) Rules.objects.create(status_type="Green")

You can manualy make a update to the data base and scrpe with this code when in shell.

Update currnet manualy:

from forecast.extraction.scraping_IMS_current import scrape_IMS_current

scrape_IMS_current()

Update weekly manualy:

from forecast.extraction.scraping_IMS_weekly import scrape_IMS_weekly

scrape_IMS_weekly()

If you try to run the serever and server say port is not available.

To kill port 80 spam this till no DIP is alive:

sudo fuser -k 80/tcp

Now try to run server again it will work


### Q&A

Q) Where is the HTML files?

A) The HTML files are in -> ariel_observatory/weather/forecast/templates

Q) What is the purpse of each HTML? 

A) There 3 HTML files: 

base.html  Is the templets of the HTML files

dashboard.html Is to show of the data base 

rules.html Is the rule base to show current status

Q) Where is the CSS/js

A) The CSS/js files are in ->ariel_observatory/weather/forecast/static

Q) What is status green/yellow/red?

A) Status is how safe is the weather we made 3 defaults status:

Green is safe

Yellow is the middle from safe to not safe 

Red is not safe

Q) Where is the scraping code store?

A) the scrape code is here -> ariel_observatory/weather/forecast/extraction

Q) what are the config file for?

A) the config file are for editing the basic info like API/what site to scrape/and more

Q) How to add more paths to use in the site?

A) You can more path here ->ariel_observatory/weather/forecast/urls.py

Q) How to edit the time of the automatic scraping?

A) You can edit them in this file -> ariel_observatory/weather/forecast/tasks.py

Q) Can i more automatic runs there?

A) Yes

Q) Can i scrape other sites that are not ariel?

A) YES 

All you need to do is to change in the config.py files the  "zone_ariel" = the site you want

1) You can see what site here https://ims.gov.il/he/Stations

2) Then press the info inside

3) Look for station number 
