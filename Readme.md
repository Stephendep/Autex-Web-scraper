
---

# AUTEX PRODUCT SCRAPER DOCUMENTATION 

## Overview
This project automates the process of scraping product information from the [Autex Acoustics Website](https://www.autexacoustics.co.uk). The script extracts details such as product name, description, specifications, images features and benefits, variants (e.g., colours, textures, patterns), and associated technical documents. The extracted data is saved in JSON format for further use.

This scraper targets the following product categories:
- **Wall**
- **Ceiling**
- **Screen**

---

## Prerequisites
1. **Python**: Ensure Python (preferably Python 3.8 or newer) is installed.
2. **Chrome WebDriver**: This project uses Selenium, which requires a ChromeDriver compatible with your Chrome browser version. Download the appropriate version from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/).

## Installation

### Step 1: Set Up Virtual Environment
Create and activate a virtual environment to isolate dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 2: Install Required Packages
Use the provided `requirements.txt` to install dependencies.

```bash
pip install -r requirements.txt
```

The key library used are:
- `Selenium` for browser automation.

## Script Overview

### Core Features

1. ### **Category Filtering:**: 
- Navigates through Wall, Ceiling, and Screen categories.
2. ### **Product Data Extraction**: 
- **Name, URL, and Description**: Extracts product name, URL, and description details.
- **Product Images**: Captures all available image URLs.
- **Specifications**: Extracts details from the specifications table.
- **Features and Benefits**: Collects and formats feature bullet points.
- **Variants**: Scrapes variant details (e.g., colors, patterns) with names and image URLs.
3. ### **Technical Documents:**: 
- Gathers all downloadable document links, including their names and URLs.
4. ### **Pagination Support**:
- Automatically handles multiple pages of products within categories.
5. ### **Error Handling**:
- Skips products that fail to load or extract data, logging errors for review.

### Usage

The main scraping logic is implemented in `autex.py`.

To run the script:

```bash
python autex.py
```

Ensure `chromedriver.exe` is in the same directory or provide its path and you should use the latest chrome version.

## Output
The script saves data in `autex_data.json` in the following format:

