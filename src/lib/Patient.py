# Create patient class for all patients in patient file

class Patient:
    '''
    id (int): patient identifier, unique
    sex (string): patient gender
    birth_year (year): year patient was born
    region (string): region patient is from
    group (string): additional affiliation of patient
    infection_reason (string): how patient became infected
    infection_order (int): reason 1-5 the patient was infected
    contact_number (int)
    confirmed_date (date): date confirmed
    released_date (date): date released
    deceased_date (date): date passed away
    state (string): outcome - released, isolated, deceased
    '''

    def __init__(self, id, sex, birth_year, region, group, infection_reason, infection_order, contact_number,
                 released_date, deceased_date, state):
        self.id = id
        self.sex = sex
        self.birth_year = birth_year
        self.region = region
        self.group = group
        self.infection_reason = infection_reason
        self.infection_order = infection_order
        self.contact_number = contact_number
        self.released_date = released_date
        self.deceased_date = deceased_date
        self.state = state
        self.age = []

        def get_age(self):
            #import datetime as datetime
            #today = datetime.now()
            self.age.append(0) #today.dt.year - self.birth_year
            return self.age
