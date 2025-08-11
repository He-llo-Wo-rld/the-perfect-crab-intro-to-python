# Video alternative: https://vimeo.com/954334266/1ad4327868
import logging
from typing import Union

import logconfig

# Original version
logger = logging.getLogger(__name__)


def just_return_it(num):
    return num


# Improved version


def just_return_it_improved(object: Union[int, float]) -> Union[int, float]:
    if not isinstance(object, (int, float)):
        logger.error(f"Invalid argument type: {type(object).__name__}")
        return None
    logger.info(f"just_return_it_improved({object}) called")
    return object


if __name__ == "__main__":
    print("just_return_it(4) returns:")
    print(just_return_it(4))
