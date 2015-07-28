#!/bin/bash -e

(
	# Set cwd
	unset CDPATH
	cd "$( dirname "${BASH_SOURCE[0]}" )"/..

	apt-get update -y -qq

	# Disable post-install autorun
	echo exit 101 | tee /usr/sbin/policy-rc.d
	chmod +x /usr/sbin/policy-rc.d

	# Install dependencies
	apt-get install -y -q slirp lxc aufs-tools cgroup-lite

	# Git
	git config --global user.email "travis@example.com"
	git config --global user.name "Travis Touchdown"

	cat /proc/cgroups

	# Script
	./scripts/build-all.sh
)
