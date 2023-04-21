# ERMDS Obfuscation Dataset
ERMDS is an obfuscation dataset designed to evaluate the robustness of Learning-based Malware Detection Systems (LB-MDS). It contains a total of 86,685 malicious software features and 30,455 benign software features. The dataset comprises three sub-datasets: the Binary Obfuscation dataset, the Packing dataset, and the Source Code Obfuscation dataset. Each of these sub-datasets includes samples that have undergone binary-level obfuscation, packing, and source code obfuscation, respectively. The ERMDS-X dataset is the combination of these three sub-datasets.

We extract the feature vectors using the LIEF project (version 0.9.0), the same as the Ember dataset (details can be found here). Each sample is represented as a 2381-feature vector, along with its label (benign or malicious) and malware family if it is malicious. We also release the original binary for malware samples only.

Further details can be found in our paper "ERMDS: An Obfuscation Dataset for Evaluating Robustness of Learning-based Malware Detection Systems".

## Download
The feature vectors and example models are open to everyone. Download the data here: [Google Drive](https://drive.google.com/drive/folders/10Oomg2byEGy3Qiz51MGH7a9sTit1Za-u?usp=sharing)
- ERMDS-X: Contains raw features for all samples
- Models: Contains the Ember model, and we will provide an example of how to use the ERMDS dataset to evaluate the robustness of the EMBER model

We cannot release the original files for the benign software due to copyright considerations. However, we will host the original binaries of malware samples. To avoid misuse, please read and agree to the following conditions before sending us emails. Please email [Lichen Jia](lcjia@gmail.com). Also, please include your Gmail address in the body so that we can add you to the Google Drive folder where the dataset is stored.

- Do not share the data with others (except your co-authors for the project). We are happy to share with other researchers based upon their requests.
- Explain in a few sentences your plan to use these binaries. It does not need to be a precise plan.
- If you are in academia, contact us using your institution's email and provide us with a webpage registered at the university domain that contains your name and affiliation.
- If you are in a research (industrial) lab, send us an email from your company's email account and introduce yourself and your company. In the email, please attach a justification letter (in PDF format) in official letterhead. The letter needs to state clearly the reasons why this dataset is being requested.
Please note that an email not following the conditions might be ignored. We will maintain a public list of organizations accessing these samples at the bottom.
