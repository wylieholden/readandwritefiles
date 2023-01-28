# start
import csv

CSVFILE = "customers.csv"
NEWFILE = "customer_country.csv"


def main():
    # open
    infile = open(CSVFILE, "r", "newline=")
    outfile = open(NEWFILE, "w", "newline=")
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=",")
    next(reader)

    # loop
    for row in reader:
        fname = row[1]
        lname = row[2]
        country = row[4]

        # display
        writer.writerow("Name (first and last):", fname, lname, "Country:", country)
    infile.close()
    outfile.close()


main()
