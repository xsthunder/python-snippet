# 左滑动窗口与右滑动窗口，找窗口内最小值所在的x
# 左滑动
import numpy as np
def local_min_from_left(sum_over_height, window_size=None):
    """
    @parmas sum_over_height: numpy.array, with ndim == 1
    @parmas windown_size: size to slip int, default 50
    @returns (local_min, x)
    ----------
    l,r = local_min_from_right(sum_over_height), local_min_from_left(sum_over_height)
    assert l[0]!=r[0] # 值不应该一样, #这两个的[0]不应该一样
    l,r = map(lambda t:t[1], [l,r])
    l,r
    """
    if not isinstance(sum_over_height, np.ndarray):sum_over_height = np.array(sum_over_height)
    assert sum_over_height.ndim == 1
    if window_size == None:window_size = 50
    _min = max(sum_over_height)
    _x = 0
    width = len(sum_over_height)
    for x in range(width):
        # 滑动，有效窗口[ _x-window_size, _x+window_size,]
#         print(x)
        if _x + window_size < x :break # 滑动出界，不得更新
        if _min > sum_over_height[x]:
            _min, _x = sum_over_height[x], x
    return _min, _x

def local_min_from_right(sum_over_height, window_size=None):
    """
    @parmas sum_over_height: numpy.array, with ndim == 1
    @parmas windown_size: size to slip int, default 20
    @returns (local_min, x)
    ----------
    l,r = local_min_from_right(sum_over_height), local_min_from_left(sum_over_height)
    assert l[0]!=r[0] # 值不应该一样, #这两个的[0]不应该一样
    l,r = map(lambda t:t[1], [l,r])
    l,r
    """
    sum_over_height = sum_over_height.copy()
    sum_over_height = np.flip(sum_over_height, 0)
    _min, _x = local_min_from_left(sum_over_height, window_size)
    return _min, len(sum_over_height) - _x

