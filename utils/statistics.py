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

def build_profile(records):
    lengths=calculate_text_lengths(records)
    average=calculate_average(lengths)
    maximum=find_max_length(lengths)
    return {
        "record_count":len(records),
        "text_lengths": lengths,
        "average_text_length": average,
        "maximum_text_length": maximum
    }

