from celery import Celery
import os
import sys
import shlex
import subprocess
import pymongo
import datetime

client_qa = pymongo.MongoClient().quantaxis.joblog
client_joblist = pymongo.MongoClient().quantaxis.joblist
client_qa.create_index('filename')
app = Celery('tasks', backend='rpc://', broker='pyamqp://')


@app.task(bind=True)
def quantaxis_run(self, shell_cmd, program='python'):

    filename = shell_cmd
    shell_cmd = '{} "{}"'.format(program, shell_cmd)

    client_qa.insert({
        'job_id': str(self.request.id),
        'source': program,
        'filename': filename,
        'time': str(datetime.datetime.now()),
        'message': 'start',
        'status': 'start'})
    client_joblist.insert(
        {'program': program, 'files': filename, 'status': 'running', 'job_id': str(self.request.id)})
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            client_qa.insert({
                'job_id': str(self.request.id),
                'filename': filename,
                'time': str(datetime.datetime.now()),
                'message': str(line),
                'status': 'running'})
    if p.returncode == 0:
        client_qa.insert({
            'job_id': str(self.request.id),
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': 'backtest run  success',
            'status': 'success'})
        client_joblist.find_and_modify({'job_id': str(self.request.id)}, {'$set': {'status': 'success'}})
    else:
        client_qa.insert({
            'job_id': str(self.request.id),
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': str(p.returncode),
            'status': 'failed'})
