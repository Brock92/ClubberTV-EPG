import gzip
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
# Function to create the EPG
def generate_epg():
    # Root element
    tv = ET.Element("tv")
    tv.set("generator-info-name", "Clubber TV Dummy EPG")
    # Define parameters
    channel_id = "GAA"
    channel_name = "Clubber TV"
    programme_title = "Local GAA Matches"
    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # Add channel
    channel = ET.SubElement(tv, "channel")
    channel.set("id", channel_id)
    display_name = ET.SubElement(channel, "display-name")
    display_name.text = channel_name
    # Add programmes for 7 days
    for day in range(7):
        for hour in range(0, 24, 2):  # Programmes are 2 hours long
            start = start_time + timedelta(days=day, hours=hour)
            end = start + timedelta(hours=2)
            # Add programme
            programme = ET.SubElement(tv, "programme")
            programme.set("start", start.strftime("%Y%m%d%H%M%S") + " +0000")
            programme.set("stop", end.strftime("%Y%m%d%H%M%S") + " +0000")
            programme.set("channel", channel_id)
            title = ET.SubElement(programme, "title")
            title.text = programme_title
    # Write to files
    tree = ET.ElementTree(tv)
    tree.write("Clubber_TV.xml", encoding="utf-8", xml_declaration=True)
    with gzip.open("Clubber_TV_dummy.xml.gz", "wt", encoding="utf-8") as gz_file:
        tree.write(gz_file, encoding="unicode")
# Run the function
if __name__ == "__main__":
    generate_epg()
