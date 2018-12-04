#!/bin/python

from roomai.games.common import AbstractStatePublic

class PublicPersonInfo(object):
    def __init__(self):
        self.__num_hand_cards__  = 0
        self.__charactor_card__  = None
        self.__equipment_cards__ = []


class BangStatePublic(AbstractStatePublic):
    def __init__(self):
        self.__public_person_info__  = []
        self.__sheriff_id__          = 0
        self.__discard_pile__        = []

    def __get_public_person_info__(self):   return tuple(self.__public_person_info__)
    public_person_info = property(__get_public_person_info__, doc="The person info in public")

    
