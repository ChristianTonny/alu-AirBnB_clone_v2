#!/usr/bin/env bash
# Script that sets up web servers for deployment of web_static

# Function to handle errors but continue execution
handle_error() {
    echo "Warning: $1" >&2
}

# Update package list and install Nginx if not already installed
apt-get update -y >/dev/null 2>&1 || handle_error "Failed to update package list"
apt-get install -y nginx >/dev/null 2>&1 || handle_error "Failed to install nginx"

# Create required directories with proper permissions
mkdir -p /data/ || handle_error "Failed to create /data/"
mkdir -p /data/web_static/ || handle_error "Failed to create /data/web_static/"
mkdir -p /data/web_static/releases/ || handle_error "Failed to create /data/web_static/releases/"
mkdir -p /data/web_static/shared/ || handle_error "Failed to create /data/web_static/shared/"
mkdir -p /data/web_static/releases/test/ || handle_error "Failed to create /data/web_static/releases/test/"

# Create fake HTML file for testing
cat > /data/web_static/releases/test/index.html << 'EOF' || handle_error "Failed to create index.html"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Remove existing symbolic link if it exists and create new one
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current || handle_error "Failed to remove existing symlink"
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current || handle_error "Failed to create symlink"

# Give ownership of /data/ folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/ >/dev/null 2>&1 || handle_error "Failed to change ownership"

# Create backup of original nginx config if it exists
if [ -f /etc/nginx/sites-available/default ]; then
    cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup >/dev/null 2>&1
fi

# Update Nginx configuration
cat > /etc/nginx/sites-available/default << 'EOF'
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
		index index.html index.htm;
	}
}
EOF

# Test nginx configuration before restarting
if nginx -t >/dev/null 2>&1; then
    # Restart Nginx to apply changes
    service nginx restart >/dev/null 2>&1 || handle_error "Failed to restart nginx"
else
    # If config is invalid, restore backup
    if [ -f /etc/nginx/sites-available/default.backup ]; then
        mv /etc/nginx/sites-available/default.backup /etc/nginx/sites-available/default >/dev/null 2>&1
    fi
    handle_error "Invalid nginx configuration"
fi

# Ensure nginx is enabled and started
systemctl enable nginx >/dev/null 2>&1 || handle_error "Failed to enable nginx"
systemctl start nginx >/dev/null 2>&1 || handle_error "Failed to start nginx"

# Always exit successfully
exit 0 