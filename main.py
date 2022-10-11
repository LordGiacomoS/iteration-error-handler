import json
from pathlib import Path

prog_file = 'progress.json'

class Progress:
    def __init__(self, prog_file='progress.json', inp_list=None):
        self.prog_file = prog_file

        if inp_list == None:
            self.load_progress()
        elif Path(self.prog_file).exists():
            self.load_progress()
        else:
            self.completed_items = []
            self.all_items = inp_list
            self.to_do = [item for item in self.all_items if item not in self.completed_items]

    def __repr__(self):
        return json.dumps(self.progress_dct(), indent=2)

    def progress_dct(self):
        dct = {
            'completed': self.completed_items,
            'to_do': self.to_do,
            'all': self.all_items
        }
        return dct

    def save_progress(self, updated):
        with open(self.prog_file, 'w') as f:
            json.dump(updated, f, indent=2)

    def load_progress(self):
        if Path(self.prog_file).exists():
            with open(self.prog_file) as f:
                dct = json.load(f)
                self.completed_items = dct['completed']
                self.all_items = dct['all']
                self.to_do = dct['to_do']
        else:
            dct = self.progress_dct()
        return dct

    def reset(self):
        new_progress = {
            'completed': [],
            'to_do': self.all_items,
            'all': self.all_items
        }
        self.completed_items = []
        self.to_do = self.all_items

        self.save_progress(new_progress)

    def work(self, interrupt=None):
        if Path(prog_file).exists() == False:
            self.completed_items = []
            progress = {
                'completed': [],
                'to_do': self.all_items,
                'all': self.all_items
            }
            self.save_progress(progress)
        
        num = 0
        print(self.to_do)
        for item in self.to_do:
            if type(interrupt) == int and interrupt == num:
                raise Exception('Interruption time')

            print(item)
            self.completed_items.append(item)
            self.to_do = [item for item in self.all_items if item not in self.completed_items]
            
            new_prog = {
                'completed': self.completed_items,
                'to_do': self.to_do,
                'all': self.all_items
            }

            self.save_progress(new_prog)
            num += 1

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
prog = Progress(prog_file, items)
prog.reset()
prog.work(6)

"""
def work(list, prog_file, interrupt=None):
    if Path(prog_file).exists() == False:

        completed_items = []
        progress = {'completed': [], 'to_do': list, 'all': list}

        save_progress(prog_file, progress)

    else:
        progress = load_progress(prog_file)
        completed_items = progress['completed']
        list = progress['all']

    num = 0
    for item in list:
        if type(interrupt) == int and interrupt == num:
            raise Exception('Interruption time')

        print(item)
        completed_items.append(item)
        undone = [item for item in item if item not in completed_items]
        new_prog = {
            'completed': completed_items,
            'to_do': undone,
            'all': items
        }

        save_progress(prog_file, new_prog)
        num += 1

def save_progress(prog_file, updated):
    with open(prog_file, 'w') as f:
        json.dump(updated, f, indent=2)

def load_progress(prog_file):
    if Path(prog_file).exists():
        with open(prog_file) as f:
            return json.load(f)
    else:
        return []

def save_txt(new_lines, file):
    if Path(file).exists():
        with open(file) as f:
            old_lines = f.readlines()
        all_lines = old_lines + new_lines
    else:
        all_lines = new_lines

    with open(file, 'w') as f:
        f.writelines(all_lines)

def reset(prog_file):
    progress = load_progress(prog_file)
    new_progress = {
        'completed': [],
        'to_do': progress['all'],
        'all': progress['all']
    }
    save_progress(prog_file, new_progress)
"""



#reset(prog_file)
#work(items, prog_file, interrupt=4)
