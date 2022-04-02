import json
from pathlib import Path

jobs_data = Path('jobs.txt')

output_data = Path('docs/jobs/index.md')

data = json.loads(jobs_data.read_text())


document = """# Jobs

These are jobs we've seen around that are friendly towards EMEA time zones. Most of them are remote. Some of them have location requirements within EMEA (in which case we list this in the title). Most of them should have transparent salary ranges. We have no direct affiliation with these companies.

"""

for job in data['records']:
    if job['fields']:
        fields = job['fields']
        document += f"* **{fields['Company']} | {fields['Position']} | {fields['Salary']}.** {fields['Description']} [Link]({fields['URL']}). Posted on {fields['Created']}\n"
    document += "\n"

with output_data.open('w') as f:
    f.write(document)

