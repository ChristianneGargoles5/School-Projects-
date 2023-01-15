# Obtain a starting image for the Apache Web Server
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=nonintercative
RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install sudo -y
RUN apt-get install apache2 -y

#Running user commands
ENV $USER =cg160746
RUN sudo adduser $USER
RUN sudo passwd -d $USER
RUN sudo usermod -aG sudo $USER

# Set the working directory to match DocumentRoot                                   
WORKDIR /home/$USER/public_html
#Running sudo a2enmod 
RUN sudo a2enmod userdir
RUN sudo a2enmod autoindex

# Copy your index.html file to DocumentRoot directory               
COPY index.html .
RUN mv index.html christianne.html
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Add in other directives as needed
LABEL Maintainer: "christianne.gargoles.439@my.csun.edu"
EXPOSE 80
CMD apache2ctl -D FOREGROUND

#CMD service apache2 restart

#EXEC

