import os
import subprocess
import uuid
from django.core.files.base import ContentFile


class Document(object):

    def __init__(self, file_name, file_content):
        self.file_name = self.__get_file_name(file_name)
        self.file_content = file_content
        self.pwd = self.__pwd()
        self.file_path = self.__get_file_path()

    def __get_file_name(self, file_name):
        return file_name.replace('/', '-').replace(' ', '-')

    def __pwd(self):
        pwd = ''
        try:
            subprocess_pwd = subprocess.check_output('pwd')
            pwd = subprocess_pwd.split('\n')[0] + '/statements/v1/services'
        except Exception as e:
            pass
        return pwd

    def __get_file_path(self):

        file_name = '{pwd}/{uuid}_{file_name}'.format(
            pwd=self.pwd, file_name=self.file_name, uuid=uuid.uuid4().hex)
        fout = open(file_name, 'wb+')
        file_content = ContentFile(self.file_content.read())
        try:
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()
            return file_name
        except:
            return None
