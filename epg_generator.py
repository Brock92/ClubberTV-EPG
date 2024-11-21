import gzip
import os
import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse

def load_existing_epg(file_path):
    """Load existing EPG data from a file, if available."""
    if not os.path.exists(file_path):
        return Element("tv")
    
    if file_path.endswith(".gz"):
        with gzip.open(file_path, "rb") as gz_file:
            tree = parse(gz_file)
    else:
        tree = parse(file_path)
    
    return tree.getroot()

def save_epg(root, output_file, compress=False):
    """Save the EPG data back to a file, optionally compressing it."""
    if compress:
        with gzip.open(output_file, "wb") as gz_file:
            tree = ElementTree(root)
            tree.write(gz_file, encoding="utf-8", xml_declaration=True)
    else:
        with open(output_file, "wb") as file:
            tree = ElementTree(root)
            tree.write(file, encoding="utf-8", xml_declaration=True)

def update_epg(dummy_file, plain_file):
    # Constants
    channel_id = "ClubberTV"
    program_title = "Local GAA Matches"
    program_duration = datetime.timedelta(hours=2)
    
    # Load existing EPG
    epg = load_existing_epg(dummy_file if os.path.exists(dummy_file) else plain_file)
    existing_programs = epg.findall(f"./programme[@channel='{channel_id}']")
    
    # Determine the start time for new programs
    if existing_programs:
        last_program = existing_programs[-1]
        start_time = datetime.datetime.strptime(last_program.get("stop").split()[0], "%Y%m%d%H%M%S")
    else:
        # If no programs exist, start from the current time
        start_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    
    # Add programs for one day
    end_time = start_time + datetime.timedelta(days=1)
    while start_time < end_time:
        programme = SubElement(epg, "programme", start=start_time.strftime("%Y%m%d%H%M%S +0000"),
                               stop=(start_time + program_duration).strftime("%Y%m%d%H%M%S +0000"),
                               channel=channel_id)
        SubElement(programme, "title").text = program_title
        start_time += program_duration

    # Save updated EPG to both files
    save_epg(epg, dummy_file, compress=True)
    save_epg(epg, plain_file, compress=False)
    print(f"EPG updated successfully in '{dummy_file}' and '{plain_file}'.")

# Specify the output files
dummy_file = "Clubber_TV_dummy.xml.gz"
plain_file = "Clubber_TV.xml"
update_epg(dummy_file, plain_file)
