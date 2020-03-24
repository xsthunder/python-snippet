



draw two chart in one pic 
----------
[HMM_CRF_torch/CRF.ipynb at master · xsthunder/HMM_CRF_torch](https://github.com/xsthunder/HMM_CRF_torch/blob/master/nb/CRF.ipynb)
```python
import matplotlib.pyplot as plt
def pxy(x, y, name='idk', plt=plt, ):
    name = str(name)
    fig, = plt.plot(x,y, )
    fig.set_label(name)
    plt.legend()

# plot layout 1 * 2
fig, m_axs = plt.subplots(1, 2, figsize = (10, 3)) 
pxy(range(len(epo_losses)), epo_losses, 'train-mean-loss', plt=m_axs[0])
pxy(range(len(epo_acces)), epo_acces, 'dev-acc', plt=m_axs[1])
```
