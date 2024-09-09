# Interchangeable adapter for the different ways to assign a tag.
def convert_lines_to_char_idx(text_box, line_info:str):
    line, char = map(int, text_box.index(line_info).split("."))
    char_index = 0
    for i in range(line - 1):
        char_index += (
            len(text_box.get(f"{i + 1}.0", f"{i + 1}.end")) + 1
        )  # +1 for line break
    char_index += char
    return char_index

def covert_char_idx_to_lines(text:str, char_index:int):
    lines = text.split("\n")
    line_index = 1
    char_count = 0
    for line in lines:
        char_count += len(line) + 1  # +1 for line break
        if char_count > char_index:
            char_index_in_line = char_index - (char_count - len(line))
            return f"{line_index}.{char_index_in_line}"
        line_index += 1
    return ""
    
