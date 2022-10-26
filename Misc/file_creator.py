import shutil
import ftplib
import re
import os

def create_directory(link2LearningID):
    directory = link2LearningID
    parent_dir = "C:/Users/vj_ku/OneDrive/_Docs/Work/Wellnet/siemens_resources/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

def get_data_from_ftp():
    ftp = ftplib.FTP("ftp.cloud.scorm.com")
    ftp.login("<Username>", "<Password>")
    ftp.cwd('/LinkeLearningRealm/TYFLI9WJR3/courses/' + link2LearningID + '/2/story_content/WebObjects')
    data = []
    ftp.dir(data.append)
    ftp.quit()
    return data

def create_files(data):
    for line in data:
        filename = re.findall('22:25\s.*(?:\.pdf|\.xls)', line)
        if len(filename) > 0:
            filename = ''.join(filename)
            filename = filename[6:]
            print(filename)
            original = r'C:\Users\vj_ku\OneDrive\_Docs\Work\Wellnet\siemens_resources\Siemens_-_generic_resource_substitution.pdf'
            target = rf'C:\Users\vj_ku\OneDrive\_Docs\Work\Wellnet\siemens_resources\{link2LearningID}\\' + filename
            shutil.copyfile(original, target)
        else:
            print("Error. Check the content of the data variable")

link2LearningID = 'Link2eLearning3284'
create_directory(link2LearningID)
data = get_data_from_ftp()
create_files(data)
