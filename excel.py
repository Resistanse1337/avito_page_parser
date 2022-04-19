import xlwt

from db import AvitoDb


def get_all_data_from_db():
    avito_db = AvitoDb()
    all_data = avito_db.get_all_data()
    headers = avito_db.get_headers()
    avito_db.close_connection()

    return all_data, headers


def make_excel(data, headers):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("result")

    headers_chars = {}

    max_column = 0

    i = 0
    for key in headers:
        if key in ["chars_names", "chars_values"]:
            pass
        else:
            ws.write(0, i, key)
            i += 1
            max_column += 1

    for i, dt in enumerate(data):
        col = 0
        for j, v in enumerate(dt):
            if j == 5:
                tmp_headers = v.split("|")
                tmp_values = dt[j+1].split("|")
                for h_ind, h in enumerate(tmp_headers):
                    if headers_chars.get(h) is None:
                        max_column += 1
                        headers_chars.update({h: max_column})
                        ws.write(0, max_column, h)
                    ws.write(i + 1, headers_chars[h], tmp_values[h_ind])
            elif j == 6:
                pass
            else:
                ws.write(i+1, col, v)
                col += 1

    wb.save("result.xls")


if __name__ == "__main__":
    all_data, headers = get_all_data_from_db()
    make_excel(all_data, headers)














