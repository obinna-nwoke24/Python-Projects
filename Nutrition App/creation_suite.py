import Client
import excel_api
import client_api
import creation_api
import pdf_api

needs_input = ['yes', 'no']
clients = []
response = input("Do you need to input clients?: ")
preset = True

while response.lower() not in ['yes', 'no']:
    print("\nInvalid response!\nTry again...\n")
    response = input("Do you need to input clients?: ")

if response.lower() == 'yes':
    preset = False
    total = int(input("How many clients do you need to add? "))

    for number in range(total):
        print("\nCreating client #{}".format(number+1))
        new_client = creation_api.create_client_from_input()
        clients.append(new_client)
else:
    clients = client_api.load_preset()

excel_api.to_excel(clients, 'test_file.xlsx')
for client in clients:
    pdf_api.client_to_pdf(client, preset=preset)
