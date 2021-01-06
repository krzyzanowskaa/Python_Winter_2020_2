def calculate_change(file):
    file_name = file + '.csv'
    from csv import writer
    from csv import reader
    with open(file_name, 'r') as read_obj, \
            open(file + '1.csv', 'w', newline='') as write_obj:
        
        csv_reader = reader(read_obj)
        
        csv_writer = writer(write_obj)

        csv_read = list(csv_reader)

        for row in csv_read[:1]:
            line = ('Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Change')
            row.append(line)
            csv_writer.writerow(line)

        for row in csv_read[1:]:
            row.append((float(row[4])-float(row[1]))/float(row[1]))
            # Add the updated row / list to the output file
            csv_writer.writerow(row)


    import csv
    with open(file+'1.csv', 'r') as file:
        reader = csv.reader(file)
    return print("File created")

calculate_change('IBM')
