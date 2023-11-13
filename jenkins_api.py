import csv

def list_job(jenkins_url,jenkins_user,jenkins_pass):

    import jenkins

    server = jenkins.Jenkins(jenkins_url,jenkins_user,jenkins_pass)
    user = server.get_whoami()
    jobs = server.get_jobs()

    job_summary = []

    for i in jobs:
        job_name=i['name']
        job_url=i['url']
        job_status=i['color']
        job_summary.append([job_name,job_url,job_status])
    
    return job_summary

with open("example.txt" , 'a') as f :
    content = "adding data into file\n"
    f.write(content)

with open("example.txt", "r") as file:
    cont = file.read()
    print(cont)

data=list_job('http://45.33.11.12:8080', 'utrains', 'devops')
with open("jenkins_object.csv", "w") as j:
    write_row = csv.writer(j)
    write_row.writerow(['job_name', 'job_url','job_status'])
    for item in data:
        write_row.writerow(item)