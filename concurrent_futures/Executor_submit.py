from concurrent import futures
#           Executor.submit(fn, *args, **kwargs)
#           fn：需要异步执行的函数
#           *args, **kwargs：fn参数
#

def test(num):
    import time
    return time.ctime(), num

with futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(test, 1)
    print(future.result())