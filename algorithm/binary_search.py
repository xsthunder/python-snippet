# abc199 d  https://atcoder.jp/contests/abc119/tasks/abc119_d
import bisect
read = input
bisect_right = bisect.bisect_right
# @ see https://docs.python.org/zh-cn/3/library/bisect.html
a ,b , q = map(int, read().split())
INF = 10**18
A =[-INF] + [int(read()) for i in range(a)] +[INF]
B =[-INF] + [int(read()) for i in range(b)] +[INF]
A.sort()
B.sort()
try:
    for i in range(q):
        x = int(read())
        sa = bisect_right(A, x)
        sb = bisect_right(B, x)
        ans = INF
        for pa in [A[sa - 1 ], A[sa]]:
            for pb in [B[sb - 1 ], B[sb]]:
                d1 = abs(x - pa) + abs(pa - pb)
                d2 = abs(x - pb) + abs(pb - pa)
                ans = min(ans, d1, d2)
        print(ans)
except:
    print(x, sa, sb)
