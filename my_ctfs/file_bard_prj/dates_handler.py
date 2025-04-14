from datetime import datetime
def add_trailing_zeros_for_date(date):
    try:
        parts = date.split('.')
        if len(parts) == 3:
            day = parts[0].zfill(2)
            month = parts[1].zfill(2)
            year = parts[2]
            return f"{day}.{month}.{year}"
    except Exception:
        return ""

def get_msgs_from_specific_dates_range(file_content: str, start_date: str, end_date: str) -> str:
    in_range = False
    msgs = file_content.split("\n")
    updated_msgs = []
    # Convert input dates to datetime objects
    try:
        start = datetime.strptime(start_date, "%d.%m.%Y")
        end = datetime.strptime(end_date, "%d.%m.%Y")
    except Exception as e:
        print(e)
        return file_content

    for line in msgs:
        if not line.strip():
            continue
        # Assuming each line starts with the date in 'YYYY-MM-DD' format
        try:
            line_date_arr = line.split('.') # 'YYYY.MM.DD'
            try:
                line_date_arr[2] = line_date_arr[2][:line_date_arr[2].find(",")]
                line_date_str = line_date_arr[0]+'.'+line_date_arr[1]+'.'+line_date_arr[2]
            except Exception as e:
                raise ValueError
            line_date = datetime.strptime(line_date_str, "%d.%m.%Y")
            if start <= line_date <= end:
                in_range = True
                updated_msgs.append(line)
            else:
                in_range = False
        except ValueError:
            # Line does not start with a valid date - means that the user typed a new line
            #we need to check if the previous line was inside the date range...
            if in_range and len(updated_msgs) > 0:
                updated_msgs[-1] = updated_msgs[-1]+"\n"+line

    return "\n".join(updated_msgs)


def tes1t():
    with open("file.txt","r",encoding="utf-8") as f:
        text = f.read()
        get_msgs_from_specific_dates_range(text,"14.00.2024","14.01.2024")