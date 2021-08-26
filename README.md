# Ariel_observatory

Final project in ariel university

By Shilo gilor & Amiel Liberman

## How to use this git?

1) Open AWS account for free

2) Make a ubuntu server

3) How to connect to a ubuntu server on AWS

4) Installing programs

5) Git clone 

6) common commands

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
