import pandas as pd
import os
# just doint some quick api with a df as a database to test the architecture

class DbHandler:
    def __init__(self, rel_data_path = "song_data.csv"):
        
        abs_data_path = os.path.join(os.path.dirname(__file__), rel_data_path)
        print(abs_data_path)
        self.df = pd.read_csv(abs_data_path)
    
    def get_data_from_ids(self, id_list):        

        matching_rows = self.df[self.df['track_id'].isin(id_list)]
        # checking matching rows how they are structured to pars them later into the correct info that is needed by the 
        # front end still thinking about what is needed
        return matching_rows

    def search_input(self, search_input:str) -> list:
        # searching for trackname 
        matching_rows_tn = self.df[self.df['track_name'].str.contains(search_input, case=False, na=False)]
        matching_rows_tn = matching_rows_tn.sort_values(by='track_popularity')

        # search for complete input artist and title
        matching_rows_ar = self.df[self.df['track_artist'].str.contains(search_input, case=False, na=False)]
        matching_rows_ar = matching_rows_ar.sort_values(by='track_popularity')

        matching_rows_tn.append(matching_rows_ar, ignore_index=True)

        # search for parts of the input ignore middle words like ("to", "the", "a", ...)
        words: list = search_input.split()

        for word in words:
            matching_rows_tn_w = self.df[self.df['track_name'].str.contains(word, case=False, na=False)]
            matching_rows_tn_w = matching_rows_tn.sort_values(by='track_popularity')
            matching_rows_ar_w = self.df[self.df['track_artist'].str.contains(word, case=False, na=False)]
            matching_rows_ar_w = matching_rows_ar.sort_values(by='track_popularity')

            matching_rows_df_combined = pd.concat([matching_rows_tn_w, matching_rows_ar_w], axis=0, ignore_index=True)

            matching_rows_tn.append(matching_rows_df_combined, ignore_index=True)
        
        # maybe combine the querys to one big one to have faster search ?

        # ranking search results
        # contains  id, title, link, all other data from that db...
        
        # send ping to a other db api that count the searched times for tracking

        return matching_rows_tn