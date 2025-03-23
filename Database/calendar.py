from app import db

# Geopolitics
class CalendarEvent(db.Model):
    __tablename__ = 'calendar_events'

    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.String(64), nullable=False)
    region = db.Column(db.String(64), nullable=False)
    event = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<CalendarEvent {self.event_date} | {self.region} | {self.event[:30]}...>"

# Macrodata
class MacroData(db.Model):
    __tablename__ = 'macrodata'

    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(10), nullable=False)
    event_name = db.Column(db.String(255), nullable=False)
    reference_date = db.Column(db.String(64), nullable=False)
    latest_value = db.Column(db.String(64), nullable=True)
    previous_value = db.Column(db.String(64), nullable=True)
    expected_value = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f"<MacroData {self.country_code} | {self.event_name} | {self.reference_date}>"

# Recapdata
class RecapData(db.Model):
    __tablename__ = 'recapdata'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64), nullable=False)
    time = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    event = db.Column(db.Text, nullable=False)
    actual = db.Column(db.String(64), nullable=True)
    expected = db.Column(db.String(64), nullable=True)
    previous = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f"<RecapData {self.date} | {self.country} | {self.event[:30]}...>"