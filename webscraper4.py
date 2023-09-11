from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos'
page = requests.get(url)
"""
Using bs4 to take the html data from the page, locate the 'table' element
at the second position and find all elements with 'th' within the table,
excluding the last two before stripping them of white space.
"""
soup = BeautifulSoup(page.text, features='html.parser')
table = soup.find_all('table')[1]
world_titles = table.find_all('th')[:-2]
world_table_titles = [title.text.strip() for title in world_titles]

"""
Create a dataframe where the columns are the world_table_titles and
locate all elements of 'tr' within the table to assign them to column_data.
"""

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:-1]:
    """
    Retrieve all data from the rows excluding the last row and strip them
    of unnecessary white space before placing them into the dataframe.
    """
    row_data = row.find_all('td')[:-1]
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
print(df)

"""
Save the dataframe to a csv file.
"""
df.to_csv('most_viewed_yt_vids.csv', index = False)