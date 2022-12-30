#!/bin/bash -Eeu

# A simple script to run a bunch of programs and verify their output.

# Usage: run.sh [[years] days]

# Examples:
#   run.sh
#     => runs all the programs for 2022
#   run.sh "10 11 12"
#     => runs the programs for 2022-10, 2022-11, 2022-12
#   run.sh "2021 2022" "$(seq 1 25)"
#     => runs all the programs for 2021 and 2022

DIR=$(dirname "$0")/..
export TIMEFORMAT="%R"

function run() {
  year=$1
  day=$2
  echo -n $year-$day
  for input in $DIR/$year/$day/*-input.txt; do
    name=$(basename $input -input.txt)
    echo -n " | $name"
    { time /opt/homebrew/bin/python3.11 -O $DIR/$year/$year-$day.py < $input >/tmp/aoc.out; } 2>/tmp/aoc.time
    echo -n " ($(</tmp/aoc.time)s)"
    diff $DIR/$year/$day/$name-output.txt /tmp/aoc.out &>/dev/null || { echo " FAILED"; exit; }
  done
  echo
}

if [ $# = 2 ]; then
  years=$1
  days=$2
elif [ $# = 1 ]; then
  years=2022
  days=$1
else
  years=2022
  days=$(seq 1 25)
fi

for year in $years; do
  for day in $days; do
    run $year $day
  done
done
