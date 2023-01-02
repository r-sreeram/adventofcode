# adventofcode

Solutions to Advent of Code (<https://adventofcode.com>) problems.

## How to use

All Python programs take input from standard input and write the solution to standard output, one line per part. Usually
this means two lines of output, but there are exceptions:

* Day 25 for every year has only one part, so there's only one output line.
* Some solutions need OCR. Programs for those days use a hard-coded set of letter shapes in [ocr.py](lib/ocr.py) to
  output the solution, but they also write out the pixel grid so you can eyeball it manually. In these cases, the output
  will have more than two lines.

All Python code is intended to be used with the latest Python, which is 3.11 as of writing. No special libraries are
required (except for the aforementioned ocr.py).

## Contributions are welcome

If you have a better way to write any part of a solution (e.g., better algorithms, more idiomatic expressions, more
optimizations), please do send me pull requests!

## Work in progress

My goal is to fill out solutions for all problems for all years, but I'm far from achieving that goal. I also want to
add solutions in other languages, such as C++, Go, Java/Scala/Kotlin, Typescript and Rust. This repo is a work in
progress. I'll add more solutions as I get time. Check back from time to time!
