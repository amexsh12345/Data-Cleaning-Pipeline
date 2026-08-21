import json
from pathlib import Path

DATA_PATH=Path("D:\工作\Data-Cleaning-Pipeline\data\student.json")


def load_data(path):
    with path.open("r",encoding="utf-8") as file:
        records =json.load(file)
    if not isinstance(records,list):
        raise ValueError("JSON顶层结构必须是一个列表")
    return records

def filter_valid_records(records):
    valid_records=[]
    skipped_count=0
    for record in records:
        if not isinstance(record,dict):
            skipped_count+=1
            continue
        if record.get("id") is None or record.get("text") is None:
            skipped_count +=1
            continue
        if not isinstance(record["text"],str):
            skipped_count+=1
            continue
        valid_records.append(record)
    return valid_records,skipped_count
def calculate_text_lengths(records):
    lengths=[]
    for record in records:
        text = record["text"]
        lengths.append(len(text))
    return lengths
def calculate_average(lengths):
    if not lengths:
        return None
    return sum(lengths)/len(lengths)

def filtered_count(lengths):
    filterd = 0
    for length in lengths:
        if length<=10:
            filterd += 1
    kept=len(lengths)-filterd
    return filterd,kept

def find_longest_texts(maximum,records,lengths):
    if not lengths:
        return None
    longest_texts=[]
    for record in records:
        if len(record["text"])==maximum:
            longest_texts.append(record["text"])
    return longest_texts

def find_max_length(lengths):
    if not lengths:
        return None
    maximum=lengths[0]
    for length in lengths[1:]:
        if length >maximum:
            maximum=length
    return maximum
def main():
    try:
        records = load_data(DATA_PATH)
    except FileNotFoundError:
        print(f"找不到文件：{DATA_PATH}")
        return
    except json.JSONDecodeError:
        print(f"JSON 格式错误：{DATA_PATH}")
        return
    except ValueError as error:
        print(f"数据结构错误：{error}")
        return

    valid_records,skipped_count=filter_valid_records(records)
    lengths= calculate_text_lengths(valid_records)
    calculate_average(lengths)
    maximum_length=find_max_length(lengths)
    filtered,kept=filtered_count(lengths)
    longest_texts=find_longest_texts(maximum_length,valid_records,lengths)
    print(f"Loaded {len(records)} records")
    print(f"Valid records: {len(valid_records)}")
    print(f"Skipped records: {skipped_count}")
    if calculate_average(lengths) is None:
        print("No valid text is available for statistics.")
        return
    print(f"Average text length: {calculate_average(lengths):.1f}")
    print(f"Maximum text length: {maximum_length}")
    print(f"Filtered:{filtered},kept:{kept}")
    print(f"longest texts:{longest_texts}")
if __name__ == "__main__":
    main()