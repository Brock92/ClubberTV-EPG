import gzip
import datetime

# Function to generate the EPG data
def generate_epg():
    now = datetime.datetime.now()
    end_date = now + datetime.timedelta(days=7)
    epg = """<?xml version="1.0" encoding="UTF-8"?>
<tv>
  <channel id="ClubberTV.ie">
    <display-name>Clubber TV</display-name>
    <desc>Local GAA action</desc>
  </channel>
"""
    current_time = now
    while current_time < end_date:
        start_time = current_time.strftime("%Y%m%d%H%M%S %z")
        end_time = (current_time + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S %z")
        epg += f"""
  <programme start="{start_time}" stop="{end_time}" channel="ClubberTV.ie">
    <title>Clubber TV</title>
    <desc>Local GAA action</desc>
  </programme>
"""
        current_time += datetime.timedelta(hours=2)

    epg += "</tv>"
    return epg

# Write to Clubber_tv.xml
with open("Clubber_tv.xml", "w") as xml_file:
    xml_file.write(generate_epg())

# Compress and write to Clubber_tv.xml.gz
with open("Clubber_tv.xml", "rb") as xml_file:
    with gzip.open("Clubber_tv.xml.gz", "wb") as gz_file:
        gz_file.writelines(xml_file)
