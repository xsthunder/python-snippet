
```
output_ids_array = array([[1275]])
```

# 索引为tuple的列表

```
output_ids_array[[(0), (0)]] # array([[1275],       [1275]])
```


# 索引为arr的列表

错误结果，注意argwhere返回非零索引列表，也是采用这种形式，所以要对第一维tuple化。

官方提示不适宜用argwhere结果做索引[The output of argwhere is not suitable for indexing arrays. For this purpose use nonzero(a) instead.](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html?highlight=argwhere#numpy.argwhere)

应使用nonzero

Using a non-tuple sequence for multidimensional indexing is deprecated; 
use `arr[tuple(seq)]` instead of `arr[seq]`. 
In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
```
output_ids_array[[[0], [0]]] # array([1275]) # 不清楚行为的原理
```

# 使用nonzero

用[numpy.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html?highlight=nonzero)代替，返回的是c-like的索引列表`[[i_1的列表],[i_2的列表], [i_2的列表],]`，符合分维度切片的原理如`np.arange(9).reshape((3,3,))[::-1, ::-1]`。

做好所以索引列表，传入，不能用`::`语法，同nonezero结果。

```
output_ids_array = array([[1275],[1276] ])
to_take_idx = np.nonzero( array([ True, True ]) ) 
output_ids_array[to_take_idx] # array([[1275],       [1276]])
```
