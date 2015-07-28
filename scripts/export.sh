#!/bin/bash -e

(
	# Set cwd
	unset CDPATH
	cd "$( dirname "${BASH_SOURCE[0]}" )"/..

	# Use bundled binaries
	export PATH=`pwd`/bin:$PATH

	images=(`docker images | cut -f 1 -d ' ' | egrep '(index.docker.IO|scitran.io)' | sort | uniq`)
	date=`date +%Y-%m-%d`
	githash=`git --no-pager log --pretty=format:"%h" -n 1`

	mkdir -p export

	# State. State... never changes.
	docker rm "export-me" > /dev/null 2> /dev/null || true

	for image in "${images[@]}"; do
		echo "Exporting $image..."

		imageName=`echo $image | sed 's$/$-$g' | sed 's/IO/io/g'`
		filename="$imageName--$date--$githash.tar.gz"

		# Docker can't export images :|
		docker run --name "export-me" $image /bin/true
		docker export "export-me" | gzip > export/$filename
		docker rm "export-me" > /dev/null

		echo -e '\t'Wrote $filename
	done
)
