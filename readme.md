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