# deep-video-prior (DVP)

## Dependencey

### Environment
This code is based on tensorflow. It has been tested on Ubuntu 18.04 LTS.

Anaconda is recommended: [Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-18-04)
| [Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04)

After installing Anaconda, you can setup the environment simply by

```
conda env create -f environment.yml
conda activate deep-video-prior
```

### Download VGG model
```
cd deep-video-prior
python download_VGG.py
unzip VGG_Model.zip
```

## Process single image colorization methods' results (for VCGAN, SVCNet)

Note that it is better to only handle one method at one time; forward memory cost for DAVIS dataset: approximately 8500 Mb

1. Put all ground truth grayscale frame subfolders under **/demo/consistency/colorization** and rename them

e.g., rename 'lab-coat' to 'input-lab-coat'; rename 'libby' to 'input-libby'

2. Put all methods' result subfolders under **/demo/consistency/colorization**

note that it is no need to rename them if there are only one method's results are handled

3. Change **subfolder** parameter and run test_svcnet.sh

```bash
bash test1.sh
bash test2.sh
```

if there is question, please see print_all_subfolders.sh

4. Results will be saved in result/colorization/${data}/${method}+DVP

e.g., result/colorization/DAVIS/CIC+DVP

5. Convert all results to formatted files, by running recover_results.py

```bash
python recover_results.py
```
