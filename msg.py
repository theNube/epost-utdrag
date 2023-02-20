import extract_msg
from tkinter import filedialog
import pypff


def open_Pst_File():
    int_folder='C:\\Users\\AlexThiery\\DevOp\\input'
    filedialog.askopenfilename(initialdir=int_folder)
    pst_file=pypff.file()
    return pst_file

class pst_File_Extract:
    def test(self, pst_file):
        root_inf=pst_file.get_root_folder()
        for folder in root_inf.sub_folders:
            print('Folder:', folder.name)
    pst_file.close()




def open_file():
    int_folder='C:\\Users\\AlexThiery\\DevOp\\input'
    file = filedialog.askopenfilename(initialdir=int_folder)
    file = extract_msg.Message(file)
    return file


class Readfile:
    def __init__(self, file):
        self.content = str('')
        self.msg_sender = file.sender
        self.msg_reciver = file.recipients
        self.msg_subj = file.subject
        self.msg_date = file.date
        self.msg_message = file.body

    def output(self):
        self.content = (f'{self.msg_sender}\n'
                        f'{self.msg_reciver}\n'
                        f'{self.msg_subj}\n'
                        f'{self.msg_date}\n'
                        f'{self.msg_message}')
        return self.content

    def clean(self):
        clean_data = self.content
        with open('slask.txt', 'w', encoding='utf-8') as d:
            d.write(clean_data)
            d.close()
        with open('slask.txt', 'r') as d:
            lines = [line for line in d.readlines() if line.strip() != '']

        with open('slask.txt', 'w', encoding='utf-8'):
            pass
        for line in lines:
            with open('slask.txt', 'a') as d:
                d.write(f'{line.strip()}\n')


if __name__=='__main__':
    pst_file = open_Pst_File()
    read_file = pst_File_Extract
    # read_file.output()
    # read_file.clean()



