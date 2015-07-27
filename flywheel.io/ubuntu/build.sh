#!/bin/bash -e

# Prepare apt-get for usage
. /helper/scripts/apt-get/bootstrap.sh
. /helper/scripts/apt-get/update.sh

# Upgrades from ubuntu
apt-get dist-upgrade -y

# Simple, small utilities that are convenient for ubiquitous availability
packages=()
packages+=("sudo")
packages+=("screen")
packages+=("wget")
packages+=("curl")
packages+=("htop")
packages+=("nano")  #  194 kB
packages+=("socat") # 1142 kB
packages+=("software-properties-common") # may be required for add-apt-repository

apt-get install -y "${packages[@]}"


#
# Locales can be a real pain inside containers.
# These simple steps can avoid real confusion later.
#

# List installed locales
locale -a

# Generate desired locale
locale-gen en_US.utf8

# Set new locale as default permanently
# This generates, among other things, /etc/default/locale
update-locale LANG=en_US.utf8

# You should now see your locale installed
locale -a | grep "en_US.utf8"

# Confirm
cat /etc/default/locale

# Cleanup
. /helper/scripts/apt-get/clean.sh
