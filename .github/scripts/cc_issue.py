import sys
import yaml # type: ignore
import subprocess

# Load labels from GitHub Action input
number = sys.argv[1]
label = sys.argv[2]
body = sys.argv[3]

# Load the label-user mapping from the YAML file
with open('.github/label_to_devs.yml', 'r') as file:
    label_user_mapping = yaml.safe_load(file)


if (related_users := label_user_mapping.get(label)):
    related_users = set(related_users)
    lines = body.split("\n")
    
    last_line = lines[-1]
    # check if the issue already has a CC
    if last_line[:4] == "CC: ":
        lines.pop()
        users = last_line[4:].split(", ") # find all users in the CC
        users = [user[1:]  for user in users] # remove the @
        all_users = set(users) | related_users # combine the old and new users
    else:
        # add three lines for formatting
        lines.append("")
        lines.append("")
        lines.append("")
        all_users = related_users
    all_users.discard("") # remove empty strings
    new_line = "CC: " + "".join(f"@{user}, " for user in all_users)[:-2]
    lines[-1] = new_line
    new_body = "".join(f"{line}\n" for line in lines)[: -1]
    command = f"gh issue edit {number} --body '{new_body}'"
    subprocess.run(command, shell=True)
