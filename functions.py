def get_listing_id(container):
    try:
        return container['data-listing-id']
    except KeyError:
        return None

def get_mls_id(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Stats--mls-id'}).text
    except:
        return None

def get_unit_number(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Stats--unit'}).text
    except:
        return None

def get_location_name(container):
    try:
        return container.find('div', {'class': 'bp-Homecard__LocationName'}).text
    except:
        return None

def get_description(container):
    try:
        return container.find('div', {'class': 'bp-Homecard__Description'}).text
    except:
        return None

def get_price_per_sqft(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Price--per-square-foot'}).text
    except:
        return None

def get_latitude(container):
    try:
        return container['data-latitude']
    except KeyError:
        return None

def get_longitude(container):
    try:
        return container['data-longitude']
    except KeyError:
        return None

def get_hoa_fee(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__HOA--fee'}).text
    except:
        return None

def get_mls_status(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Status--mls'}).text
    except:
        return None

def get_date_sold(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__DateSold'}).text
    except:
        return None

def get_time_listed(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__TimeListed'}).text
    except:
        return None

def get_number_of_photos(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Photos--count'}).text
    except:
        return None

def get_virtual_tour_link(container):
    try:
        return container.find('a', {'class': 'bp-Homecard__VirtualTour'})['href']
    except (KeyError, TypeError):
        return None

def get_agent_name(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Agent--name'}).text
    except:
        return None

def get_agent_phone(container):
    try:
        return container.find('span', {'class': 'bp-Homecard__Agent--phone'}).text
    except:
        return None

def get_broker_phone(container): 
    try:
        return container.find('span', {'class': 'bp-Homecard__Broker--phone'}).text
    except:
        return None

def get_property_url(container):
    try:
        return container.find('a', {'class': 'bp-Homecard__Link'})['href']
    except (KeyError, TypeError):
        return None
