# file_name
# from csv import writer
# from csv import reader
# # Open the input_file in read mode and output_file in write mode
# with open(file_name, 'r') as read_obj, \
#         open('GOOG1.csv', 'w', newline='') as write_obj:
#     # Create a csv.reader object from the input file object
#     csv_reader = reader(read_obj)
#     # Create a csv.writer object from the output file object
#     csv_writer = writer(write_obj)
#
#     # Add contents of list as last row in the csv file
#     list_of_elem=['Date','Open','High','Low','Close','Adj Close','Volume','Change']
#     csv_writer.writerow(list_of_elem)
#
#     for row in csv_reader:
#         # Append the default text in the row / list
#         row.append((float(row[1])-float(row[4]))/float(row[1]))
#         # Add the updated row / list to the output file
#         csv_writer.writerow(row)
#
#
# import csv
# with open('GOOG1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



def calculate_change(file_name):
    from csv import writer
    from csv import reader
    with open(file_name, 'r') as read_obj, \
            open(file_name+'1.csv', 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)


        for row in csv_reader:

            # Append the default text in the row / list
            row.append((float(row[1])-float(row[4]))/float(row[1]))
            # Add the updated row / list to the output file
            csv_writer.writerow(row)

    import csv
    with open(file_name+'1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    return print("File created")

calculate_change('GOOG.csv')