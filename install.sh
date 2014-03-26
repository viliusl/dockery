#!/bin/bash

#$1 - command, $2 - package
function check_dependency {
    command -v $1 >/dev/null 2>&1 || { echo "   '$2' is not installed - install it manually using ex. 'sudo apt-get install $1' on ubuntu, or whatever else way in your distro." >&2; exit 1; }
    echo "   Found '$1'."
}

function create_symlink {
    echo "Installing $2..."
    sudo ln -sf `pwd`$1 /usr/bin/$2
    echo -e "Installing $2... Done.\n"
}

echo "Checking dependencies..."
check_dependency python python
check_dependency pip python-pip
check_dependency docker
echo -e "Checking dependencies... Done.\n"

# install python libraries
echo "Downloading libraries..."
sudo -E easy_install pip
sudo -E easy_install colorama
sudo -E easy_install argparse
echo -e "Downloading libraries... Done.\n"

# creates command symlinks
create_symlink /dockery.py dockery

#echo "Don't forget to check configuration in ../.dockery/ and try one of the following:"
echo "Read README on how to initialize ssh properly."
echo ""
echo "Try one of the following:"
echo "      dockery"

echo "Cheers!"

# refresh shell for symlinks would be visible right away.
exec bash