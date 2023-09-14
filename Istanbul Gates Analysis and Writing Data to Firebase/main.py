import firebase_admin
from firebase_admin import credentials, db
import csv
from tabulate import tabulate

cred=credentials.Certificate('example.json')
firebase_admin.initialize_app(cred,{'databaseURL': "https://firebaseio.com"})


def add_database():
    csv_file = "gate.csv" 
    data_to_add = []

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:

            if 'GATE_NAME' in row:
                row['GATE_NAME'] = row['GATE_NAME'].lower()
            data_to_add.append(row)

    ref = db.reference('example')  
    ref.set(data_to_add)
    print('The data in the CSV file has been added to the Firebase database!')


def delete_data_by_name(gate_name):
    ref = db.reference('example')
    data_snapshot = ref.get()
    deleted = False

    if data_snapshot:
        for key, data in enumerate(data_snapshot):
            if data is not None and 'GATE_NAME' in data and data['GATE_NAME'].lower() == gate_name.lower():
                ref.child(str(key)).delete()
                print(f"{gate_name} the data named has been deleted from the Firebase database.")
                deleted = True
                break  

        if not deleted:
            print(f"{gate_name} data named was not found in Firebase database!")
    else:
        print("No data found in Firebase database!")


def get_data_by_gate_name(gate_name):
    ref = db.reference('example')
    data_snapshot = ref.get()

    if data_snapshot:
        found = False
        gate_name = gate_name.lower() 

        for data in data_snapshot:
            if data is not None and 'GATE_NAME' in data and data['GATE_NAME'].lower() == gate_name:
                found = True
                print(f"GATE_NAME : {data['GATE_NAME']}")
                print(f"GATE_TYPE : {data['GATE_TYPE']}")
                print(f"COUNTY_NAME : {data['COUNTY_NAME']}")
                print(f"NEIGHBORHOOD_NAME : {data['NEIGHBORHOOD_NAME']}")
                print(f"LOCATION : {data['LOCATION']}")
                print(f"STREET_NAME : {data['STREET_NAME']}")
                print(f"LATITUDE : {data['LATITUDE']}")
                print(f"LONGITUDE : {data['LONGITUDE']}")

        if not found:
            print(f"'{gate_name}' Gate Name was not found!")
    else:
        print("No data found in Firebase database!")


def get_all_name():
    ref = db.reference('example')
    data_snapshot = ref.get()

    if data_snapshot is not None:
        gate_names = set()

        for data in data_snapshot:
            if isinstance(data, dict) and 'GATE_NAME' in data:
                gate_name = data['GATE_NAME'].strip()
                gate_names.add(gate_name)

        if gate_names:
            gate_name_list = list(enumerate(gate_names, start=1))
            table = tabulate(gate_name_list, headers=['Sequence Number', 'Gate Name'], tablefmt='simple')
            
            print(table)
        else:
            print("Gate Name not found in Firebase database!")
    else:
        print("No data found in Firebase database!")


def all_delete():
    ref=db.reference('example')
    ref.delete()


while True:
    print('Add dataset to firebase ----------->add\nDelete dataset from firebas ----------->delete\nDelete data by name ----------->delname\nGate name info ----------->info\nGet all gate names ----------->allnames\nQuit ----------->disconnect')

    choice = input('Choose section : ')
    if choice=='add':
        add_database()
    
    elif choice=='delete':
        all_delete()

    elif choice=='delname':
        gotname=input('Enter the gate name to be deleted : ')
        delete_data_by_name(gotname)

    elif choice=='info':
        print('-'*100)
        gotnameinfo=input('Enter the Gate Name whose information you want to get : ')
        get_data_by_gate_name(gotnameinfo)
    
    elif choice=='allnames':
        get_all_name()

    elif choice=='disconnect':
        break
    
    else:
        print('Invalid action selection. Please try again!')

    print('-'*100)
