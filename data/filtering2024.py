import csv
import argparse
from datetime import datetime
from collections import defaultdict

def main():
    with open("311_Service.csv") as f, \
    open("filtered2024.csv", "w") as w:
    
        reader = csv.DictReader(f)
        writer = csv.DictWriter(w, fieldnames=reader.fieldnames)
        writer.writeheader


        for row in reader: 
            c_date = datetime.strptime(row["Created Date"].split()[0], "%m/%d/%Y")
            if c_date.year == 2024: 
                writer.writerow(row)
            
    

if __name__ == "__main__":
    main()