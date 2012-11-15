#!/bin/bash

set -e
set -o pipefail

# This script builds the latest Python module and uploads it to Pypi. It keeps 
# a record of the latest uploaded version in $VERSION_FILE, and only uploads
# a new module if a new version has been tagged. The steps are:
#
#     1. Run "hg tags" and find the latest tag name that comes after the tip.
#        e.g. "1.2.0"
#     2. If $VERSION_FILE contains the string "1.2.0" then exit
#     3. Build the module "foobar-1.2.0.tar.gz" and upload it to Pypi
#     4. Write the string "1.2.0" to $VERSION_FILE

VERSION_FILE="VERSION.txt"

if [ -f "$VERSION_FILE" ]; then
    deployed_version=$(cat "$VERSION_FILE")
else
    deployed_version=""
fi
latest_version=$(hg tags | head -2 | tail -1 | awk '{print $1}')
if [ "$deployed_version" = "$latest_version" ]; then
    echo "Nothing to do (latest version $deployed_version already deployed)"
else
    echo "Deploying version $latest_version to production"
    module_version=$(python setup.py --version)
    if [ "$module_version" = "$latest_version" ]; then
        echo "Releasing new production version: $latest_version"
        distutils_output=$(python setup.py sdist upload 2>&1)
        echo "$distutils_output"
        if echo "$distutils_output" | grep "^Upload failed" >/dev/null; then
            # setup.py returns an exit status of 0 even if the upload fails, so need to check the output
            # see distutils issue #245: https://bitbucket.org/tarek/distribute/issue/245/python-setuppy-should-return-a-non-zero
            echo "Error: pypi upload failed (if you manually upload the file, remember to update $VERSION_FILE)" >&2
            exit 1
        fi
        echo "$latest_version" > $VERSION_FILE
    else
        echo "Error: module version ($module_version) != SCM tag ($latest_version); did you update setup.py and .hgtags?" >&2
        exit 1
    fi
fi
