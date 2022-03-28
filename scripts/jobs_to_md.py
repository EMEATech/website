import json
from pathlib import Path

jobs_data = Path('jobs.txt')

output_data = Path('docs/jobs.md')

data = json.loads(jobs_data.read_text())

document = ""
for job in data['records']:
    if job['fields']:
        fields = job['fields']
        document += f"* **{fields['Company']} | {fields['Position']} | {fields['Salary']}.** {fields['Description']} {fields['URL']}\n"
    document += "\n"

with output_data.open('a') as f:
    f.write(document)

