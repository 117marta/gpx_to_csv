import csv
from lxml import etree


NAME_SPACE = "http://www.topografix.com/GPX/1/1"
HEADERS = (
    "Szerokość geograficzna",
    "Długość geograficzna",
    "Wysokość [m]",
    "Czas (UTC)",
    "Czas (Warszawa)",
    "Prędkość [m/s]",
    "Prędkość [km/s]",
    "Kurs [rad]",
    "Kurs [deg]",
    "Nazwa",
    "Opis",
    "Długość [km]",
    "Czas trwania [ms]",
)


def get_gpx_data():
    tree = etree.parse("input.gpx")
    root_tree = tree.getroot()
    output = [HEADERS]

    for trk in root_tree.iter("{%s}trk" % NAME_SPACE):
        name = trk.find("{%s}name" % NAME_SPACE).text
        description = trk.find("{%s}desc" % NAME_SPACE).text
        short_info = (None, None, None, None, None, None, None, None, None, None, None, name, description)
        output.append(short_info)

    return output


def gpx_to_csv():
    with open(file="output.csv", mode="x") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(get_gpx_data())


gpx_to_csv()
