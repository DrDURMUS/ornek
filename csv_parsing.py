import csv
'''with open('names.txt', 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    #for line in csv_reader:
        #print(line[2])
    with open('new_names', 'w') as new_csv:
        csv_writer=csv.writer(new_csv,delimiter='-')
        csv_writer = csv.writer(new_csv, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)'''
with open('names.txt','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('new_names_dic','w') as n_c_d:
        #fieldnames=['first_name', 'last_name', 'email']
        fieldnames=['first_name', 'last_name']
        csv_dicwri=csv.DictWriter(n_c_d, fieldnames=fieldnames, delimiter='\t')
        csv_dicwri.writeheader()
        for line in csv_reader:
            del line['email']
            csv_dicwri.writerow(line)
        #print(line['email'])
