from db import AvitoDb
from avito_parser import parse_avito
from excel import make_excel, get_all_data_from_db


if __name__ == "__main__":
    with open("saved_avito_page.html", encoding="utf8") as f:
        html = f.read()

    avito_data = parse_avito(html)
    avito_data["chars_names"] = "|".join(avito_data["chars_names"])
    avito_data["chars_values"] = "|".join(avito_data["chars_values"])
    avito_data["images"] = "|".join(avito_data["images"])

    avito_db = AvitoDb()
    avito_db.insert_row(list(avito_data.values()))
    avito_db.close_connection()

    all_data, headers = get_all_data_from_db()
    make_excel(all_data, headers)









