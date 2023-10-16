"""Take in file and pulls necessary date's and assignments"""

def create_file(file_name, file_content):
    """Creates File for reading and finding dates"""
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)

def read_file(file_name):
    """Read and finds dates and assignment for calendar"""
    with open(f'{file_name}.txt', encoding='utf-8') as f:
        return f.read()
