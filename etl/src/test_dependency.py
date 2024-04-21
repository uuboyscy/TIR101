def input_1(a: str) -> str:
    return ""

def input_2(a: str) -> str:
    return ""

def transform_1(a: str, b: str) -> str:
    return ""

def load(a: str) -> None:
    pass

if __name__ == "__main__":
    input_data_1 = "123"
    input_data_2 = "321"
    source_1 = input_1(input_data_1)
    source_2 = input_2(input_data_2)
    tmp_data = transform_1(source_1, source_2)
    load(tmp_data)

