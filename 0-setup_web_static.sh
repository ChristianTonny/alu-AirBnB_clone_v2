#!/usr/bin/env bash
# Script that sets up web servers for deployment of web_static

# Update package list and install Nginx if not already installed
apt-get update -y
apt-get install -y nginx

# Create required directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create fake HTML file for testing
cat << 'EOF' > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Remove existing symbolic link if it exists and create new one
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
# Create or update the Nginx site configuration
cat << 'EOF' > /etc/nginx/sites-available/default
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
EOF

# Restart Nginx to apply changes
service nginx restart

# Exit successfully
exit 0 