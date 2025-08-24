import re 

with open("ssh_error.log") as file:
    for line in file:
      if "Failed password" in line:
        ip = re.search(r'[0-9]+(?:\.[0-9]+){3}', line)
        if ip:
          print(ip.group())
