from celery import Celery
import os
import sys
import shlex
import subprocess
import pymongo
import datetime

client = pymongo.MongoClient().LQDESKTOP_JOB.JOB_LOG

client.create_index('filename')
app = Celery('tasks', backend='rpc://', broker='pyamqp://')



@app.task
def quantaxis_run(shell_cmd):

    filename = shell_cmd
    shell_cmd = 'python "{}"'.format(shell_cmd)

    client.insert({
        'source': 'quantaxis',
        'filename': filename,
        'time': str(datetime.datetime.now()),
        'message': 'start',
        'status': 'start'})
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            client.insert({
                'filename': filename,
                'time': str(datetime.datetime.now()),
                'message': str(line),
                'status': 'running'})
    if p.returncode == 0:
        client.insert({
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': 'backtest run  success',
            'status': 'success'})
    else:
        client.insert({
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': str(p.returncode),
            'status': 'failed'})


@app.task
def lq_run(shell_cmd):

    filename = shell_cmd
    shell_cmd = 'autogen "{}"'.format(shell_cmd)

    client.insert({
        'source': 'LQ_AutoGEN',
        'filename': filename,
        'time': str(datetime.datetime.now()),
        'message': 'start',
        'status': 'start'})
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            client.insert({
                'filename': filename,
                'time': str(datetime.datetime.now()),
                'message': str(line),
                'status': 'running'})
            #print('QUANTAXIS: [{}]'.format(line))
    if p.returncode == 0:
        #self.write_message('backtest run  success')
        client.insert({
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': 'backtest run  success',
            'status': 'success'})
    else:
        client.insert({
            'filename': filename,
            'time': str(datetime.datetime.now()),
            'message': str(p.returncode),
            'status': 'failed'})
