#!/bin/bash -e

(
	# Set cwd
	unset CDPATH
	cd "$( dirname "${BASH_SOURCE[0]}" )"/..

	# Ensure bundled binaries
	test -f bin/docker -a -f bin/hroot || (
		mkdir -p bin; cd bin
		curl https://storage.googleapis.com/scitran-dist/prod-releases/hana/docker-hroot-bundle.tar.gz | tar -xz
	)

	# Use bundled binaries
	export PATH=`pwd`/bin:$PATH

	# Check bundled binaries
	hroot version
	docker version 2>/dev/null || true  # `docker version` exits non-zero if daemon not running. you can't make this stuff up.

	# This duration needs to be long enough to run and cleanly shut down.
	# Hackaround for a sleep-try-loop that waits for docker to be up.
	waitSeconds="5"

	# Daemon, debug, no restart, disposable state dir
	docker -d -D -r=false --graph `pwd`/flak &
	dockerPID=$!
	sleep 0.5; echo "Waiting for docker to boot..."; sleep $waitSeconds

	time ./scripts/build.sh

	# Kill
	kill -INT $dockerPID
	sleep 0.5; echo "Waiting for docker to die..."; sleep $waitSeconds
	rm -rf flak || true # Who knows if state-nuking will be successful

	# Print audit log
	( cd graph && git --no-pager log --graph --all --pretty=format:"%Cred%h%Creset%C(yellow)%d%Creset %s %Cgreen%cr %Creset" )
	echo

	# Print graph size
	echo "Graph size: `du -h -d 0 graph/ | cut -f 1`"
)
