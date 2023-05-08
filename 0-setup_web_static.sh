#!/usr/bin/env bash
#Bash script that sets up web servers for the deployment of web_static

#!/usr/bin/env bash

# Install Nginx if it not already installed
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null 
| grep -c "ok installed") -eq 0 ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file for testing
echo "<html><head><title>Test HTML file</title></head><body><p>This is a test
HTML file.</p></body></html>"
 | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content of /data/web_static/current/ to
 hbnb_static
sudo sed -i '/listen 80 default_server;/a\\n\tlocation /hbnb_static {\n\t\
talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
