def fib(n: int):
    """
    求第n个斐波那契数列
    思路：不要用递归，容易想到的方案是设
    a=1,  b=1, 那么循环 3-n，依次用a=b， b=b+a。把两个变量想象成两个指针，依次移动两个指针的位置
    :param n:
    :return:
    """
    a = 1
    b = 1
    if n <= 2:
        return 1
    for i in range(3, n + 1):
        t = b  # 暂存b
        b = a + b
        a = t
    return b
