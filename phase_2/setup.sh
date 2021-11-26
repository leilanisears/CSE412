#retrieve files from Leilani's github
git clone https://github.com/leilanisears/CSE412.git
cd CSE412

#change to root user as this is the only user able to change to postgres user
sudo su
#change to user postgres
su postgres

#create specified database
createdb musicdb
