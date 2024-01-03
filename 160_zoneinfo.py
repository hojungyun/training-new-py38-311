# TIME ZONES PRIOR TO PYTHON 3.9
# - By default datetime objects have no time zone information
# - You can add a time zone to a date using the tz attribute in date/time creation methods

from datetime import datetime, timezone, timedelta

print(f"----- TIME ZONES PRIOR TO PYTHON 3.9 -----")
now = datetime.now()
print(f"{now.isoformat()=}")
utc_now = datetime.now(tz=timezone.utc)
print(f"{utc_now.isoformat()=}")

# TIME ZONES IN PYTHON 3.9
# - Use zoneinfo.ZoneInfo to access your computer’s time zone database
# - Can specify time zones by name
# - Has hundreds of time zones
# - Handles zone name changes during daylight savings time

from zoneinfo import ZoneInfo

print(f"----- TIME ZONES IN PYTHON 3.9 -----")
oslo_now = datetime.now(tz=ZoneInfo("Europe/Oslo"))
print(f"{oslo_now.isoformat()=}")

dt_with_tz = datetime(2020, 1, 1, 0, 0, tzinfo=ZoneInfo("America/Los_Angeles"))
print(f"{dt_with_tz.isoformat()=}")

dt_after_6_months = dt_with_tz + timedelta(days=30*6)
print(f"{dt_after_6_months.isoformat()=}")

dt_with_tz_changed = dt_with_tz.astimezone(ZoneInfo("Asia/Singapore"))
print(f"{dt_with_tz_changed.isoformat()=}")





