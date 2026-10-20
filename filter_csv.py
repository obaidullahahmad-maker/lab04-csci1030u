# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    # TODO: open args.filename and read it with csv.reader.
    file = csv.reader(open(args.filename))

    # The first row is the header.
    header = next(file)

    #   Find the position of args.column

    index_col = header.index(args.column)
    # print(header.index(args.column))

    for row in file:
        if row[index_col] == args.value:
            # "-".join(["a", "b"])   # gives "a-b"
            print(",".join(row))
    #  within the header, then print every data row
    #  (its values joined by commas) whose value in
    #  that column equals args.value.

    #     print(row)
if __name__ == "__main__":
    main()

# people.csv

# name,city,age
# Alice,Oshawa,30
# Bob,Toronto,25
# Cara,Oshawa,41
# Dan,Whitby,52
