api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

r = requests.get(api_url)

if not r.ok:
    print("Failed to fetch data")
    data = []

else:    
    data = r.json()

def get_number_of_jobs_T(technology):
    count = 0
    for jobs in data:
        if isinstance(jobs, dict):
            if technology.lower() in jobs.get("Key Skills","").lower():
                count += 1
    
    return technology, count

get_number_of_jobs_T("Python")
