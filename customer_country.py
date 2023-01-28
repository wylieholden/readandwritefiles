# start
import csv

CSVFILE = "customers.csv"
NEWFILE = "customer_country.csv"


def main():
    # open
    infile = open(CSVFILE, "r", newline="")
    outfile = open(NEWFILE, "w", newline="")

    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=",")
    next(reader)

    header = ["First Name", "Last Name", "Country"]
    writer.writerow(header)
    # loop
    for row in reader:
        fname = row[1]
        lname = row[2]
        country = row[4]

        # display
        new_row = [fname, lname, country]
        writer.writerow(new_row)
    infile.close()
    outfile.close()


main()
