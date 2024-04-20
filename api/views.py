from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import pandas as pd
import os
from django.conf import settings
import subprocess
import os
import shutil
from .utils import GetCSV



class FileAPIView(APIView):
    def get(self,request):
        GetCSV()
        try:
            os.remove(os.path.join(settings.BASE_DIR, 'data.csv'))
        except:
            pass  
        substring = "CF-AN"
        
        # download_dir = r"C:\Users\dell\Downloads\\"
        download_dir = '/Users/kira/Downloads/'
        files = os.listdir(download_dir)

        latest_file = max([file for file in files if file.startswith('CF-AN-equities')], key=lambda f: os.path.getmtime(os.path.join(download_dir, f)))
        new_file_name = 'data.csv'  # Provide the new file name here
        os.rename(os.path.join(download_dir, latest_file), os.path.join(download_dir, new_file_name))

        print("Renamed file:", new_file_name)

        destination_file = './'

        shutil.move(download_dir + new_file_name,destination_file)
        
        return Response({'msg':'File Copied Sucessfully'})

class GetSubjectAPIView(APIView):
    def get(self,request):
        file_ = open(os.path.join(settings.BASE_DIR, 'data.csv'))
        
        df = pd.read_csv(file_)
        subjects = df["SUBJECT"].unique().tolist()
        # print(subjects)
        data_with_id = [{'id': i, 'name': item} for i, item in enumerate(subjects)]
        return Response(data_with_id)
    
class GetContentAPIView(APIView):
    def get(self,request):
        file_ = open(os.path.join(settings.BASE_DIR, 'data.csv'))
        subject = request.query_params.get('subject')
        df = pd.read_csv(file_)
        subjects = df["SUBJECT"].unique().tolist()
        newdf = df[df["SUBJECT"]==str(subject)]
        grouped = newdf.groupby("SUBJECT")

        result = []
        count = 0
        # Iterate over each group
        for name, group in grouped:
            while True:
                try:
                    result.append(group.to_dict(orient='records')[count])
                    count += 1
                except:
                    break
        return Response(result)