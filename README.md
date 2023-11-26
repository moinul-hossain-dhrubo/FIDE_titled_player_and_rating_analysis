# FIDE_Ratings_Analysis

### Problem Statement:
The objective of this project was to compile information on Grandmasters, International Masters, and Candidate Masters who presently hold ratings with FIDE and also actively compete in tournaments. To do that we needed information from [this website](https://ratings.fide.com/) . <br/>

After the data was processed, we ended up with 4996 records and 9 columns containing the following information: Name, Title, Country, Standard rating, Rapid rating, and Blitz rating; also we had their Age and Birth Year.
After that, Tableau, an excellent visualization tool/software, was utilized to analyze the data and extract useful information. We built three dashborads using the plots mentioned below:

1. Countries with most GM,IM and CM - Country map
2. Age distribution of the players along with the countries - Histogram
3. Emerging Players - Bar plot
4. Linear combination of the ratings - Scatter plot
5. Profiles of the Candidates tournament qualifiers etc. Note that, only the winner of this tournament will face the reigning world champion in the world championship matches.

Some interesting findings are :
1. The majority of the titled players are found in Europe.
   
   ![player_count_by_country](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/93bd445d-e1bb-44fa-80d8-58e9212e0e52)
   
2. There is a linear correlation between a player's standard, rapid, and blitz ratings; this means that a player with a higher standard time format rating is likely to have a higher rapid and blitz rating as well. Keep in mind that there are three different time formats: standard(longest time format), rapid(faster than standard) and blitz(fastest). [know more about time formats](https://chessarmory.com/blogs/chess-blog/time-controls-in-tournament-chess)
   
   ![linear_correlation_of_ratings](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/0b901a08-77cc-44f7-93d6-e8b97943cfb7)
   
5. The majority of German players are in the older age group, whereas the majority of Indian players are in the lower age bracket. The Spanish players are distributed fairly throughout the 20–60 age range.
   
   ![age_distribution](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/79ecba7e-5812-4bf8-85df-b3d7066b6f7f)
   
7. While players born after 2000 have already attained Grandmaster title, several players born before 1940 are still active and have not yet attained the status of GM or IM.
   
   ![birth_year](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/1fa18c25-bae2-4c63-bb3c-d20c5e3fd6ec)
   
9. Of the young stars, only one player is a Grandmaster.
    
    ![Mishra age](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/d214f6c5-7a5e-4b0a-81b5-47d2eecdcb0a)
   
11. Russia still holds the record of having the most Grandmasters, despite the fact that Germany has the most titled players and International masters. Additionally, Spain has the most Candidate masters.
    
    ![title_count_by_countries_marked](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/assets/122023969/8a9a54f7-9bd2-4b5b-9617-9adb566ebddb)

### **You can visit the dashboard [here](https://public.tableau.com/app/profile/moinul.hossain.dhrubo/viz/FIDEratingsAnalysis/Agedistribution) . <br/>**

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
   or,
   ```bash
   python -m venv venv
   ./venv/Scripts/activate
   ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Download Chromedriver from [here](https://chromedriver.chromium.org/downloads) <br/>
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
   python web_scraping_FIDE/scrape.py --chromedriver_path <path_to_chromedriver>
   ```
5. Within 20 seconds,Interact with the website to filter them similarly after the browser opens.
   You can change the time by updating
   ```bash
   time.sleep(your desired time)
   ```
6. The data will be stored in a csv file named 'active_candidate_masters.csv'. Change the name at your wish.
7. You can concatenate the csv files into a single csv file using jupyter notebook as I did [here](https://github.com/moinul-hossain-dhrubo/FIDE_Ratings_Analysis/blob/main/data/fide_active_players_2023.csv) . <br/>
