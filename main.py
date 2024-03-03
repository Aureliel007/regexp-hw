import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print(contacts_list)
pattern = r"(\+7|8)?[\s\(\-]*(\d{3})[\)\s\-]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s?\(?(доб\.)?\s?(\d+)?\)?"
substitution = r"+7(\2)\3-\4-\5 \6\7"

data = {}

for contact in contacts_list[1:]:
    name = ' '.join(contact[:3])
    phone = contact[5]
    phone_correct = re.sub(pattern, substitution, phone)
    contact[5] = phone_correct.strip()
    full_name = name.split()
    if len(full_name) < 3:
        record = name.split() + contact[2:]
    else:
        record = (name.split() + contact[3:])
    key = ' '.join(record[:2])
    person = data.get(key)
    if not person:
        data.setdefault(key, record[2:])
    else:
        data[key] = [y if not x else x for x, y in zip(person, record[2:])]

result = [contacts_list[0]]
for name, info in data.items():
    person = name.split()
    person.extend(info)
    result.append(person)

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result)
