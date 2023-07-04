from dotenv import load_dotenv
import os
import requests
import matplotlib.pyplot as plt

load_dotenv()  # Take environmental variables from .env

BLS_key = os.getenv("BLS_key")

private_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000000500000001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(private_url)
data = response.json()
series_data = data['Results']['series'][0]['data']

months = []
employment = []
job_may_19 = 0
job_may_23 = 0

for data_point in series_data:
    year = int(data_point['year'])
    period = data_point['period']
    job = float(data_point['value'])

    if period == 'M05' and year == 2019:
        job_may_19 = job
        print(f"Private Sector Jobs in May 2019: {job_may_19}")

for data_point in series_data:
    year = int(data_point['year'])
    period = data_point['period']
    job = float(data_point['value'])
    months.append(year + int(period[1:])/12)  # Combine year and month as a decimal for x-axis
    employment.append(job)

    if period == 'M05' and year == 2023:
        job_may_23 = job
        print(f"Private Sector Jobs in May 2023: {job_may_23}")

plt.plot(months, employment)
plt.xlabel('Year and Month')
plt.ylabel('Jobs in thousands')
plt.title('Private Sector Jobs in Massachusetts by Month')
plt.show()

local_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25716509093000001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(local_url)
data = response.json()
local_data = data['Results']['series'][0]['data']

local_months = []
local_jobs = []
local_job_may_19 = 0
local_job_may_23 = 0

