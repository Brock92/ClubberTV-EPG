import datetime

def generate_epg():
    # Get the current date
    today = datetime.datetime.now().strftime('%Y%m%d')

    # Generate the repeating EPG for 7 days
    epg_template = """
<?xml version="1.0" encoding="UTF-8"?>
<tv>
  <channel id="clubberTV">
    <display-name>Clubber TV</display-name>
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

    # Write to XML file
    filename = f'epg_{today}.xml'
    with open(filename, 'w') as file:
        file.write(epg_template)

    print(f"EPG generated: {filename}")

if __name__ == '__main__':
    generate_epg()
