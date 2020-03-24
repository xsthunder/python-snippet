torch.tensor
----------
tensor.tensor(1, requre_grad=True) # 需要grad的话，初始化就要设置
tensor.tensor(1, dtype=Tensor.int64) # 而不是tensor.Tensor，可以看成工厂类


torch.Tensor.item()
--------
获取scalar tensor的python值
```python
a = torch.tensor(1)
a.item() # 1
```

resumeNER
----------
`emb + lstm + home-made crf`

`Metric, Parser` 作为实例工具函数

`get_data, read_data` 作为带len的迭代器

`C2ID`，作为标签->int的双向映射

[HMM_CRF_torch/CRF.ipynb at master · xsthunder/HMM_CRF_torch](https://github.com/xsthunder/HMM_CRF_torch/blob/master/nb/CRF.ipynb)
