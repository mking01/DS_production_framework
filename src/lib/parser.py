## Imports data and creates objects ##

import sys
import pandas as pd
from configs import path, patient_file#, route_file, time_file, trend_file
from Patient import Patient

patients_df = pd.read_csv(path + patient_file).head(1)


# Clean and prep data



# Create patient class
# read patient rows into patient class
for index, row in patients_df.iterrows():

    # create empty list to hold all patients
    patients = []

    # match file features to class attributes
    id = patients_df['id'].iloc[index]
    sex = patients_df['sex'].iloc[index]
    birth_year = patients_df['birth_year'].iloc[index]
    region = patients_df['region'].iloc[index]
    group = patients_df['group'].iloc[index]
    infection_reason = patients_df['infection_reason'].iloc[index]
    infection_order = patients_df['infection_order'].iloc[index]
    contact_number = patients_df['contact_number'].iloc[index]
    released_date = patients_df['released_date'].iloc[index]
    deceased_date = patients_df['deceased_date'].iloc[index]
    state = patients_df['state'].iloc[index]

    # create a patient object, pass features to attributes
    patient = Patient(id=id, sex=sex, birth_year=birth_year, region=region, group=group,
                       infection_reason=infection_reason, infection_order=infection_order,
                       contact_number=contact_number, released_date=released_date, deceased_date=deceased_date,
                       state=state)

    print(patient.get_age())
    # append patient to list of patients
    #patients.append(patient)

    #for i in range(len(patients)):
    #    print(patients[i].age)


# Run ETL pipeline