```json

    {
        "Url": "https://www.autexacoustics.co.uk/products/composition",
        "Title": "Composition\u00ae",
        "Description": "Composition\u00ae is a durable and flexible acoustic wallcovering that is typically applied in vertical drops like wallpaper. It is easily maintained and retains its rich, solid colour and soft, velvety finish over time.",
        "product_images": [
            {
                "name": "A classroom with Composition\u00ae in Falling Water on the walls with artwork pinned to it",
                "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FComposition_Gallery_1-scaled.jpg&w=3840&q=75"
            },
            {
                "name": "An image of two breakout spaces in a classroom with Composition\u00ae in Myst and Lime",
                "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FComposition_Gallery_2-scaled.jpg&w=3840&q=75"
            },
            {
                "name": "A small classroom area with Composition\u00ae in Falling Water",
                "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FComposition_Gallery_3-scaled.jpg&w=3840&q=75"
            },
            {
                "name": "Two classroom areas with Composition\u00ae in Falling Water and Flatiron on the walls",
                "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FComposition_Gallery_4-scaled.jpg&w=3840&q=75"
            },
            {
                "name": "A classroom reading area with a custom Composition\u00ae design in Falling Water and Myst",
                "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FComposition_Gallery_5-scaled.jpg&w=3840&q=75"
            }
        ],
        "Specifications": {
            "Form:": "Roll",
            "NRC:": "0.40",
            "Composition:": "100% polyester fibre (PET)",
            "Fire rating:": "BS EN 13501-1:2018 B-s1, d0",
            "Size:": "1220 mm wide",
            "Thickness:": "8 mm - 10 mm",
            "Application:": "Wall",
            "Install method:": "Direct fix"
        },
        "Features and Benefits": [
            "Targets speech frequencies",
            "Improves speech intelligibility",
            "Pinnable, hook and loop receptive surface",
            "An alternative finish to paint",
            "Durable and easily maintained",
            "Floor to ceiling solution with no vertical joins",
            "Easy installation around windows and openings",
            "Customisable for limitless branding and design options through in-house cutting",
            "Carbon neutral",
            "Made locally",
            "Education",
            "Commercial/office spaces",
            "Retail",
            "To access DWG and Revit content files for this product, click below:"
        ]
    },
    [
        {
            "Colours": [
                {
                    "name": "Canyon",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Canyon.23.KL_.01.png"
                },
                {
                    "name": "Highland",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Highland.23.KL_.02.png"
                },
                {
                    "name": "Terrace",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Terrace.23.KL_.png"
                },
                {
                    "name": "Caspian",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Caspian.23.KL_.01.png"
                },
                {
                    "name": "Sargazo",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Sargazo.22.jpg"
                },
                {
                    "name": "Vintage",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Vintage.22.jpg"
                },
                {
                    "name": "Chilli Red",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Chilli-Red.22.jpg"
                },
                {
                    "name": "Blazing Red",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Blazing-Red.22.jpg"
                },
                {
                    "name": "Simba",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Simba.22.jpg"
                },
                {
                    "name": "Beehive",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Beehive.22.jpg"
                },
                {
                    "name": "Senado",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Senado.22.jpg"
                },
                {
                    "name": "Electric Blue",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Electric-Blue.22.jpg"
                },
                {
                    "name": "Octane",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Octane.22.jpg"
                },
                {
                    "name": "Muralla",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Muralla.22.jpg"
                },
                {
                    "name": "Ink",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Ink.22.jpg"
                },
                {
                    "name": "Calypso",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Calypso.22.jpg"
                },
                {
                    "name": "Stonewash",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Stonewash.22.jpg"
                },
                {
                    "name": "Atlantis",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Atlantis.22.jpg"
                },
                {
                    "name": "Falling Water",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Falling-Water.22.jpg"
                },
                {
                    "name": "Porcelain",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Porcelain.22.jpg"
                },
                {
                    "name": "Myst",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Myst.22.jpg"
                },
                {
                    "name": "Tree House",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Tree-House.22.jpg"
                },
                {
                    "name": "Gherkin",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Gherkin.22.jpg"
                },
                {
                    "name": "Jade",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Jade.22.jpg"
                },
                {
                    "name": "Lime",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Lime.22.jpg"
                },
                {
                    "name": "Acros",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Acros.22.jpg"
                },
                {
                    "name": "Granny Smith",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Granny-Smith.22.jpg"
                },
                {
                    "name": "Spearmint",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Spearmint.22.jpg"
                },
                {
                    "name": "Sage",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Sage.22.jpg"
                },
                {
                    "name": "Petronas",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Petronas.22.jpg"
                },
                {
                    "name": "Pinnacle",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Pinnacle.22.jpg"
                },
                {
                    "name": "Empire",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Empire.22.jpg"
                },
                {
                    "name": "Koala",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Koala.22.jpg"
                },
                {
                    "name": "Flatiron",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Flatiron.22.jpg"
                },
                {
                    "name": "Savoye",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Savoye.22.jpg"
                },
                {
                    "name": "Parthenon",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Parthenon.22.jpg"
                },
                {
                    "name": "Opera",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Opera.22.jpg"
                },
                {
                    "name": "Cavalier",
                    "url": "https://www.autexacoustics.co.uk/_next/image?url=https%3A%2F%2Fcms.autexacoustics.co.nz%2Fuk%2Fwp-content%2Fuploads%2Fsites%2F3%2F2022%2F08%2FAutex_Vertiface_Cavalier.22.jpg"
                }
            ]
        },
        {
            "Categories": [
                "Targets speech frequencies",
                "Improves speech intelligibility",
                "Pinnable, hook and loop receptive surface",
                "An alternative finish to paint",
                "Durable and easily maintained",
                "Floor to ceiling solution with no vertical joins",
                "Easy installation around windows and openings",
                "Customisable for limitless branding and design options through in-house cutting",
                "Carbon neutral",
                "Made locally",
                "Education",
                "Commercial/office spaces",
                "Retail",
                "To access DWG and Revit content files for this product, click below:"
            ]
        }
    ],
    {
        "Technical documents": [
            {
                "name": "Composition\u00ae Lookbook",
                "url": "https://cdn.mediavalet.com/aunsw/autex/L6bp-Z2PT0qJNU4Dms8kuw/9vN45caEd0uYWO9KfUV4kQ/Original/Composition%20Lookbook.pdf"
            },
            {
                "name": "Colour Guide",
                "url": "https://cdn.mediavalet.com/aunsw/autex/igziqBzlWUSUbFex8TWRRQ/124FevkjlE-hekO07VcWkQ/Original/UK_Colour%20Guide.pdf"
            },
            {
                "name": "RGB Vertiface Colour Match",
                "url": "https://cdn.mediavalet.com/aunsw/autex/3yM0sUq5fEacEuqKVoEggg/jnrXzDTi1k6ljh56HtHSCA/Original/RGB%20Vertiface%20Colour%20Match.pdf"
            },
            {
                "name": "Composition\u00ae Data Sheet",
                "url": "https://cdn.mediavalet.com/aunsw/autex/kZG51WA7xkOTJ7S1TcsUuA/qpIR7RNJVk2FQUWNRCAR4Q/Original/Composition%20DataSheet_UK.pdf"
            },
            {
                "name": "Material Safety Data Sheet",
                "url": "https://cdn.mediavalet.com/aunsw/autex/NqnovisJwU-6Q2RfwAHR4g/TPFWptb1g0GhpuKxO77-AQ/Original/Material%20Safety%20Datasheet.pdf"
            },
            {
                "name": "Composition\u00ae Install Instructions",
                "url": "https://cdn.mediavalet.com/aunsw/autex/f6NDGdBEzUmS4LkoncmLzg/KWK7hrthKECisKNt8yIReg/Original/Composition%20Install%20Instructions.pdf"
            },
            {
                "name": "Composition\u00ae Manufacturer's Guarantee",
                "url": "https://cdn.mediavalet.com/aunsw/autex/ddTrluFhG0SjlIVcq2x_cQ/7BI8I70LfE6W9FbgGtDUTQ/Original/Composition%20Manufacturers%20Guarantee%20UK.pdf"
            },
            {
                "name": "Care and Maintenance",
                "url": "https://cdn.mediavalet.com/aunsw/autex/YFEsHndTaEGtYHRoKswz3Q/6c4KqsMGHE6guLxfazrXjw/Original/Care%20and%20Maintenance.pdf"
            },
            {
                "name": "Highly Humid Environments",
                "url": "https://cdn.mediavalet.com/aunsw/autex/5ZjHnvOGNECjh0ESvOqtbw/5GlT4j4B90OMUb2YAYo6sg/Original/Highly%20Humid%20Environments.pdf"
            }
        ]
    }
```

## Notes
- **ChromeDriver Version**: Ensure ChromeDriver matches your Chrome browser version.
- **Error Handling**: The script includes basic error handling to skip over products that fail to load or extract data.
  
---
