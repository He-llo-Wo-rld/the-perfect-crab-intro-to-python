# Video alternative: https://vimeo.com/954334266/1ad4327868
import logging

import logconfig

# Original version
logger = logging.getLogger(__name__)


def just_return_it(num):
    return num


# Improved version


def just_return_it_improved(num: int) -> int:
    logger.info(f"just_return_it_improved({num}) called")
    return num


if __name__ == "__main__":
    print("just_return_it(4) returns:")
    print(just_return_it(4))
