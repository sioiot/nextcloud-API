import sys
import os
import re
import json
import argparse
from os.path import join
from os.path import dirname


sys.path.insert(0, join(dirname(__file__), 'src'))

from nextcloud import NextCloud

class upload_file(object):
    
    NEXTCLOUD_URL = ""
    NEXTCLOUD_USERNAME = ""
    NEXTCLOUD_PASSWORD = ""
    NEXTCLOUD_LOCAL_FILEPATH =""
    NEXTCLOUD_UPLOAD_FILEPATH=""

    def __init__(self,NEXTCLOUD_URL,NEXTCLOUD_USERNAME,NEXTCLOUD_PASSWORD,NEXTCLOUD_LOCAL_FILEPATH,NEXTCLOUD_UPLOAD_FILEPATH):
        self.NEXTCLOUD_URL=NEXTCLOUD_URL
        self.NEXTCLOUD_USERNAME=NEXTCLOUD_USERNAME
        self.NEXTCLOUD_PASSWORD=NEXTCLOUD_PASSWORD
        self.NEXTCLOUD_LOCAL_FILEPATH=NEXTCLOUD_LOCAL_FILEPATH
        self.NEXTCLOUD_UPLOAD_FILEPATH=NEXTCLOUD_UPLOAD_FILEPATH

    def exec(self):
        try:
            nextcloud_client = NextCloud(endpoint=self.NEXTCLOUD_URL, user=self.NEXTCLOUD_USERNAME, password=self.NEXTCLOUD_PASSWORD, json_output=True)
            ret = nextcloud_client.upload_file(self.NEXTCLOUD_USERNAME, self.NEXTCLOUD_LOCAL_FILEPATH, self.NEXTCLOUD_UPLOAD_FILEPATH)
            if re.search('Status: Failed', str(ret)):
                raise SystemExit(1)

        except IOError as e:
            print(e)
            raise SystemExit(2)
    
    def  run(self):
        self.exec()

if __name__ == "__main__":
    init_parser = argparse.ArgumentParser(description='upload_file.py', add_help=False)
    init_parser.add_argument('--url', '-u',
                             help='nextclod url')
    init_parser.add_argument('--username', '-n',
                             help='nextclod username')
    init_parser.add_argument('--password', '-p',
                             help='nextclod password')
    init_parser.add_argument('--localfile', '-lf',
                             help='nextclod local filepath')
    init_parser.add_argument('--uploadfile', '-uf',
                             help='nextclod upload filepath')
    args = init_parser.parse_args()
    
    upload_file(args.url, args.username, args.password, args.localfile, args.uploadfile).run()
