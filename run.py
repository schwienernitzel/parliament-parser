from datetime import datetime
import os
import re
import subprocess

datetime = datetime.now().strftime('%d%m%y')
dataset = f'../dataset-{datetime}.csv'

curdir = os.getcwd()
protocols = os.path.join(curdir, 'lp21/protocols')
os.chdir(protocols)

files = []

for file in os.listdir(protocols):
    if file.endswith('.xml'):
        number = int(file[:-4])
        files.append((number, file))

files.sort()
total = len(files)

for number, file in files:
    num = file[2:-4]
    try:
        result = subprocess.run(['python3', '../../process.py', file], check=True, capture_output=True, text=True)
        with open(dataset, 'a') as writefile:
            writefile.write(result.stdout)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Unable to process {file}: {e.stderr}")

with open(dataset, 'r') as file:
    lines = file.readlines()

with open(dataset, 'w') as file:
    for line in lines:
        if re.search(r'<redner id="[^:]*:', line):
            continue
        line = line.replace('#', '')
        line = re.sub(r'[0-9]+Anlage.*', '', line)
        file.write(line)