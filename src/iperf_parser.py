import re


def parser(result):
    result = re.sub("\[.*\]", "", result.strip())
    lines = result.split("\n")
    for line in lines:
        if re.search("^\D*$", line) and line:
            result = re.sub(line, "*", result)
    res_section = result.split("*")[1].strip()
    lines = res_section.split("\n")
    dict = []
    for line in lines:
        line_dict = {}
        params = re.split("\s+", line.strip())
        line_dict["Interval"] = params[0]
        line_dict["Transfer"] = params[2]
        line_dict["Bitrate"] = params[4]
        line_dict["Retr"] = params[6]
        line_dict["Cwnd"] = params[7]
        dict.append(line_dict)
    return dict
