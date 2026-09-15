import json
from datetime import datetime
import matplotlib.pyplot as plt

input_file = input("What is the data file name: ")
with open(input_file, "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

COUNTRY = input("Please input the country you want to see data for: ")

def check_country(record):
    country = record[2]
    return country == COUNTRY

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")
    country_text = eva.get("country")

    if not date_text or not duration_text or not country_text:
        continue

    date = datetime.fromisoformat(date_text)
    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    records.append((date, duration_hours, country_text))

records.sort(key=lambda record: record[0])
records_country = filter(check_country, records)


def cumulate_hour_and_plot(plot_records, country="all countries"):
    dates = []
    cumulative_hours = []
    total_hours = 0

    for date, duration_hours, country_text in plot_records:
        total_hours += duration_hours
        dates.append(date)
        cumulative_hours.append(total_hours)

    plt.plot(dates, cumulative_hours)
    plt.title("Cumulative hours for " + country)
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")
    plt.tight_layout()
    plt.savefig(f"cumulative_duration_{COUNTRY}.png")
    plt.show()

cumulate_hour_and_plot(records)
cumulate_hour_and_plot(records_country, COUNTRY)