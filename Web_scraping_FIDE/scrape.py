from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--chromedriver_path', type = str, help = "Check the chromedriver path in your local machine")
arg = parser.parse_args()

###Columns to Scrape
columns = ['Name', 'Title','NaN', 'Country', 'Standard Rating', 'Rapid Rating', 'Blitz Rating', 'Birth Year']



def main():
    url = "https://ratings.fide.com/"
    webdriver_path = arg.chromedriver_path
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Click on the "Advanced Search" button
    advanced_search_button = driver.find_element(By.ID, "advanced_search")
    advanced_search_button.click()

    time.sleep(20) #Interact with the website by this time

    #Clicking on search button
    search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'search2')))

    search_button.click()

    time.sleep(5)

    # Defining the number of times you want to click the "50 More" button
    num_clicks = 1391//50  # You can adjust this number based on your requirements

    for _ in range(num_clicks): 
        # Click on the " 50 More" button
        more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'more')))
        more_button.click()

        # Wait for the updated content to load (adjust as needed)
        driver.implicitly_wait(20)



    # Wait for the updated content to load (adjust as needed)
    driver.implicitly_wait(10)
    time.sleep(5)




    # List to store dictionaries for each row
    data = []

    for row_index in range(1, 10):
        row_values = []
        for col_index in range(1, 9):  # As there are 8 columns (adjust the range accordingly)
            # Use f-string to dynamically insert row_index and col_index into the XPath
            td_element = driver.find_element(By.XPATH, f"(//tr[{row_index}]/td[{col_index}])")
            row_values.append(td_element.text)
        
        # Create a dictionary for the current row
        result_dict = dict(zip(columns, row_values))

        # Append the dictionary to the data list
        data.append(result_dict)

        # Print the dictionary for the current row (uncomment if needed)
        # print(result_dict)

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Replace the first name in the DataFrame
    df.at[0, 'Name'] = 'Aaditya Dhingra'

    # Drop the 'NaN' column
    df = df.drop('NaN', axis=1)


    df.to_csv('Active Candidate Masters.csv', index = False)


    # time.sleep(5)
    # driver.close()

    return


if __name__ == "__main__":
    main()
