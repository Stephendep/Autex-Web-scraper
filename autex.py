import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration and initialization
driver_path = 'chromedriver.exe'


# Initializing the Selenium driver with custom options (compatible with Selenium 4)
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')
# service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Maximize the browser window (optional)
driver.maximize_window()

base_url = 'https://www.autexacoustics.co.uk'

def wait_and_click(xpath, wait_time=10):
    """Wait for an element to be clickable and click it."""
    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()

def extract_links():
    """Extract all 'a' elements with href containing '/products/'."""
    # Ensure dropdown menu is visible
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='MuiStack-root css-wu34vq']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    time.sleep(2)  # Allow lazy-loaded links to render

    elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/products/')]")
    # print(f"Number of links found: {len(elements)}")  # Debugging output

    # Ensure no duplicates and avoid double appending base URL
    links = []
    for element in elements:
        href = element.get_attribute('href')
        # print(f"Found href: {href}")  # Debugging output
        if not href.startswith(base_url):
            href = f"{base_url}{href}"
        if href not in links:  # Avoid duplicates
            links.append(href)
    return links
 
try:
    # Open the URL
    driver.get(base_url)

    # Click the "Products" menu
    wait_and_click("//p[text()='Products']")

    # Click the "Wall" option
    wait_and_click("//h3[text()='Wall']")

    # Extract links for Wall
    wall_links = extract_links()

    # Click the "Ceiling" option
    wait_and_click("//h3[text()='Ceiling']")

    # Extract links for Ceiling
    ceiling_links = extract_links()

    # Click the "Screen" option
    wait_and_click("//h3[text()='Screen']")

    # Extract links for Screen
    screen_links = extract_links()

    # Combine links or handle them separately
    url = wall_links + ceiling_links + screen_links

    url = list(set(url))

except NoSuchElementException:
    print("Skipping...")


product_data = []

print(f"Scraping page")

# Wait for elements to load
driver.implicitly_wait(10)

