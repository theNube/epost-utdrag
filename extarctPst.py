import tkinter.messagebox
from tkinter import filedialog
import pypff
import os
import  shutil


def open_Pst_File():
    int_folder = 'C:\\Users\\AlexThiery\\DevOp\\input\\'
    pst_file = filedialog.askopenfilename(initialdir=int_folder)
    pst = pypff.file()
    pst_file = pst_file.replace('/', '\\')
    pst.open(pst_file)
    root = pst.get_root_folder()
    return root


def get_Init(root):

    messages = []
    for folder in root.sub_folders:
        folder_name = folder.name

        for sub_folder in folder.sub_folders:
            sub_folder_name = sub_folder.name

            for message in sub_folder.sub_messages:
                subject = message.subject
                sender = message.sender_name
                date = message.client_submit_time
                if message.plain_text_body is not None:
                    body = message.plain_text_body.decode()
                else:
                    print('finns inget innehåll i e-posten')
                    body = ''
                messages.append((folder_name, sub_folder_name, subject, sender, date, body))
    return messages


class readFile:
    def __init__(self, message):
        self.pst_folder = message[0]
        self.pst_subfolder = message[1]
        self.pst_subject = message[2]
        self.pst_sender = message[3]
        self.pst_date = message[4]
        self.pst_body = message[5]
        self.content_messages = str('')

    def content_inmasseges(self):
        self.content_messages = (f'{self.pst_subject}\n'
                                 f'{self.pst_sender}\n'
                                 f'{self.pst_date}\n'
                                 f'{self.pst_body}\n')
        return self.content_messages

    def write(self):
        self.content_inmasseges()
        clean_data = self.content_messages

        with open('slask.txt', 'a', encoding='utf-8') as d:
            d.write(clean_data)

        try:
            with open('slask.txt', 'r', encoding='utf-8') as d:
                lines = [line for line in d.readlines() if line.strip() != '']
        except UnicodeDecodeError as e:
            print(f'Error decoding file: {str(e)}')
            lines = []

        with open('slask.txt', 'w', encoding='utf-8') as d:
            for line in lines:
                try:
                    clean_line = line.encode('utf-8', 'ignore').decode('utf-8')
                    d.write(f'{clean_line.strip()}\n')
                except UnicodeEncodeError as e:
                    print(f'Error encoding line: {str(e)}')

class MakeFile:
    def Txtfile(self):
        source_file='slask.txt'
        dest_file=input('Namege filen: ')
        destination_file=dest_file+ '.txt'
        os.system(f'copy {source_file} {destination_file}')
        os.remove(source_file)

    def Txtfile_tkinter(Self):
       copy_file='slask.txt'
       destination=filedialog.askdirectory()+'.txt'
       shutil.copy(copy_file, destination)
       tkinter.messagebox.showinfo('Filen sparad')


if __name__ == '__main__':
    root = open_Pst_File()
    messages = get_Init(root)
    for message in messages:
        reader = readFile(message)
        reader.write()
    file=MakeFile()
    file.Txtfile_tkinter()