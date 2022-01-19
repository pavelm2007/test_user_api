from enum import Enum


class GenderTypes(Enum):
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
