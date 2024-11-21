import gzip
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def generate_epg():
    # Root XML element
    tv = ET.Element("tv")
    tv.set("generator-info-name", "Clubber TV Dummy EPG")
    
    # Channel configuration
    channel_id = "GAA"
    channel_name = "Clubber TV"
    programme_title = "Local GAA Matches"
    
    # Add the channel to the EPG
    channel = ET.SubElement(tv, "channel", id=channel_id)
    display_name = ET.SubElement(channel, "display-name")
    display_name.text = channel_name

    # Start time for the schedule (current day at midnight)
    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(days=7)  # Generate for 7 days

    # Add programmes every 2 hours
    current_time = start_time
    while current_time < end_time:
        programme = ET.SubElement(tv, "programme", channel=channel_id)
        programme.set("start", current_time.strftime("%Y%m%d%H%M%S") + " +0000")
        programme.set("stop", (current_time + timedelta(hours=2)).strftime("%Y%m%d%H%M%S") + " +0000")
        
        # Add programme title
        title = ET.SubElement(programme, "title")
        title.text = programme_title
        
        # Move to the next programme slot
        current_time += timedelta(hours=2)

    # Save the EPG to XML and compressed formats
    # Save as Clubber_TV.xml
    tree = ET.ElementTree(tv)
    with open("Clubber_TV.xml", "wb") as xml_file:
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)

    # Save as Clubber_TV_dummy.xml.gz
    with gzip.open("Clubber_TV_dummy.xml.gz", "wt", encoding="utf-8") as gz_file:
        tree.write(gz_file, encoding="unicode")

# Run the function
if __name__ == "__main__":
    generate_epg()
