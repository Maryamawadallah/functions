import re

def get_home_price(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__Price--value'}).text
    except:
        x = None
    return x

def get_beds_num(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__Stats--beds text-nowrap'}).text.replace(' beds', '').replace(' bed', '')
    except:
        x = None
    return x

def get_baths_num(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__Stats--baths text-nowrap'}).text.replace(' baths', '').replace(' bath', '')
    except:
        x = None
    return x

def get_area_value(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__LockedStat--value'}).text
    except:
        x = None
    return x

def get_area_label(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__LockedStat--label'}).text
    except:
        x = None
    return x

def get_home_address(container):
    try:
        x = container.find('div', {'class': 'bp-Homecard__Address flex align-center color-text-primary font-body-xsmall-compact'}).text
    except:
        x = None
    return x

def get_listing_by(container):
    try:
        x = container.find('div', {'class': 'bp-Homecard__Attribution inline-flex flex-grow flex-wrap color-text-secondary font-body-xsmall-compact'}).text.replace('Listing by ', '')
    except:
        x = None
    return x

def get_listing_id(container):
    try:
        x = container['data-listing-id']  # Adjust this based on actual HTML attribute
    except:
        x = None
    return x

def get_mls_id(container):
    try:
        x = container['data-mls-id']  # Adjust this based on actual HTML attribute
    except:
        x = None
    return x

def get_unit_number(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__UnitNumber'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_location_name(container):
    try:
        x = container.find('div', {'class': 'bp-Homecard__LocationName'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_description(container):
    try:
        x = container.find('div', {'class': 'bp-Homecard__Description'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_price_per_sqft(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__PricePerSqFt'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_latitude(container):
    try:
        x = container['data-latitude']  # Adjust this based on actual HTML attribute
    except:
        x = None
    return x

def get_longitude(container):
    try:
        x = container['data-longitude']  # Adjust this based on actual HTML attribute
    except:
        x = None
    return x

def get_hoa_fee(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__HOAFee'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_mls_status(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__MLSStatus'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_date_sold(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__DateSold'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_time_listed(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__TimeListed'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_number_of_photos(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__NumberOfPhotos'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_virtual_tour_link(container):
    try:
        x = container.find('a', {'class': 'bp-Homecard__VirtualTour'})['href']  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_agent_name(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__AgentName'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_agent_phone(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__AgentPhone'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_broker_phone(container):
    try:
        x = container.find('span', {'class': 'bp-Homecard__BrokerPhone'}).text  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def get_property_url(container):
    try:
        x = container.find('a', {'class': 'bp-Homecard__Link'})['href']  # Adjust this based on actual HTML structure
    except:
        x = None
    return x

def parse_address(address):
    if not address:
        return None, None, None
    match = re.compile(r'^(.*?)(?:,\s*(.*?)(?:,\s*NY\s+(\d{5}))?)?$').match(address)
    
    if match:
        street = match.group(1).strip()
        neighborhood = match.group(2).strip() if match.group(2) else ""
        zip_code = match.group(3).strip() if match.group(3) else ""
        
        return street, neighborhood, zip_code
    else:
        return None, None, None
