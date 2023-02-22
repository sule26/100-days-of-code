with open("Day 024/Input/Names/invited_names.txt", encoding='utf-8') as names:
    all_names = names.read()
    person_list = all_names.strip(' ').split()

with open("Day 024/Input/Letters/starting_letter.docx") as letter:
    starting_list = letter.read()

for person in person_list:
    with open(f'Day 024/Output/ReadyToSend/letter_for_{person}.docx', 'w', encoding='utf-8') as new_letter:
        finished_letter = starting_list.replace('[name]', f'{person}', 1)
        new_letter.write(finished_letter)
