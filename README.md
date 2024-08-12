# Real Estate Scraper

This project demonstrates a web scraping tool designed to extract real estate data from Redfin.

## Features

- Scrapes property prices, number of beds and baths, area and address details.
- Handles pagination to retrieve multiple pages of results.
- Includes error handling for network requests.

## Project Structure

```
.
├── main.ipynb  # Jupyter notebook containing the main scraping logic
├── functions.py  # Helper functions for extracting data from HTML
├── data/
│ └── homes.csv # Sample output of the scraped data
├── README.md  # Project documentation
└── requirements.txt  # List of Python dependencies
```

## Getting Started

### Prerequisites

- `requests`
- `beautifulsoup4`
- `pandas`

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the Jupyter notebook `main.ipynb` to start the web scraping process. The results will be stored in a CSV file.

### Functions

The helper functions are defined in `functions.py`:

- `get_home_price(container)`: Extracts the home price from a container.
- `get_beds_num(container)`: Extracts the number of bedrooms.
- `get_baths_num(container)`: Extracts the number of bathrooms.
- `get_area_value(container)`: Extracts the area value.
- `get_area_label(container)`: Extracts the area label.
- `get_home_address(container)`: Extracts the full address of the property.
- `parse_address(container)`: Parses the address into street, neighborhood and zip code.
- `get_listing_by(container)`: Extracts the listing agent or company.

### Output

The scraped data includes the following fields:

- **price**: The price of the property.
- **beds**: The number of bedrooms.
- **baths**: The number of bathrooms.
- **area_value**: The size of the property in square feet or meters.
- **area_label**: The unit of the area measurement.
- **street**: The street address of the property.
- **neighborhood**: The neighborhood of the property.
- **zip_code**: The zip code of the property location.
- **listing_by**: The agent or company listing the property.

### Example Output

```json
{
    "price": "$500,000",
    "beds": "3",
    "baths": "2",
    "area_value": "1500",
    "area_label": "sqft",
    "street": "123 Main St",
    "neighborhood": "Downtown",
    "zip_code": "10001",
    "listing_by": "Real Estate Co."
}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
