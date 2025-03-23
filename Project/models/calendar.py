import csv
from ..db import get_db
from googletrans import Translator
def load_calendar_events(csv_path):
    db = get_db()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO calendar_events (event_date, region, event) VALUES (?, ?, ?)',
                (row['Date'], row['Region'], row['Event'])
            )
    db.commit()

def load_macro_data(csv_path):
    db = get_db()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                '''INSERT INTO macrodata (country_code, event_name, reference_date, latest_value, previous_value, expected_value)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                (
                    row['calendar-iso'],
                    row['calendar-event'],
                    row['calendar-reference'],
                    row['calendar-item'],
                    row['calendar-item (2)'],
                    row['calendar-item (3)']
                )
            )
    db.commit()

def load_recap_data(csv_path):
    db = get_db()
    translator = Translator()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date_cn = row['Date']
            time_cn = row['Time']
            country_cn = row['Country']
            event_cn = row['Event']
            actual_cn = row.get('Actual', None)
            expected_cn = row.get('Expected', None)
            previous_cn = row.get('Previous', None)
            date_en = translator.translate(date_cn, dest='en').text if date_cn else ''
            time_en = translator.translate(time_cn, dest='en').text if time_cn else ''
            country_en = translator.translate(country_cn, dest='en').text if country_cn else ''
            event_en = translator.translate(event_cn, dest='en').text if event_cn else ''
            actual_en = translator.translate(actual_cn, dest='en').text if actual_cn else None
            expected_en = translator.translate(expected_cn, dest='en').text if expected_cn else None
            previous_en = translator.translate(previous_cn, dest='en').text if previous_cn else None
            db.execute(
                '''INSERT INTO recapdata (date, time, country, event, actual, expected, previous)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (
                    date_en,
                    time_en,
                    country_en,
                    event_en,
                    actual_en,
                    expected_en,
                    previous_en
                )
            )
    db.commit()

