# FIDE_Ratings_Analysis

### Problem Statement:
The objective of this project was to compile information on Grandmasters, International Masters, and Candidate Masters who presently hold ratings with FIDE and also actively compete in tournaments. To do that we needed information from [this website](https://ratings.fide.com/) . <br/>

After the data was processed, we ended up with 4996 records and 9 columns containing the following information: Name, Title, Country, Standard rating, Rapid rating, and Blitz rating; also we had their Age and Birth Year.
After that, Tableau, an excellent visualization tool/software, was utilized to analyze the data and extract useful information. We built three dashborads using the plots mentioned below:

1. Countries with most GM,IM and CM - Country map
2. Age distribution of the players along with the countries - Histogram
3. Emerging Players - Bar plot
4. Linear combination of the ratings - Scatter plot
5. Profiles of the Candidates tournament qualifiers etc.

Some interesting findings are :
1. Europe continent has most of the titled players
2. Players have linear correlation beteen standard, rapid and blitz rating meaning that a player who has higher rating in standard time format will most likely have higher rating in
   rapid and blitz section. Note that, standard, rapid and blitz are three different time formats.
3. India has the most players in the younger age bins whereas most German players are in older age group.
4. Some players who were born before 1940 are still playing and have not become a GM or IM yet whereas players born after 2000 have already become Grandmasters.
5. Only one player amongst the youngstars is a Grandmaster.
6. Though Germany has the highest titled players, Russia still holds the record of having the most Grandmasters.

You can visit the dashboard [here](https://public.tableau.com/app/profile/moinul.hossain.dhrubo/viz/FIDEratingsAnalysis/Agedistribution) . <br/>

### Build from sources :
1. Clone the repo
   ```bash
   git clone https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis.git
   ```
2. Initialize and activate virtual environment
   ```bash
   virtualenv --no-site-packages venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Download Chromedriver from [here](https://chromedriver.chromium.org/downloads) <br/>
4. Apply filter regarding your need and then see how many results are found.
5. Update num_clicks, range of row_index according to the number of results found.
   ```bash
   # Defining the number of times you want to click the "More" button
    num_clicks = number of results found//50
   ```
   ```bash
   for row_index in range(1, number of results found + 1):
   ```
7. Replace the first name manually
   ```bash
   # Replace the first name in the DataFrame
    df.at[0, 'Name'] = 'First name of the table'
   ```
4. Run the Scraper
   ```bash
   python Web_scraping_FIDE/scrape.py --chromedriver_path <path_to_chromedriver>
   ```
5. Within 20 seconds,Interact with the website to filter them similarly after the browser opens.
   You can change the time by updating
   ```bash
   time.sleep(your desired time)
   ```
6. The data will be stored in a csv file named 'Active Candidate Masters.csv'. Change the name at your wish.
7. You can concatenate the csv files into a single csv file using jupyter notebook as I did [here](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/blob/main/Web_scraping_FIDE/data_process.ipynb) . <br/>
