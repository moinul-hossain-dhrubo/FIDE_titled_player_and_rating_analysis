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
1. The majority of the titled players are found in Europe.
   ![player_count_by_country](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/b5da80bc-e9ee-4701-ba16-62dee0443968)
3. There is a linear correlation between a player's standard, rapid, and blitz ratings; this means that a player with a higher standard time format rating is likely to have a higher rapid and blitz rating as well. Keep in mind that there are three different time formats: standard, rapid and blitz.
4. The majority of German players are in the older age group, whereas the majority of Indian players are in the lower age bracket.
5. While players born after 2000 have already attained Grandmaster title, several players born before 1940 are still active and have not yet attained the status of GM or IM.
6. Of the young stars, only one player is a Grandmaster.
7. Russia still holds the record of having the most Grandmasters, despite the fact that Germany has the most titled players.

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
