### patient
7382 confirmed participants as of March 9, 2020.
- id: patient ID
- sex: patient gender
- birth_year: patient birth year
- country: nationality
  - China, South Korea, or Mongolia
- region: Primary activity area (by metro area / province)
  - capital area: Seoul, Incheon, Gyeonggi-do
  - filtered at airport: Inactive after airport quarantine
  - Busan
  - Daegu
  - Gwangju 
  - Ulsan
  - Gangwon - do
  - Chungcheongbuk - do
  - Chungcheongnam - do
  - Jeollabuk - do
  - Gyeongsangbuk - do
  - Gyeongsangnam - do
  - Jeju - do
- disease: Underlying disease
  - 0, no underlying disease, or 1, underlying disease
- group: Underlying groups (? not totally sure without looking at the data what that means)
  - Shincheonji Church, Cheongdo Daenam Hospital, Eunpyeong St. Mary's Hospital, Onchun Church, Myungsung Church, Pilgrimage
- infection_reason: How a patient became infected
  - Visited infected country or city
  - Contact with infected person (domestic)
  - Contacted with infected person (international)
  - Wuhan resident
  - Pilgrimage to Israel
- infection_order: Degree of infection (nth infection)
- infected_by: ID of who the patient was infected by
- contact_number: contact number
- confirmed_date: Date confirmed 
- released_date: Date released
- deceased_date: Date deceased
- state: condition
  - isolated: hospitalized in isolation
  - released: discharged (uncontained)
  - deceased: passed away

### route
Information about the path of the patient.
- id: Patient ID
- date: travel date
- province: state or province visited
- city: city visited
- visit: Places visited (type)
  - airport
  - hospital
  - hospital, isolation unit
  - clinic
  - hotel
  - store
  - market
  - restaurant 
  - cafe 
  - company
  - bus terminal
  - train station
  - movie theater
  - hair salon
  - church
  - other
- latitude: latitude of location visited
- longitude: longitude of location visited

### time
Daily testing results and status information.
- date
- acc_test: Cumulative checks, including ongoing checks
- acc_negative: Cumulative negative results
- acc_confirmed: Cumulative positive results
- acc_released: Cumulative isolation count
- acc_deceased: Cumulative deaths
- new_test: New checks
- new_negative: New negative results
- new_confirmed: New positive results
- new_released: New quarantines released
- new_deceased: New deaths

### trend
Keyword search volume information for COVID-19 by date.
- date
- cold: Cold search volume
- flu: Flu search volume
- pneumonia: Pneumonia search volume
- coronavirus: Coronavirus search volume