# Loop through each URL
for link in url:

    driver.get(link)

    print('Extracting :', link)

    #extract product_image url and name 
    prod_name_url = []

    try:
        # Wait for and get the text from the element using the given XPath
        title_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/div[1]/h2'))
        )

        # Extract the text from the nested span elements within the h2 tag
        title_text = title_element.text.strip()

        # Wait for and get the description using the given XPath
        description_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/p'))
        )
        # Extract the text from the description element
        description_text = description_element.text.strip()
    
        img_name_url = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-1ixqe7c')]//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-vd28q6')]//img"))
        )
    
        for img in img_name_url:
            src = img.get_attribute('src')
            alt = img.get_attribute('alt')
            # print(f"Image Name: {alt}")

            # Append data if both name and URL are found
            if alt and src:
                prod_name_url.append({"name": alt, "url": src})

  
        label_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'MuiGrid-root') and contains(@class, 'MuiGrid-item') and contains(@class, 'MuiGrid-grid-xs-6') and contains(@class, 'MuiGrid-grid-xl-4') and contains(@class, 'css-am2yhu')]"))
        )
        value_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'MuiGrid-root') and contains(@class, 'MuiGrid-item') and contains(@class, 'MuiGrid-grid-xs-6') and contains(@class, 'MuiGrid-grid-xl-8') and contains(@class, 'css-1kauoex')]"))
        )

        specifications_data = {}
        for label, value in zip(label_elements, value_elements):
            try:
                # Attempt multiple methods to extract text
                label_text = (label.find_element(By.TAG_NAME, "p").text.strip() or 
                              label.get_attribute("aria-label") or 
                              label.get_attribute("title") or
                              driver.execute_script("return arguments[0].innerText;", label.find_element(By.TAG_NAME, "p"))).strip()

                value_text = (value.find_element(By.TAG_NAME, "p").text.strip() or
                              value.get_attribute("aria-label") or 
                              value.get_attribute("title") or 
                              driver.execute_script("return arguments[0].innerText;", value.find_element(By.TAG_NAME, "p"))).strip()        

                specifications_data[label_text] = value_text

            except NoSuchElementException:
                print("One of the elements was not found for this product. Skipping...")


    
        Features_benefits = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'MuiStack-root') and contains(@class, 'css-ghvmpm')]//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-127vnk0')]")
            )
        )
        features = [
            driver.execute_script("return arguments[0].innerText;", bullet).strip()
            for bullet in Features_benefits
        ]

    except TimeoutException:
    
        print("Timeout waiting for products to load. Moving to next step.")
        driver.quit()
        exit()


    try:
        # List to hold the extracted data
        product_variant = []

        # Sequentially check elements 3 to 8
        for i in range(3, 9):  # Loop from 3 to 8
            try:
                # Dynamic XPath for each container
                container_xpath = f"(//div[contains(@class, 'MuiStack-root') and contains(@class, 'css-1bpk2h0')])[{i}]"
                color_container = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, container_xpath))
                )

                # Extract container name
                try:
                    name_xpath = f"{container_xpath}//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1')]"
                    container_name_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, name_xpath))
                    )
                    container_name = container_name_element.text.strip()
                except Exception as e:
                    print(f"Error locating name for container {i}: {e}")
                    container_name = f"Unknown Container {i}"

                # Conditional handling for "Certifications" and "Categories"
                if container_name in [ "Certifications", "BIM content"]:
                    print(f"Skipping container {i} as it is '{container_name}.")
                    continue  # Skip this container and move to the next

                elif container_name == "Categories":
                    print(f"Processing 'Categories' in container {i}.")
                    try:
                        # Extract categories
                        Categories = WebDriverWait(driver, 20).until(
                            EC.presence_of_all_elements_located(
                                (By.XPATH, "//div[contains(@class, 'MuiStack-root') and contains(@class, 'css-ghvmpm')]//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-127vnk0')]")
                            )
                        )
                        Categories_list = [
                            driver.execute_script("return arguments[0].innerText;", bullet).strip()
                            for bullet in Categories
                        ]

                        # Add "Categories" data to product_variant
                        product_variant.append({"Categories": Categories_list})
                    except Exception as e:
                        print(f"Error processing 'Categories' in container {i}: {e}")
                    continue  # Move to the next container after processing "Categories"


                # Locate all color items within this container
                color_items = color_container.find_elements(By.XPATH, ".//div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-1wxaqej')]")

                # List to hold product images for this container
                product_images = []

                # Extract name and URL from each child
                for idx, item in enumerate(color_items):
                    try:
                        # Extract color name
                        name_element = WebDriverWait(item, 10).until(
                            EC.presence_of_element_located((By.XPATH, ".//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1')]"))
                        )
                        color_name = name_element.get_attribute('innerHTML')

                        # Extract image URL and transform it if needed
                        img_element = item.find_element(By.XPATH, ".//img")
                        raw_img_url = img_element.get_attribute('src')

                        # Transform the URL to match the desired format
                        transformed_img_url = raw_img_url.replace(
                            "https://www.autexacoustics.co.nz/_next/image?url=",
                            "https://cms.autexacoustics.co.nz/uk/wp-content/uploads/"
                        ).split("&")[0]

                        # Append to product images
                        product_images.append({
                            "name": color_name,
                            "url": transformed_img_url
                        })
                    except Exception as e:
                        print(f"Error extracting item {idx + 1} in container {i}: {e}")
                        continue

                # Add the container and its product images to the list
                product_variant.append({container_name : product_images })

            except TimeoutException:
                print(f"Container {i} not found within the timeout.")
                continue  # Proceed to the next container in the loop

    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    # List to store extracted document data
    tech_docs = []

    try:
        driver.get(link)

        # Wait for the Technical Documents button to appear
        menu_element = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//button[@id="technicalDocumentsButton" and contains(@class, "base-Button-root")]'))
        )

        # Scroll into view and click the button
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", menu_element)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="technicalDocumentsButton" and contains(@class, "base-Button-root")]')))
        driver.execute_script("arguments[0].click();", menu_element)

        # Wait for dynamic content to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'MuiStack-root') and contains(@class, 'css-1sb9fsf')]"))
        )

        # Extract all document elements
        document_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiStack-root') and contains(@class, 'css-1sb9fsf')]//div[contains(@class, 'css-919ryk')]")
        # print(f"Found {len(document_elements)} document elements.")

        for document in document_elements:
            try:
                # Extract document name (normalize spaces and remove line breaks)
                name_element = document.find_element(By.XPATH, ".//h3[@class='MuiTypography-root MuiTypography-h3 css-1jbom63']")
                name = " ".join(name_element.text.split()).strip()

                # Extract document URL
                link_element = document.find_element(By.XPATH, ".//div[contains(@class, 'MuiStack-root css-v2fnns')]//a[1]")
                url = link_element.get_attribute("href")

                # Append to list
                tech_docs.append({"name": name, "url": url})
            except Exception as e:
                print(f"Failed to extract a document: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        

    product_data.append({
        "Url": link,
        "Title": title_text,
        "Description": description_text,
        "product_images": prod_name_url,
        "Specifications": specifications_data,
        "Features and Benefits": features
        })

    product_data.append(product_variant)
    product_data.append({"Technical documents": tech_docs})



# print(json.dumps(product_data, indent=4))
# Save the extracted data to autex.json
with open("autex_data.json", "w") as file:
    json.dump(product_data, file, indent=4)

print("\nFinal extracted data saved to 'autex_data.json'")

driver.quit()
exit()







    