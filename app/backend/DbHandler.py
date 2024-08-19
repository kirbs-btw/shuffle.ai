import pandas as pd
import os
# just doint some quick api with a df as a database to test the architecture

class DbHandler:
    def __init__(self, rel_data_path = "song_data.csv"):
        abs_data_path = os.path.join(os.path.dirname(__file__), rel_data_path)
        self.df = pd.read_csv(abs_data_path)
    
    def getDataFromIdList(self, id_list):        
        return self.df[self.df['track_id'].isin(id_list)]

    def searchInput(self, search_input:str) -> pd.DataFrame:
        # searching for trackname 
        base_df = self.df[self.df['track_name'].str.contains(search_input, case=False, na=False)]
        base_df = base_df.sort_values(by='track_popularity')

        # search for complete input artist and title
        matching_rows_ar = self.df[self.df['track_artist'].str.contains(search_input, case=False, na=False)]
        matching_rows_ar = matching_rows_ar.sort_values(by='track_popularity')

        base_df.append(matching_rows_ar, ignore_index=True)

        words: list = self.__removeFiller(search_input.split())

        for word in words:
            matching_rows_tn_w = self.df[self.df['track_name'].str.contains(word, case=False, na=False)]
            matching_rows_tn_w = base_df.sort_values(by='track_popularity')
            matching_rows_ar_w = self.df[self.df['track_artist'].str.contains(word, case=False, na=False)]
            matching_rows_ar_w = matching_rows_ar.sort_values(by='track_popularity')

            matching_rows_df_combined = pd.concat([matching_rows_tn_w, matching_rows_ar_w], axis=0, ignore_index=True)

            base_df.append(matching_rows_df_combined, ignore_index=True)
        
        # maybe combine the querys to one big one to have faster search ?

        # ranking search results
        # contains  id, title, link, all other data from that db...
        
        # send ping to a other db api that count the searched times for tracking

        # remove the duplicates

        return base_df
    
    def __removeFiller(words: list):
        filter = ["to", "the", "a"]
        return [word for word in words if word not in filter]
         
# comments 