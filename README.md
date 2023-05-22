# ERMDS Obfuscation Dataset

## Introduction
ERMDS is an obfuscation dataset designed to evaluate the robustness of Learning-based Malware Detection Systems (LB-MDS). It contains a total of 86,685 malicious software features and 30,455 benign software features. The dataset comprises three sub-datasets: the Binary Obfuscation dataset, the Packing dataset, and the Source Code Obfuscation dataset. Each of these sub-datasets includes samples that have undergone binary-level obfuscation, packing, and source code obfuscation, respectively. The ERMDS-X dataset is the combination of these three sub-datasets.

We extract the feature vectors using the [LIEF](https://lief.quarkslab.com/) project (version 0.9.0), the same as the [Ember](https://github.com/elastic/ember) dataset (details can be found [here](https://github.com/elastic/ember/blob/master/ember/features.py)). Each sample is represented as a 2381-feature vector, along with its label (benign or malicious) and malware family if it is malicious. We also release the original binary for malware samples only.

Further details can be found in our paper "ERMDS: An Obfuscation Dataset for Evaluating Robustness of Learning-based Malware Detection Systems" [PDF]().

## Download
The feature vectors and example models are open to everyone. Download the data here: [Google Drive](https://drive.google.com/drive/folders/10Oomg2byEGy3Qiz51MGH7a9sTit1Za-u?usp=sharing)
- ERMDS-X: Contains raw features for all samples
- Models: Contains the Ember model, and we will provide an example of how to use the ERMDS dataset to evaluate the robustness of the EMBER model

<!-- We cannot release the original files for the benign software due to copyright considerations. However, we will host the original binaries of malware samples. **To avoid misuse, please read and agree to the following conditions before sending us emails.** Please email [Lichen Jia](lcjia@gmail.com). Also, please include your Gmail address in the body so that we can add you to the Google Drive folder where the dataset is stored.

- Do not share the data with others (except your co-authors for the project). We are happy to share with other researchers based upon their requests.
- Explain in a few sentences your plan to use these binaries. It does not need to be a precise plan.
- If you are in academia, contact us using your institution's email and provide us with a webpage registered at the university domain that contains your name and affiliation.
- If you are in a research (industrial) lab, send us an email from your company's email account and introduce yourself and your company. In the email, please attach a justification letter (in PDF format) in official letterhead. The letter needs to state clearly the reasons why this dataset is being requested.

Please note that an email not following the conditions might be ignored. We will maintain a public list of organizations accessing these samples at the bottom. -->

## Installation
1. Clone this repo from git:

```bash
git clone https://github.com/lcjia94/ERMDS.git
```

2. We recommend setting up a Python 3.6.9 virtual environment (other Python 3.7 or above versions might also work but didn't test).

```bash
cd ERMDS
pip install -r requirements.txt
```

## Assessing the Robustness of MDS using ERMDS:
1. Evaluate the robustness of MDS using all datasets from ERMDS-X

```bash
python evaluation.py ALL
```

2. Evaluate the robustness of MDS using the BOS dataset from ERMDS-X

```bash
python evaluation.py BOS
```
3. Evaluate the robustness of MDS using the SOS dataset from ERMDS-X

```bash
python evaluation.py SOS
```
4. Evaluate the robustness of MDS using the POS dataset from ERMDS-X

```bash
python evaluation.py POS
```

## How to Expand the ERMDS Dataset:
To facilitate future researchers in defining their own datasets or expanding the ERMDS dataset, we provide a feature extraction script called feature.py. Modify the paths in this file and run the script to obtain sample features in JSON format.

```bash
python feature.py
```

## Citing
```
@article{JIA2023100106,
title = {ERMDS: A obfuscation dataset for evaluating robustness of learning-based malware detection system},
journal = {BenchCouncil Transactions on Benchmarks, Standards and Evaluations},
volume = {3},
number = {1},
pages = {100106},
year = {2023},
issn = {2772-4859},
doi = {https://doi.org/10.1016/j.tbench.2023.100106},
url = {https://www.sciencedirect.com/science/article/pii/S2772485923000236},
author = {Lichen Jia and Yang Yang and Bowen Tang and Zihan Jiang},
keywords = {Dataset, Malware detection system, Security, Machine learning, Adversarial malware}
}
```
