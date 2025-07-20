import os

def read_data() -> str:
    file_path = os.path.join(os.path.dirname(__file__), "data.md")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_chunks() -> list[str]:
    content: str = read_data()
    chunks: list[str] = content.split("\n\n")
    result: list[str] = []
    header: Literal[''] =""
    for chunk in chunks:
        if chunk.startswith("#"):
            header += f"{chunk}\n"
        else:
            result.append(f"{header}{chunk}")
            header = ""
    return result

if __name__ == '__main__':
    chunks: list[str] = get_chunks()
    # print("Current working directory:", os.getcwd())
    for chunk in chunks:
        print(chunk)
        print("-------")
