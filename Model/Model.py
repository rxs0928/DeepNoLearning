# -*-coding:utf-8-*-
class Model:

    """
    Notation:
    We define some common operation and attribute here.This file may update according to the developing process,as the
    minute we found some update we will update this file soon.This is just a beta framework.You should inherit this par-
    ent class to describe your own model.

    Class description:
    The parent class of different model

    Attribute Description:
        1.__model_name: (Private)  The name of one model, such as "ResNet', "GAN"
        2.__layer_num: (Private)  The depth of one model

    Function Description: Define the Structure of the Model you want construct
        1. __model_structure(self):(Private) Define the Structure of the Model you want construct
        2. __opt_select(self):(Private) Define some optimization method you want to use in the training
    """

    __model_name = ""  # The name of one model, such as "ResNet', "GAN"
    __layer_num = 0  # The depth of one model

    # The default initialize method
    def __init__(self, name: str = "model_name", layer_num: int = 0):
        self.__model_name = name
        self.__layer_num = layer_num
        print(self.__layer_num)
        print(self.__model_name)

    # Define the Structure of the Model you want construct
    def __model_structure(self): pass

    # Define some optimization method you want to use in the training
    def __opt_select(self): pass

    # Define the loss_function
    def __loss(self):pass

    #
