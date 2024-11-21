import gzip
import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

def create_epg(output_file):
    # Define constants
    channel_id = "GAA"
    program_title = "Local GAA Matches"
    program_duration = datetime.timedelta(hours=2)
    days = 7

    # Create root element for the EPG
    tv = Element("tv")
    channel = SubElement(tv, "channel", id=channel_id)
    SubElement(channel, "display-name").text = "GAA Channel"

    # Generate programs for 7 days
    start_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    end_time = start_time + datetime.timedelta(days=days)

    while start_time < end_time:
        programme = SubElement(tv, "programme", start=start_time.strftime("%Y%m%d%H%M%S +0000"),
                               stop=(start_time + program_duration).strftime("%Y%m%d%H%M%S +0000"),
                               channel=channel_id)
        SubElement(programme, "title").text = program_title
        start_time += program_duration

    # Save XML data to a .gz file
    with gzip.open(output_file, "wb") as gz_file:
        tree = ElementTree(tv)
        tree.write(gz_file, encoding="utf-8", xml_declaration=True)

# Specify output file
output_file = "epg.xml.gz"
create_epg(output_file)

print(f"EPG file '{output_file}' created successfully.")
