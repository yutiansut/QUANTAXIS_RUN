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


## 版本记录:

- 1.0 基础的分布式任务
- 1.1 基于job_id的任务部署/查询
