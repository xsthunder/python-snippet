# 运行

https://github.com/xsthunder/LatticeLSTM
本地 `jupyter-ws/example-git/LatticeLSTM-pycharm-y50` 数据`jupyter-ws/example-git/CCKS-Data-Use`

## TODO

## 待研究及pull request

2. seqeval在python2的下，评价`zengjianjun/jupyter-ws/example-git/LatticeLSTM-pycharm-y50/ccks-output/dataset_1/1218-0945/model.75.model.test.json`会报错

## pytorch代码结构

1. 复杂计算分开，分为`#1运行慢，加载慢`和`#2运行慢，加载快`，`#2`可以拆出来
2. `#1 load model`，`#2 计算词典`，`#2 计算词典匹配`，`--status test的decode`
3. error.log也要导入到run.log

## 设计

### `--status train`

1. 允许指定dset，直接Load。存在的时候跳过计算dset的过程。
1. 允许指定`--model_input_data` `{train:[], test:[], dev:[]}`的`json`文件，存在时跳过计算转换
1. 需要指定`--output_dir`，在没有指定1,2时保存到该目录下并且该目录名称应该随着事件变化
1. 允许指定`--savedmodel`，允许断点训练


#### train bash

https://github.com/xsthunder/python-snippet/blob/master/latticeLstm/train.sh

### `--status test`

1. 设计`metrics.py`，允许独立运行，指定`argparse`，此时打印结果
2. 允许指定允许指定`--model_input_data` `{test:[], dev:[]}`的`json`文件，存在时跳过计算转换
3. 需要指定`--savedmodel`

#### `seqeval_file.py`

https://github.com/xsthunder/python-snippet/blob/master/latticeLstm/seqeval_file.py


#### test bash
[test.sh](https://github.com/xsthunder/python-snippet/blob/master/latticeLstm/test.sh)输出decode test/dev 的结果 以及 ground-truth 结果
调用（使用不同env）[seqeval.sh](https://github.com/xsthunder/python-snippet/blob/master/latticeLstm/seqeval_all.sh)

### 同时显示所有log

https://github.com/xsthunder/python-snippet/blob/master/latticeLstm/print_log.sh
