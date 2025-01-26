#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update the APT sources.list file to use the Debian archive for stretch
echo "Updating APT sources.list..."
cat <<EOF > /etc/apt/sources.list
deb http://archive.debian.org/debian stretch main
deb-src http://archive.debian.org/debian stretch main
deb http://archive.debian.org/debian-security stretch/updates main
deb-src http://archive.debian.org/debian-security stretch/updates main
EOF

# Display the updated sources.list for verification
echo "Updated APT sources.list:"
cat /etc/apt/sources.list

# Disable the "Check-Valid-Until" setting to avoid errors with outdated repository metadata
echo "Disabling APT valid-until checks..."
echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# Update the package list
echo "Updating package list..."
apt-get update -o Acquire::AllowInsecureRepositories=true

# Install Python
echo "Installing Python..."
apt-get install -y python

# Install Nano text editor
echo "Installing Nano..."
apt-get install -y nano

echo "Setup completed successfully!"
