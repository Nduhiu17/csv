import csv

def generate_list(name):
    with open(name, 'r') as f:
        file = csv.reader(f)
        return list(file)




def generate_file(data,file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()


if __name__ == '__main__':
    musoni_list = generate_list("musoni.csv")
    empty_payments = []
    musoni_references = []
    empty_payments.append(musoni_list[0])
    for payment in musoni_list:
        if len(payment[17]) == 0:
            empty_payments.append(payment)
        else:
            musoni_references.append(payment[17])
    generate_file(empty_payments,'missing_references.csv')
    mpesa_list = generate_list("mpesa.csv")


    list_difference = []
    for payment in mpesa_list:
        if payment[0] not in musoni_references:
            list_difference.append(payment)


    generate_file(list_difference,"difference.csv")

