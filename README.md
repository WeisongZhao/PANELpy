
[![website](https://img.shields.io/badge/website-up-green.svg)](https://weisongzhao.github.io/PANELpy/)
[![paper](https://img.shields.io/badge/paper-nat.%20methods-black.svg)](https://www.nature.com/nmeth/)
[![Github commit](https://img.shields.io/github/last-commit/WeisongZhao/PANELpy)](https://github.com/WeisongZhao/PANELpy/)
[![License](https://img.shields.io/github/license/WeisongZhao/PANELpy)](https://github.com/WeisongZhao/PANELpy/blob/master/LICENSE/)<br>
[![Twitter](https://img.shields.io/twitter/follow/weisong_zhao?label=weisong)](https://twitter.com/weisong_zhao/status/1370308101690118146)
[![GitHub watchers](https://img.shields.io/github/watchers/WeisongZhao/PANELpy?style=social)](https://github.com/WeisongZhao/PANELpy/) 
[![GitHub stars](https://img.shields.io/github/stars/WeisongZhao/PANELpy?style=social)](https://github.com/WeisongZhao/PANELpy/) 
[![GitHub forks](https://img.shields.io/github/forks/WeisongZhao/PANELpy?style=social)](https://github.com/WeisongZhao/PANELpy/)


<p>
<h1 align="center">PANEL<font color="#b07219">py</font></h1>
<h6 align="right">v0.4.6</h6>
<h5 align="center">rFRC mapping and PANEL pinpointing with with Python.</h5>
</p>
<br>

<p>
<img src='./img/splash.png' align="left" width=180>
</p>


rFRC (rolling Fourier ring correlation) mapping and simplified PANEL (Pixel-level ANalysis of Error Locations) (w/o RSM) pinpointing. This repository will be in continued development. The full PANEL can be found in [PANELM](https://github.com/WeisongZhao/PANELM). If you find this useful, please cite the corresponding publication. [Weisong Zhao et al. Quantitatively mapping local quality at super-resolution scale by rolling Fourier ring correlation, <!-- Nature Methods -->, X, XXX-XXX (2022)](https://www.nature.com/nmeth/). More details on [demo.ipynb](https://github.com/WeisongZhao/PANELpy/blob/main/demo.ipynb). If it helps your research, please cite our work in your publications. 

<br>
<br>
<br>

<p>
<img src='./img/imagej-128.png' align="right" width=50>
</p>
<br>


More details on [PANELM Wiki](https://github.com/WeisongZhao/PANELM/wiki/) & [PANELJ Wiki](https://github.com/WeisongZhao/PANELJ/wiki/).

## Usages of rFRC and PANEL in specific

The `rFRC` is for quantitatively mapping the local image quality (effective resolution, data uncertainty). The lower effective resolution gives a higher probability to the error existence, and thus we can use it to represent the uncertainty revealing the error distribution.

**rFRC is capable of:**
- **Data uncertainty mapping** of reconstructions without Ground-Truth (Reconstruction-1 vs Reconstruction-2) | 3σ curve is recommended;
- **Data uncertainty and leaked model uncertainty mapping** of deep-learning predictions of low-level vision tasks without Ground-Truth (Prediction-1 vs Prediction-2) | 3σ curve is recommended;
- **Full error mapping** of reconstructions/predictions with Ground-Truth (Reconstruction/Prediction vs Ground-Truth) | 3σ curve is recommended;
- **Resolution mapping** of raw images (Image-1 vs Image-2) | 1/7 hard threshold or 3σ curve are both feasible;

**When two-frame is not accessible, two alternative strategies for single-frame mapping is also provided (not stable, the two-frame version is recommended).** 

**PANEL**

- In this plugin, `PANEL` is a `filtered rFRC` map, for biologists to qualitatively pinpoint regions with low reliability as a concise visualization

- Note that our `rFRC` and `PANEL` cannot fully pinpoint the unreliable regions induced by the model bias, which would require more extensive characterization and correction routines based on the underlying theory of the corresponding models.



## Declaration
This repository contains the Python library for <b>rFRC & PANEL</b> mapping. The development of this Python library is work in progress, so expect rough edges. 

If you want to reproduce the results of the publication, the <b>PANELM</b> (Matlab version) is recommended.  

TO the [PANELM](https://github.com/WeisongZhao/PANELM)


## Version
- v0.4.6 PANEL pinpointing
- v0.3.5 full rFRC mapping
- v0.2.0 Initial rFRC mapping
- v0.1.0 Initial FRC calculation


<details>
<summary><b>Plans</b></summary>

- The single-frame rFRC mapping;
- The RSM combination for full PANEL.

</details>

## Open source [PANELpy](https://github.com/WeisongZhao/PANELpy)

- This software and corresponding methods can only be used for **non-commercial** use, and they are under Open Data Commons Open Database License v1.0.
- Feedback, questions, bug reports and patches are welcome and encouraged!