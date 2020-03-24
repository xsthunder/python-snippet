torch.Tensor.item()
--------
获取scalar tensor的python值
```python
a = torch.tensor(1)
a.item()
```

resumeNER
----------
`emb + lstm + home-made crf`

`Metric, Parser` 作为实例工具函数

`get_data, read_data` 作为带len的迭代器

`C2ID`，作为标签->int的双向映射

[HMM_CRF_torch/CRF.ipynb at master · xsthunder/HMM_CRF_torch](https://github.com/xsthunder/HMM_CRF_torch/blob/master/nb/CRF.ipynb)
