from operator import itemgetter
import difflib
import json


class Note:
    def __init__(self, note: str):
        self.note = note

    def show_note(self):
        pass

    def edit_note(self, note, new_note):
        if note in self.note:
            self.note += new_note

    def delete_note(self, note):
        if note in self.note:
            self.note.replace(self.note, '')

    def __repr__(self):
        return f'{self.note}'


class NoteRecord:
    def __init__(self, note='', tag=None):
        self.note = Note(note)
        self.tag = tag
        self.filename = 'data.json'
        self.record = {'note': str(self.note), 'tag': self.tag}

    def tag_note_search(self, tag):
        tag_list = []
        for i in map(lambda x: x['tag'], self.record):
            tag_list.extend(i)
        tag_list = set(tag_list)
        tag_list_of_dict = []
        for item in tag_list:
            ratio = int(difflib.SequenceMatcher(None, str(tag), str(item)).ratio() * 100)
            if ratio > 50:
                user_tag = item
                for i in self.record:
                    if user_tag in i['tag']:
                        tag_list_of_dict.append({ratio: i['note']})
        sort_list = []
        for tag in tag_list_of_dict:
            for key, value in tag.items():
                sort_list.append({"ratio": key, "tag": value})
        new_list = sorted(sort_list, key=itemgetter('ratio'), reverse=True)
        return ([d["tag"] for d in new_list]) if len(new_list) > 0 else f"No such tags in notes"

    def note_serialize(self, list_of_notes=None):
        if list_of_notes is None:
            list_of_notes = []
        if list_of_notes:
            with open(self.filename, 'w') as file:
                json.dump(list_of_notes + [self.record], file, sort_keys=True, indent=4)
        else:
            with open(self.filename, 'w') as file:
                json.dump([self.record], file, sort_keys=True, indent=4)

    def note_deserialize(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

#
# while True:
#     command = input(': ')
#     sep_val = command.split(' ')
#     if sep_val[0] == 'note' and sep_val[1] != 'change':
#         tag_index = sep_val.index('-tag') if '-tag' in sep_val else len(sep_val)
#         main_note = NoteRecord(
#             ' '.join(sep_val[1:tag_index]),
#             sep_val[tag_index + 1:] if tag_index != len(sep_val) else None
#         )
#         try:
#             note_list = main_note.note_deserialize()
#             main_note.note_serialize(note_list)
#         except FileNotFoundError:
#             main_note.note_serialize()
#     elif sep_val[0] == '.':
#         break
#     else:
#         print('Try again!')
