import sys
import yaml #type[ignore]
import subprocess

# Load labels from GitHub Action input
labels = sys.argv[2].split(',')
number = int(sys.argv[1])

# Load the label-user mapping from the YAML file
with open('.github/label_to_devs.yml', 'r') as file:
    label_user_mapping = yaml.safe_load(file)

# Find reviewers based on labels
for label in labels:
    reviewers = set()
    label = label.strip()
    if label in label_user_mapping:
        reviewers.update(label_user_mapping[label])
        print(reviewers)
    if reviewers:
        prefix_arg = f"gh pr edit {number} --add-assignee "
        reviewers_arg = "".join(f"{reviewer} " for reviewer in reviewers)
        arg = prefix_arg + reviewers_arg
        print(arg)
        subprocess.run(arg, shell=True)
