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