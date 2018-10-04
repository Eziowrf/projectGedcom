def FormatDate(date):
    def monthToNum(month):
        numbers = {
            "JAN": "01",
            "FEB": "02",
            "MAR": "03",
            "APR": "04",
            "MAY": "05",
            "JUN": "06",
            "JUL": "07",
            "AUG": "08",
            "SEP": "09",
            "OCT": "10",
            "NOV": "11",
            "DEC": "12",
        }
        return numbers.get(month, None)
    if date != "NA":
        date_list = date.split(' ')
        return date_list[2] + '-' + monthToNum(date_list[1]) + '-' + date_list[0].zfill(2)
    else:
        return "NA"