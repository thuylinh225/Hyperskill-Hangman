def heading(text, level=1):
    if level <= 1:
        return "# " + text
    if level >= 6:
        return "###### " + text
    return level * "#" + " " + text
