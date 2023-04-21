# ERMDS: A Ofuscation Dataset for Evaluating Robustness of Learning-based Malware Detection System

ERMDS是一个混淆数据集， 可以被用来评估Learning-based Malware Detection System (LB-MDS)的鲁棒性，共包含86685个恶意软件的特征以及30455个良性程序的特征。 该数据集 comprises three sub-datasets: the Binary obfuscation dataset, the Packing dataset, and the Source Code obfuscation dataset. Each of these sub-datasets includes samples that have undergone binary-level obfuscation, packing, and source code obfuscation, respectively. The ERMDS-X dataset is the combination of these three sub-datasets.

We extract the feature vectors using the LIEF project (version 0.9.0), the same as the Ember dataset (details can be found here). Each sample is represented as a 2381 feature vector, along with its label (benign or malicious) and malware family if it’s malicious. We also release the original binary for malware samples only.

Further details can be found in our paper “ERMDS: A Obfuscation Dataset for Evaluating Robustness of Learning-based Malware Detection System”.

# Download
The feature vectors and 以及示例模型 are open to everyone. Download the data here: [Google Drive](https://drive.google.com/drive/folders/10Oomg2byEGy3Qiz51MGH7a9sTit1Za-u?usp=sharing)
 ERMDS-X: 其中包含所有样本的raw feature 
 Models：其中包含ember模型，我们会给定一个例子，说明如何在EMBER模型上使用ERMDS数据集来评估其鲁棒性

We cannot release the original file for the benign software due to copyright considerations. But we will host the original binaries of malware samples. To avoid misuse, please read and agree to the following conditions before sending us emails. Please email [Lichen Jia](lcjia@gmail.com). Also, please include your Gmail address in the body so that I can add you to the google drive folder where the dataset is stored.
- Do not share the data with any others (except your co-authors for the project). We are happy to share with other researchers based upon their requests.
- Explain in a few sentences of your plan to do with these binaries. It should not be a precise plan.
- If you are in academia, contact us using your institution email and provide us a webpage registered at the university domain that contains your name and affiliation.
- If you are in research (industrial) labs, send us an email from your company’s email account and introduce yourself and company. In the email, please attach a justification letter (in PDF format) in official letterhead. The letter needs to state clearly the reasons why this dataset is being requested.

Please note that an email not following the conditions might be ignored. And we will keep the public list of organizations accessing these samples at the bottom.

