import geoip2.database

def get_country(ip, reader_path='GeoLite2-Country.mmdb'):
    try:
        with geoip2.database.Reader(reader_path) as reader:
            response = reader.country(ip)
            return response.country.name
    except:
        return 'Unknown'
