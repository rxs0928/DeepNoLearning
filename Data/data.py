import requests
import os
import tensorflow as tf


class Data:
    """
    Description:
     This class provide the download function that can download the data_set to use,for instance: MNIST. And  unzip it.
     Then we  provide the construct function to build own data_set, and return train data, test data and validation set,
     meanwhile, return the iterator too.

    Attributes:
        __dataset_name: (private) the name of the data_set
        __dataset_path: (private) the store path of the set
    Function:
        __init__(): the default initialize function
        download_through_url(): Download the data from Internet
        download_dataset()：  Download the data according to name
        construct_dataset(): Construction of data. making it could be use in different model.
        todo: code the construct_dataset()
    """
    __dataset_name=""
    __dataset_path=""

    def __init__(self, dataset_name: str="", store_type="txt"):
        self.__dataset_name = dataset_name
        self.__data_store_type = "." + store_type
        path_lists = [os.curdir, "dataset", self.__dataset_name]
        for ele in path_lists:
            self.__dataset_path = os.path.join(self.__dataset_path, ele)

    def download_thourgh_url(self, dataset_url):
        dataset_path = self.__dataset_path
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
            resource = requests.get(dataset_url, stream=True)
            file_path = os.path.join(dataset_path,self.__dataset_name+self.__data_store_type)
            with open(file_path, "wb") as file:
                for chunk in resource.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

    def download_dataset(self):
        url = {"mnist": "http://yann.lecun.com/exdb/mnist/", "cifar_10":"http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz", "cifar_100":"http://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz"}
        mnist_data_keys = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz',
                     't10k-labels-idx1-ubyte.gz']
        if self.__dataset_name == "mnist":
            for key in mnist_data_keys:
                mnist_url = url["mnist"]+key
                self.download_thourgh_url(mnist_url)
        elif self.__dataset_name == "cifar_10":
            self.download_thourgh_url(url["cifar_10"])
        elif self.__dataset_name == "cifar_100":
            self.download_thourgh_url(url["cifar_100"])

    # unzip the downloaded data
    def unzip_data(self):pass

    # Description : this function read the download data_sets and build train data and so on,then it return the iterator
    #  of data
    # return: train data_set and test data_set as well as cross validation set
    def consruct_dataset(self): pass


if __name__ == '__main__':
    data = Data('mnist', 'gz')
    data.download_dataset()



