#!/bin/bash

set -e

referenceImage='./images/george1e.jpeg'

if [ ! -d "./images" ] ; then
    echo "Directory images does not exist."
    exit 1
fi

if [ ! -f "./images/george1e_resized.jpeg" ] ; then
    echo "File george1e_resized.jpeg does not exist. Resizing..."
    python3 resize.py "$referenceImage" '100'
fi

if [ ! -f "./images/george1e_scaled.jpeg" ] ; then
    echo "File george1e_scaled.jpeg does not exist. Resizing..."
    python3 scale.py "$referenceImage"
fi

if [ ! -f "./images/salt-and-pepper-george.jpeg" ] ; then
    echo "File salt-and-pepper-george.jpeg does not exist. Resizing..."
    python3 rotate.py "$referenceImage"
fi

sleep 5

execute_comparison() {
    local algorithm="$1"
    echo "Algorithm: $algorithm"
    for angle in "45" "90" "135" "180"; do
        time python3 -W ignore compare_degree.py "$algorithm" "$referenceImage" "$angle"
    done
}

execute_comparison 'sift'
execute_comparison 'orb'

time python3 -W ignore compare_degree.py "sift" "$referenceImage" '1'
time python3 -W ignore compare_degree.py "orb" "$referenceImage" '1'

time python3 -W ignore compare_degree.py "sift" "$referenceImage" '2'
time python3 -W ignore compare_degree.py "orb" "$referenceImage" '2'

