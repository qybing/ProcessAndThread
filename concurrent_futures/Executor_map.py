from concurrent import futures
#
# 相当于map(func, *iterables)，但是func是异步执行。timeout的值可以是int或float，如果操作超时，会返回raisesTimeoutError；如果不指定timeout参数，则不设置超时间。
#
# func：需要异步执行的函数
#
# *iterables：可迭代对象，如列表等。每一次func执行，都会从iterables中取参数。
#
# timeout：设置每次异步操作的超时时间
def test(num):
    import time
    return time.ctime(), num


data = [1, 2, 3]
with futures.ThreadPoolExecutor(max_workers=1) as executor:
    for future in executor.map(test, data):
        print(future)

