https://docs.python.org/zh-cn/3/library/profile.html#pstats.Stats.sort_stats

`python -u -m cProfile -s cumulative su.py | tee su.log`

https://docs.python.org/zh-cn/3/library/profile.html#instant-user-s-

```
    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    4394/1    0.179    0.000  390.088  390.088 {built-in method builtins.exec}
         1    0.005    0.005  390.088  390.088 success-beam-search-line-profile.su.py:10(<module>)
         1    0.045    0.045  360.899  360.899 success-beam-search-line-profile.su.py:579(timeSuSingle)
      1487    0.059    0.000  360.720    0.243 success-beam-search-line-profile.su.py:183(generate)
      1487    3.336    0.002  349.942    0.235 success-beam-search-line-profile.su.py:192(beam_search)
     13138    7.717    0.001  332.245    0.025 snippets.py:456(new_predict)
     13138    0.212    0.000  324.528    0.025 success-beam-search-line-profile.su.py:176(predict)
     13138    0.295    0.000  323.492    0.025 training.py:1363(predict)
     13138    1.529    0.000  310.813    0.024 training_arrays.py:223(predict_loop)
     13138    0.892    0.000  306.003    0.023 backend.py:3438(__call__)
     13138    0.117    0.000  288.999    0.022 session.py:1464(__call__)
     13138  288.874    0.022  288.874    0.022 {built-in method _pywrap_tensorflow_internal.TF_SessionRunCallable}
         1    0.001    0.001   18.981   18.981 models.py:2277(build_transformer_model)
     13141    0.140    0.000   15.265    0.001 backend.py:460(get_session
```

ncalls

    调用次数
tottime

    在指定函数中消耗的总时间（不包括调用子函数的时间）
percall

    是 tottime 除以 ncalls 的商
cumtime

    指定的函数及其所有子函数（从调用到退出）消耗的累积时间。这个数字对于递归函数来说是准确的。
percall

    是 cumtime 除以原始调用（次数）的商（即：函数运行一次的平均时间）
