# quantaxis_run

quantaxis_run 是基于celery的分布式回测运行代码

1. 配置好celery以及rabbitmq(需要安装erlang)
2. 创建一个文件:

```python

from quantaxis_run import quantaxis_run
filelist = [
            'E:\\quantaxis\\EXAMPLE\\test_backtest\\example\\simple_backtest_day.py']
res = [quantaxis_run.delay(item) for item in filelist]

```


3. 启动任务后台

```
celery -A quantaxis_run worker --loglevel=info
```

4. 查看任务

```python
from quantaxis_run.query import query_result

print(query_result())

```
5. 查看单个任务
```python
from quantaxis_run.query import query_onejob
query_onejob('08e384e5-302d-4d28-9a5d-7a53cf4cae42') #这里是运行时返回的
```


## 示例:
```python
from quantaxis_run import quantaxis_run

quantaxis_run.delay('E:\\AGModel\\temp_teststrategy.py')
<AsyncResult: bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc>

from quantaxis_run.query import query_result,query_onejob


query_onejob('bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc')
[{'_id': ObjectId('5c3f0ea2671bd962a4fdc213'),
  'job_id': 'bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc',
  'source': 'python',
  'filename': 'E:\\AGModel\\temp_teststrategy.py',
  'time': '2019-01-16 18:59:46.475493',
  'message': 'start',
  'status': 'start'},
 {'_id': ObjectId('5c3f0eb6671bd962a4fdc215'),
  'job_id': 'bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc',
  'filename': 'E:\\AGModel\\temp_teststrategy.py',
  'time': '2019-01-16 19:00:06.571495',
  'message': "b'common:         C:\\\\Users\\\\yutia\\\\Documents\\\\Tencent Files\\\\279336410\\\\FileRecv'",
  'status': 'running'},
 {'_id': ObjectId('5c3f0eb7671bd962a4fdc216'),
  'job_id': 'bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc',
  'filename': 'E:\\AGModel\\temp_teststrategy.py',
  'time': '2019-01-16 19:00:07.631495',
  'message': 'backtest run  success',
  'status': 'success'}]

query_result()
[{'_id': ObjectId('5c3f0eb7671bd962a4fdc216'),
  'job_id': 'bc6d07fd-1a70-4dfc-bcd7-ce7274f4c6cc',
  'filename': 'E:\\AGModel\\temp_teststrategy.py',
  'time': '2019-01-16 19:00:07.631495',
  'message': 'backtest run  success',
  'status': 'success'}]

```


## 版本记录:

- 1.0 基础的分布式任务
- 1.1 基于job_id的任务部署/查询
