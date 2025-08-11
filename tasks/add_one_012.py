from typing import Union

import logconfig

logging = logconfig.get_logger(__name__)

# Original version
def add_one(num):
    return num + 1

# Improved version
def add_one_improved(object: Union[int, float]) -> Union[int, float]:
    if not isinstance(object, (int, float)):
        logging.error(f"invalid argument type:{type(object).__name__}")
        raise TypeError(
            f"Argument 'object' must be int or float, got {type(object).__name__}"
        )
    logging.info(f"add_one_improved({round(object+1, 2)})")
    return round(object + 1, 2)


if __name__ == "__main__":
    print("add_one(6) returns:")
    print(add_one(6))
