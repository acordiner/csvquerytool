#!/bin/bash

set -e
set -o pipefail

VERSION_FILE="VERSION.txt"

if [ -f "$VERSION_FILE" ]; then
    deployed_version=$(cat "$DEPLOYED_TAG_FILE")
else
    deployed_version=""
fi
latest_version=$(hg tags | head -2 | tail -1 | awk '{print $1}')
if [ "$deployed_version" = "$latest_version" ]; then
    echo "Nothing to do (latest version $deployed_version already deployed)"
else
    echo "Deploying version $latest_version to production"
    package_version=$(python setup.py --version)
    if [ "$package_version" = "$latest_version" ]; then
        echo "Releasing new production version: $latest_version"
        python setup.py sdist upload
        echo "$latest_version" > $VERSION_FILE
    else
        echo "Error: package version ($package_version) != SCM tag ($latest_version); did you update setup.py and .hgtags?" >&2
        exit 1
    fi
fi
