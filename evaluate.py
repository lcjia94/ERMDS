import os
import sys
import hashlib
import time
import datetime
import pefile
import json
from models import *

#from ember import predict_sample
#import lightgbm as lgb
#import numpy as np
import glob
#from torch.autograd import Variable

MALCONV_MODEL_PATH = 'models/malconv/malconv.checkpoint'
EMBER_2019_MODEL_PATH = 'models/ember_2019/ember_model.txt'


class Classifier:
    def __init__(self, classifier_name):
        if classifier_name == 'malconv':
            self.model = MalConvModel( MALCONV_MODEL_PATH, thresh=0.5 )
        elif classifier_name == 'ember':
            self.model = EmberModel_2019( EMBER_2019_MODEL_PATH, thresh=0.8336 )
        #elif classifier_name == 'clamav':
        #    self.model = ClamAV()
        else:
            print('bad classifier_name, please check configure')
            exit()

def try_parse_pe(sample_path):
    try:
        pe = pefile.PE(sample_path)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        return False
    return True



    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("illegal input")
        exit(0)

    _, mode = sys.argv

    bins = []
    if mode == 'all':
        datasets = [r'ERMDS-X/BOS_benign.json', r'ERMDS-X/BOS_malware.json', r'ERMDS-X/SOS_benign.json', r'ERMDS-X/POS_benign.json', r'ERMDS-X/POS_malware.json']
    elif mode == 'BOS':
        datasets = [r'ERMDS-X/BOS_benign.json', r'ERMDS-X/BOS_malware.json']
    elif mode == 'SOS':
        datasets = [r'ERMDS-X/SOS_benign.json']
    elif mode == 'POS':
        datasets = [r'ERMDS-X/POS_benign.json', r'ERMDS-X/POS_malware.json']
    else:
        # datasets = [r'ERMDS-X/test.json']
        print("illegal input")
        exit(0)

    for dataset in datasets:
        with open(dataset, 'r') as f:
            bins += f.readlines()


    # malconv = Classifier('malconv')
    ember = Classifier('ember')
    
    print(f"evaluation begin, mode: {mode}")
   
    cnt = 0
    num = 0
    for bin in bins:
        try:
            feature = json.loads(bin)
        except:
            continue
        
        num += 1
        label = feature['label']
        is_benign = label == 0
        obfuscation_method = feature['obfuscation']

        predict_is_benign = ember.model.is_evasive(feature)
        if predict_is_benign == is_benign:
            cnt += 1
        print(f"predict_is_benign: {predict_is_benign}, label: {is_benign}, {obfuscation_method}")

    print(f"file nums: {num}, accuracy: {cnt}/{num}={cnt/num}")

    
    