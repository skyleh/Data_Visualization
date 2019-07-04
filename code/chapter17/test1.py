def hanoi(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        # 将前n-1个盘子从a移动到b上
        hanoi(n-1,a,c,b)
        # 将最底下的最后一个盘子从a移动到c上
        hanoi(1,a,b,c)
        # 将b上的n-1个盘子移动到c上
        hanoi(n-1,b,a,c)
n=int(input('请输入汉诺塔的层数：'))
print("移动路径为：")
hanoi(n,'a','b','c')