for data_point in local_data:
    local_year = int(data_point['year'])
    local_period = data_point['period']
    local_job = float(data_point['value'])
    local_months.append(local_year + int(local_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    local_jobs.append(local_job)

    if local_period == 'M05' and local_year == 2019:
        local_job_may_19 = local_job
        print(f"Local Government Jobs in May 2019: {local_job_may_19}")

for data_point in local_data:
    local_year = int(data_point['year'])
    local_period = data_point['period']
    local_job = float(data_point['value'])

    if local_period == 'M05' and local_year == 2023:
        local_job_may_23 = local_job
        print(f"Local Government Jobs in May 2023: {local_job_may_23}")

plt.plot(local_months, local_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('Local Govt Jobs in Massachusetts by Month')
plt.show()


state_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000009092000001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(state_url)
data = response.json()
state_data = data['Results']['series'][0]['data']

state_months = []
state_jobs = []
state_job_may_19 = 0
state_job_may_23 = 0

for data_point in state_data:
    state_year = int(data_point['year'])
    state_period = data_point['period']
    state_job = float(data_point['value'])
    state_months.append(state_year + int(state_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    state_jobs.append(state_job)

    if state_period == 'M05' and state_year == 2019:
        state_job_may_19 = state_job
        print(f"State Government Jobs in May 2019: {state_job_may_19}")

for data_point in state_data:
    state_year = int(data_point['year'])
    state_period = data_point['period']
    state_job = float(data_point['value'])

    if state_period == 'M05' and state_year == 2023:
        state_job_may_23 = state_job
        print(f"State Government Jobs in May 2023: {state_job_may_23}")

plt.plot(state_months, state_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('State Govt Jobs in Massachusetts by Month')
plt.show()

#job_may_19 = 0
#job_may_23 = 0

#public_job_may_19 = 0
#public_job_may_23 = 0

#calculate if private jobs have recovered
if job_may_23 >= job_may_19:
    print("Private sector jobs in MA have recovered since the pandemic")
else:
    print("Private sector jobs in MA have not recovered since the pandemic")

print('')

#calculate if state government jobs have recovered
if local_job_may_23 >= local_job_may_19:
    print("Local government jobs in MA have recovered since the pandemic")
else:
    print("Local government jobs in MA have not recovered since the pandemic")

print('')

#calculate if state government jobs have recovered
if state_job_may_23 >= state_job_may_19:
    print("State government jobs in MA have recovered since the pandemic")
else:
    print("State government jobs in MA have not recovered since the pandemic")

print('')

#calculate what percentage of private jobs have been recovered
percentage_private_recovered = (job_may_23 / job_may_19)
print(f"Percentage of private sector jobs recovered:{percentage_private_recovered}%")
loss_Job = job_may_23 - job_may_19
loss_Job_change = (loss_Job / job_may_19)

if loss_Job < 0:
    loss_Job_change = round(abs(loss_Job_change)*100)
    print(f"That's a {loss_Job_change} percent drop.")
    loss_Job = round(abs(loss_Job)*1000)
    print(f"{loss_Job} private sector jobs have been lost.")
else:
    loss_Job_change = round(abs(loss_Job_change)*100)
    print(f"That's a {loss_Job_change} percent gain.")
    loss_Job = round(abs(loss_Job)*1000)
    print(f"{loss_Job} private sector jobs have been gained.")

print('')

#calculate what percentage of local government jobs have been recovered
percentage_local_recovered = (local_job_may_23 / local_job_may_19)
print(f"Percentage of local government jobs recovered:{percentage_local_recovered}%")
loss_local = local_job_may_23 - local_job_may_19
loss_local_change = (loss_local / local_job_may_19)

if loss_local < 0:
    loss_local_change = round(abs(loss_local_change)*100)
    print(f"That's a {loss_local_change} percent drop.")
    loss_local =round(abs(loss_local)*1000)
    print(f"{loss_local} local government jobs have been lost.")
else:
    loss_local_change = round(abs(loss_local_change)*100)
    print(f"That's a {loss_local_change} percent gain.")
    loss_local = round(abs(loss_local)*1000)
    print(f"{loss_local} local government jobs have been gained.")

print('')

#calculate what percentage of state jobs have been recovered
percentage_state_recovered = (state_job_may_23 / state_job_may_19)
print(f"Percentage of state government jobs recovered:{percentage_state_recovered}%")
loss_state = state_job_may_23 - state_job_may_19
loss_state_change = (loss_state / state_job_may_19)

if loss_state < 0:
    loss_state_change = round(abs(loss_state_change)*100)
    print(f"That's a {loss_state_change} percent drop.")
    loss_state = round(abs(loss_state)*1000)
    print(f"{loss_state} state government jobs have been lost.")
else:
    loss_state_change = round(abs(loss_state_change)*100)
    print(f"That's a {loss_state_change} percent gain.")
    loss_state = round(abs(loss_state)*1000)
    print(f"{loss_state}  state government jobs have been gained.")

print('')

###state government excluding education
NoEd_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000009092200001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(NoEd_url)
data = response.json()
NoEd_data = data['Results']['series'][0]['data']

NoEd_months = []
NoEd_jobs = []
NoEd_job_may_19 = 0
NoEd_job_may_23 = 0

for data_point in NoEd_data:
    NoEd_year = int(data_point['year'])
    NoEd_period = data_point['period']
    NoEd_job = float(data_point['value'])
    NoEd_months.append(NoEd_year + int(NoEd_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    NoEd_jobs.append(NoEd_job)

    if NoEd_period == 'M05' and NoEd_year == 2019:
        NoEd_job_may_19 = NoEd_job
        print(f"State Government (Excluding Education) Jobs in May 2019: {NoEd_job_may_19}")

for data_point in NoEd_data:
    NoEd_year = int(data_point['year'])
    NoEd_period = data_point['period']
    NoEd_job = float(data_point['value'])

    if NoEd_period == 'M05' and NoEd_year == 2023:
        NoEd_job_may_23 = NoEd_job
        print(f"State Government (Excluding Education) Jobs in May 2023: {NoEd_job_may_23}")

plt.plot(NoEd_months, NoEd_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('State Govt Jobs (Excluding Education) in Massachusetts by Month')
plt.show()


###state government education
Ed_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000009092161101?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(Ed_url)
data = response.json()
Ed_data = data['Results']['series'][0]['data']

Ed_months = []
Ed_jobs = []
Ed_job_may_19 = 0
Ed_job_may_23 = 0

for data_point in Ed_data:
    Ed_year = int(data_point['year'])
    Ed_period = data_point['period']
    Ed_job = float(data_point['value'])
    Ed_months.append(Ed_year + int(Ed_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    Ed_jobs.append(Ed_job)

    if Ed_period == 'M05' and Ed_year == 2019:
        Ed_job_may_19 = Ed_job
        print(f"State Government Education Jobs in May 2019: {Ed_job_may_19}")

for data_point in Ed_data:
    Ed_year = int(data_point['year'])
    Ed_period = data_point['period']
    Ed_job = float(data_point['value'])

    if Ed_period == 'M05' and Ed_year == 2023:
        Ed_job_may_23 = Ed_job
        print(f"State Government Education Jobs in May 2023: {Ed_job_may_23}")

plt.plot(Ed_months, Ed_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('State Govt Jobs Education in Massachusetts by Month')
plt.show()

###state government hospitals
Hosp_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000009092262201?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(Hosp_url)
data = response.json()
Hosp_data = data['Results']['series'][0]['data']

Hosp_months = []
Hosp_jobs = []
Hosp_job_may_19 = 0
Hosp_job_may_23 = 0

for data_point in Hosp_data:
    Hosp_year = int(data_point['year'])
    Hosp_period = data_point['period']
    Hosp_job = float(data_point['value'])
    Hosp_months.append(Hosp_year + int(Hosp_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    Hosp_jobs.append(Hosp_job)

    if Hosp_period == 'M05' and Hosp_year == 2019:
        Hosp_job_may_19 = Hosp_job
        print(f"State Government Hospital Jobs in May 2019: {Hosp_job_may_19}")

for data_point in Hosp_data:
    Hosp_year = int(data_point['year'])
    Hosp_period = data_point['period']
    Hosp_job = float(data_point['value'])

    if Hosp_period == 'M05' and Hosp_year == 2023:
        Hosp_job_may_23 = Hosp_job
        print(f"State Government Hospital Jobs in May 2023: {Hosp_job_may_23}")

plt.plot(Hosp_months, Hosp_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('State Govt Hospital Jobs in MA by Month')
plt.show()


#NoEd_job_may_19 = 0
#NoEd_job_may_23 = 0
#Ed_job_may_19 = 0
#Ed_job_may_23 = 0
#Hosp_job_may_19 = 0
#Hosp_job_may_23 = 0

print('')

#calculate if state government jobs excluding education have recovered
if NoEd_job_may_23 >= NoEd_job_may_19:
    print("State government jobs excluding education in MA have recovered since the pandemic")
else:
    print("State government jobs excluding education have not recovered since the pandemic")

print('')

#calculate if state government education jobs have recovered
if Ed_job_may_23 >= Ed_job_may_19:
    print("State government education jobs in MA have recovered since the pandemic")
else:
    print("State government education jobs in MA have not recovered since the pandemic")

print('')

#calculate if state government hospital jobs have recovered
if Hosp_job_may_23 >= Hosp_job_may_19:
    print("State government hospital jobs in MA have recovered since the pandemic")
else:
    print("State government hospital jobs in MA have not recovered since the pandemic")

print('')

#calculate what percentage of state government jobs excluding education jobs have been recovered
percentage_NoEd_recovered = (NoEd_job_may_23 / NoEd_job_may_19)
loss_NoEd = NoEd_job_may_23 - NoEd_job_may_19
loss_NoEd_change = (loss_NoEd / Ed_job_may_19)
print(f"Percentage of state government jobs (excluding education) recovered:{percentage_NoEd_recovered}%")

if loss_NoEd < 0:
    loss_NoEd_change = round(abs(loss_NoEd_change)*100)
    print(f"That's a {loss_NoEd_change} percent drop.")
    loss_NoEd = round(abs(loss_NoEd)*1000)
    print(f"{loss_NoEd} state government jobs (excluding education) jobs have been lost.")
else:
    loss_NoEd_change = round(abs(loss_NoEd_change)*100)
    print(f"That's a {loss_NoEd_change} percent gain.")
    loss_NoEd = round(abs(loss_NoEd)*1000)
    print(f"{loss_NoEd} state government jobs (excluding education) jobs have been gained.")

print('')

#calculate what percentage of state government education jobs  have been recovered
percentage_Ed_recovered = (Ed_job_may_23 / Ed_job_may_19)
loss_Ed = Ed_job_may_23 - Ed_job_may_19
loss_Ed_change = (loss_Ed / Ed_job_may_19)
print(f"Percentage of state government education jobs recovered:{percentage_Ed_recovered}%")

if loss_Ed < 0:
    loss_Ed_change = round(abs(loss_Ed_change)*100)
    print(f"That's a {loss_Ed_change} percent drop.")
    loss_Ed = round(abs(loss_Ed)*1000)
    print(f"{loss_Ed} jobs have been lost.")
else:
    loss_Ed_change = round(abs(loss_Ed_change)*100)
    print(f"That's a {loss_Ed_change} percent gain.")
    loss_Ed = round(abs(loss_Ed)*1000)
    print(f"{loss_Ed} jobs have been gained.")

print('')

#calculate what percentage of state government hospital jobs have been recovered
percentage_Hosp_recovered = (Hosp_job_may_23 / Hosp_job_may_19)
loss_Hosp = Hosp_job_may_23 - Hosp_job_may_19
loss_Hosp_change = (loss_Hosp / Hosp_job_may_19)
print(f"Percentage of state government hospital jobs recovered:{percentage_Hosp_recovered}%")

if loss_Hosp < 0:
    loss_Hosp_change = round(abs(loss_Hosp_change)*100)
    print(f"That's a {loss_Hosp_change} percent drop.")
    loss_Hosp = round(abs(loss_Hosp)*1000)
    print(f"{loss_Hosp} state government hospital jobs have been lost.")
else:
    loss_Hosp_change = round(abs(loss_Hosp_change)*100)
    print(f"That's a {loss_Hosp_change} percent gain.")
    loss_Hosp = round(abs(loss_Hosp)*1000)
    print(f"{loss_Hosp} state government hospital jobs have been gained.")

print('')

###hospitals
All_Hosp_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000006562200001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(All_Hosp_url)
data = response.json()
All_Hosp_data = data['Results']['series'][0]['data']

All_Hosp_months = []
All_Hosp_jobs = []
All_Hosp_job_may_19 = 0
All_Hosp_job_may_23 = 0

for data_point in All_Hosp_data:
    All_Hosp_year = int(data_point['year'])
    All_Hosp_period = data_point['period']
    All_Hosp_job = float(data_point['value'])
    All_Hosp_months.append(All_Hosp_year + int(All_Hosp_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    All_Hosp_jobs.append(All_Hosp_job)

    if All_Hosp_period == 'M05' and All_Hosp_year == 2019:
        All_Hosp_job_may_19 = All_Hosp_job
        print(f"Hospital Jobs in May 2019: {All_Hosp_job_may_19}")

for data_point in All_Hosp_data:
    All_Hosp_year = int(data_point['year'])
    All_Hosp_period = data_point['period']
    All_Hosp_job = float(data_point['value'])

    if All_Hosp_period == 'M05' and All_Hosp_year == 2023:
        All_Hosp_job_may_23 = All_Hosp_job
        print(f"Hospital Jobs in May 2023: {All_Hosp_job_may_23}")

plt.plot(All_Hosp_months, All_Hosp_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('Hospital Jobs in MA by Month')
plt.show()



###nursing homes
Nursing_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000006562300001?startyear=2019&endyear=2023&registrationkey={BLS_key}'
response = requests.get(Nursing_url)
data = response.json()
Nursing_data = data['Results']['series'][0]['data']

Nursing_months = []
Nursing_jobs = []
Nursing_job_may_19 = 0
Nursing_job_may_23 = 0

for data_point in Nursing_data:
    Nursing_year = int(data_point['year'])
    Nursing_period = data_point['period']
    Nursing_job = float(data_point['value'])
    Nursing_months.append(Nursing_year + int(Nursing_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    Nursing_jobs.append(Nursing_job)

    if Nursing_period == 'M05' and Nursing_year == 2019:
        Nursing_job_may_19 = Nursing_job
        print(f"Nursing Home Jobs in May 2019: {Nursing_job_may_19}")

for data_point in Nursing_data:
    Nursing_year = int(data_point['year'])
    Nursing_period = data_point['period']
    Nursing_job = float(data_point['value'])

    if Nursing_period == 'M05' and Nursing_year == 2023:
        Nursing_job_may_23 = Nursing_job
        print(f"Nursing Home Jobs in May 2023: {Nursing_job_may_23}")

plt.plot(Nursing_months, Nursing_jobs)
plt.xlabel('Year and Month')
plt.ylabel('Jobs (Thousands)')
plt.title('Nursing Home Jobs in MA by Month')
plt.show()

print('')

#calculate if hospital jobs have recovered
if All_Hosp_job_may_23 >= All_Hosp_job_may_19:
    print("Hospital jobs in MA have recovered since the pandemic")
else:
    print("Hospital jobs in MA have not recovered since the pandemic")

print('')

#calculate if nursing home jobs have recovered
if Nursing_job_may_23 >= Nursing_job_may_19:
    print("Nursing home jobs in MA have recovered since the pandemic")
else:
    print("Nursing home jobs in MA have not recovered since the pandemic")

print('')

#All_Hosp_job_may_19 = 0
#All_Hosp_job_may_23 = 0
#Nursing_job_may_19 = 0
#Nursing_job_may_23 = 0

#calculate what percentage of hospital have been recovered
percentage_All_Hosp_recovered = (All_Hosp_job_may_23 / All_Hosp_job_may_19)
loss_All_Hosp = All_Hosp_job_may_23 - All_Hosp_job_may_19
loss_All_Hosp_change = (loss_All_Hosp / All_Hosp_job_may_19)
print(f"Percentage of hospital jobs recovered:{percentage_All_Hosp_recovered}%")

if loss_All_Hosp < 0:
    loss_All_Hosp_change = round(abs(loss_All_Hosp_change)*100)
    print(f"That's a {loss_All_Hosp_change} percent drop.")
    loss_All_Hosp = round(abs(loss_All_Hosp)*1000)
    print(f"{loss_All_Hosp} hospital jobs have been lost.")
else:
    loss_All_Hosp_change = round(abs(loss_All_Hosp_change)*100)
    print(f"That's a {loss_All_Hosp_change} percent gain.")
    loss_All_Hosp = round(abs(loss_All_Hosp)*1000)
    print(f"{loss_All_Hosp} hospital jobs have been gained.")

print('')

#calculate what percentage of nursing home jobs have been recovered
percentage_Nursing_recovered = (Nursing_job_may_23 / Nursing_job_may_19)
loss_Nursing = Nursing_job_may_23 - Nursing_job_may_19
loss_Nursing_change = (loss_Nursing / Nursing_job_may_19)

print(f"Percentage of nursing home jobs recovered:{percentage_Nursing_recovered}%")

if loss_Nursing < 0:
    loss_Nursing_change = round(abs(loss_Nursing_change)*100)
    print(f"That's a {loss_Nursing_change} percent drop.")
    loss_Nursing = round(abs(loss_Nursing)*1000)
    print(f"{loss_Nursing} nursing home jobs have been lost.")
else:
    loss_Nursing_change = round(abs(loss_Nursing_change)*100)
    print(f"That's a {loss_Nursing_change} percent gain.")
    loss_Nursing = round(abs(loss_All_Hosp)*1000)
    print(f"{loss_Nursing} nursing home jobs have been gained.")
    