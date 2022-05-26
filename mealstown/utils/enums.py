from enum import Enum


class EnumParticipantGenderTypes(Enum):
    MALE = 1,
    FEMALE = 2,
    UNDISCLOSED = 3,
    OTHERS = 4


class QuestionTypeChoice(Enum):
    CHECK_BOX = 1
    RADIO_BUTTON = 2
    RATING_SCALE = 3
    LINEAR_RATING_SCALE = 4
    TEXT_LONG = 5
    TEXT_SHORT = 6
    EMAIL = 7
    MULTIPLE_CHOICE_GRID = 8
    CHECKBOX_GRID = 9
    DATE = 10
    TIME = 11

    QUESTION_CHOICES = (
        (CHECK_BOX, 'CHECK BOX'),
        (RADIO_BUTTON, 'RADIO BUTTON'),
        (RATING_SCALE, 'RATING_SCALE'),
        (LINEAR_RATING_SCALE, 'LINEAR RATING SCALE'),
        (TEXT_LONG, 'TEXT LONG'),
        (TEXT_SHORT, 'TEXT SHORT'),
        (EMAIL, 'EMAIL'),
        (MULTIPLE_CHOICE_GRID, 'MULTIPLE CHOICE GRID'),
        (CHECKBOX_GRID, 'CHECKBOX GRID'),
        (DATE, 'DATE'),
        (TIME, 'TIME'),
    )

