import time
import json
import sys

import os

from minio import Minio
from PIL import Image


bucket_name = "serverlessbench"

MAX_WIDTH = 250.0
MAX_HEIGHT= 250.0

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    LAUNCH_TIME = time.time_ns()
    currentTime = GetTime()
    event = json.loads(req)

    startTimes = event["startTimes"]
    startTimes.append(currentTime)

    response = event.copy()

    minio_url = event["minio_url"]
    access_key = event["access_key"]
    secret_key = event["secret_key"]
    bucket_name = event["bucket_name"]
    img_name = event["img_name"]

    response["startTimes"] = startTimes

    logid = event["log"]

    db_begin = GetTime()
    minioClient=Minio(minio_url,access_key=access_key,secret_key=secret_key,secure=False)
    filepath = '/tmp/{}-{}'.format(logid, img_name)
    minioClient.fget_object(bucket_name, object_name=img_name, file_path=filepath)
    db_finish = GetTime()
    db_elapse_ms = db_finish - db_begin

    commTimes = event["commTimes"]
    commTimes.append(db_elapse_ms)
    response["commTimes"] = commTimes

    size = event["extracted-metadata"]["dimensions"]
    width = size["width"]
    height = size["height"]

    scalingFactor = min(MAX_HEIGHT/ height, MAX_WIDTH / width)
    width = int(width * scalingFactor)
    height = int(height * scalingFactor)
   
    logid = event["log"]
    thumbnailName = "thumbnail-" + logid + "-" + img_name
    filepath2 = '/tmp/thumbnail-{}-{}'.format(logid, img_name)
    ResizeImage(filepath, filepath2, width, height)
    minioClient.fput_object(bucket_name, object_name=thumbnailName, file_path=filepath2)

    response["thumbnail"] = thumbnailName

    minioClient.remove_object(bucket_name, logid)
    minioClient.remove_object(bucket_name, thumbnailName)
    os.remove(filepath)
    os.remove(filepath2)

    endTime = time.time_ns()
    executionTime = endTime - LAUNCH_TIME
    response["execution-time"] = executionTime

    return json.dumps(response)


def execute(img_name):
    """handle a request to the function
    Args:
        req (str): request body
    """
    currentTime = GetTime()



    logid = []

    db_begin = GetTime()
    minioClient = Minio('192.168.1.109:31786', access_key='admin123', secret_key='admin123', secure=False)
    filepath = '/tmp/{}-{}'.format(logid, img_name)
    minioClient.fget_object(bucket_name, object_name=img_name, file_path=filepath)
    db_finish = GetTime()
    db_elapse_ms = db_finish - db_begin


    width = 50
    height = 50

    scalingFactor = min(MAX_HEIGHT / height, MAX_WIDTH / width)
    width = int(width * scalingFactor)
    height = int(height * scalingFactor)

    logid = "output.jpg"
    thumbnailName = "thumbnail-" + logid + "-" + img_name
    filepath2 = '/tmp/thumbnail-{}-{}'.format(logid, img_name)
    ResizeImage(filepath, filepath2, width, height)
    minioClient.fput_object(bucket_name, object_name=thumbnailName, file_path=filepath2)


    #minioClient.remove_object(bucket_name, logid)
    #minioClient.remove_object(bucket_name, thumbnailName)
    os.remove(filepath)
    os.remove(filepath2)


    print(GetTime()-currentTime)
    return json.dumps([])

def ResizeImage(filein, fileout, width, height):
    img = Image.open(filein)
    out = img.resize((width, height),Image.Resampling.LANCZOS)
    out.save(fileout, "JPEG")

def GetTime():
    return int(round(time.time() * 1000))

if __name__ == '__main__':
    #execute("001.jpg")
    execute(sys.argv[1])
