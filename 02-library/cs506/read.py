import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='"')

        ret = []
        for row in reader:
            curr_row = []
            for x in row[0].split(','):
                if x.isnumeric():
                    curr_row += [int(x)]
                else:
                    curr_row += [(x)]
            ret += [curr_row]
        
        return ret
