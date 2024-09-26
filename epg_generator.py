import datetime
import gzip

def generate_epg():
    # Get the current date
    today = datetime.datetime.now().strftime('%Y%m%d')

    # URL for the channel logo
    channel_logo_url = "https://example.com/clubbertv-logo.png [example.com]"  # Replace with your logo URL

    # Generate the repeating EPG for 7 days
    epg_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<tv>
  <channel id="clubberTV">
    <display-name>Clubber TV</display-name>
    <icon src="{channel_logo_url}" />
  </channel>
    """

    start_time = datetime.datetime.now()
    for day in range(7):
        for hour in range(0, 24, 2):
            start = start_time + datetime.timedelta(days=day, hours=hour)
            end = start + datetime.timedelta(hours=2)

            epg_template += f"""
  <programme start="{start.strftime('%Y%m%d%H%M%S')} +0000" stop="{end.strftime('%Y%m%d%H%M%S')} +0000" channel="clubberTV">
    <title>Clubber TV</title>
    <desc>GAA Action</desc>
    <category>Sports</category>
  </programme>
            """

    epg_template += "</tv>"

    # Write the XML file
    xml_filename = f'epg_{today}.xml'
    with open(xml_filename, 'w') as file:
        file.write(epg_template)

    # Compress the XML file into a .gz file
    gz_filename = f'epg_{today}.xml.gz'
    with open(xml_filename, 'rb') as f_in:
        with gzip.open(gz_filename, 'wb') as f_out:
            f_out.writelines(f_in)

    print(f"EPG XML generated: {xml_filename}")
    print(f"EPG XML compressed to: {gz_filename}")

if __name__ == '__main__':
    generate_epg()
