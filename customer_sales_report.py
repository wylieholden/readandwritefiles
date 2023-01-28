# start
import csv

CSVFILE = "sales.csv"


def main():
    # open
    infile = open(CSVFILE, "r", newline="")
    reader = csv.reader(infile)
    next(reader)

    # loop
    for row in reader:
        cust_id = row[0]
        if cust_id == cust_id:
            sales = row[3] + row[3]
        else:
            sales = 88

        # display
        print(sales)

    infile.close()


main()
