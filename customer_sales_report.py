# start
import csv

CSVFILE = "sales.csv"
NEWFILE = "salesreport.csv"

# open
infile = open(CSVFILE, "r", newline="")
outfile = open(NEWFILE, "w", newline="")

reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter=",")
next(reader)

# loop
customer_id = "250"
cust_total = 0

for i in reader:
    if customer_id != i[0]:
        outfile.write(customer_id + "\t" + str("%.2f" % cust_total) + "\n")
        customer_id = i[0]
        cust_total = 0
    total = float(i[3]) + float(i[4]) + float(i[5])
    cust_total += total

outfile.write(customer_id + "\t" + str("%.2f" % cust_total) + "\n")
# close
infile.close()
outfile.close()
