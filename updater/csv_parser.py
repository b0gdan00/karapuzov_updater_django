import csv
from io import TextIOWrapper

def parse_rrc(uploaded_file):
    data = []
    file_wrapper = TextIOWrapper(uploaded_file.file, encoding="utf-8")
    reader = csv.reader(file_wrapper)

    for row in reader:
        if not row or len(row) < 5:
            continue

        try:
            code = row[0].strip()
            sku = row[1].strip()
            name = row[2].strip()
            price_rrc = row[4].strip().replace(",", ".")  # Заміна коми на крапку

            if code.isdigit() and price_rrc.replace(".", "").isdigit():
                data.append({
                    "code": code,
                    "sku": sku,
                    "name": name,
                    "price_rrc": price_rrc
                })
        except IndexError:
            continue

    return data
