# -*- coding: utf-8 -*-
"""
@author: Ardalan MEHRANI <ardalan77400@gmail.com>
@brief:
"""

import os
import sys
import csv
import tarfile
import shutil
import hashlib
from tqdm import tqdm
from urllib.request import urlretrieve
from urllib.error import URLError
from urllib.error import HTTPError
csv.field_size_limit(sys.maxsize)
DATA_FOLDER = "datasets"


class Twitter(object):
    def __init__(self):

        self.data_name = "twitter"
        self.data_folder = "{}/{}/raw".format(DATA_FOLDER, self.data_name)
        self.n_classes = 2
        

    @staticmethod
    def _generator(filename):

        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f, quotechar='"')
            for line in reader:
                sentence = line['sentence']
                label = int(line['label'])
                # if sentence and label:
                yield sentence, label

    def load_train_data(self):
        return self._generator(os.path.join(self.data_folder, "train.csv"))

    def load_test_data(self):
        return self._generator(os.path.join(self.data_folder, "test.csv"))


def load_datasets(names=["ag_news", "imdb"]):
    """
    Select datasets based on their names

    :param names: list of string of dataset names
    :return: list of dataset object
    """

    datasets = []
    if 'twitter' in names:
        datasets.append(Twitter())
    return datasets


if __name__ == "__main__":

    names = [
        'twitter'
    ]

    for name in names:
        print("name: {}".format(name))
        dataset = load_datasets(names=[name])[0]
        
        # train data generator
        gen = dataset.load_train_data()
        sentences, labels = [], []
        for sentence, label in tqdm(gen):
            sentences.append(sentence)
            labels.append(label)
        print(" train: (sentences,labels) = ({}/{})".format(len(sentences), len(labels)))

        # test data generator
        gen = dataset.load_test_data()
        sentences, labels = [], []
        for sentence, label in tqdm(gen):
            sentences.append(sentence)
            labels.append(label)
        print(" train: (sentences,labels) = ({}/{})".format(len(sentences), len(labels)))
