# start
import csv

CSVFILE = "EmployeePay.csv"


def main():
    # open
    infile = open(CSVFILE, "r", newline="")
    reader = csv.reader(infile)
    next(reader)

    # loop
    for row in reader:
        ident = row[0]
        fname = row[1]
        lname = row[2]
        salary = row[3]
        bonus = row[4]

        # display
        print(
            "Name (first and last):", fname, lname, "Salary:", salary, "Bonus:", bonus
        )

    infile.close()


main()
