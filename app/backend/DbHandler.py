import pandas as pd
import os

class DbHandler:
    def __init__(self, rel_data_path = "db/song_data.csv") -> None:
        abs_data_path = os.path.join(os.path.dirname(__file__), rel_data_path)
        self.df = pd.read_csv(abs_data_path)
    
    def getDataFromIdList(self, id_list) -> pd.DataFrame:        
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
            matching_rows_tn_w: pd.DataFrame = self.df[self.df['track_name'].str.contains(word, case=False, na=False)]
            matching_rows_tn_w: pd.DataFrame = base_df.sort_values(by='track_popularity')
            matching_rows_ar_w: pd.DataFrame = self.df[self.df['track_artist'].str.contains(word, case=False, na=False)]
            matching_rows_ar_w: pd.DataFrame = matching_rows_ar.sort_values(by='track_popularity')

            matching_rows_df_combined: pd.DataFrame = pd.concat([matching_rows_tn_w, matching_rows_ar_w], axis=0, ignore_index=True)

            base_df.append(matching_rows_df_combined, ignore_index=True)

        # ranking search results
        # contains  id, title, link, all other data from that db...

        # send ping to a other db api that count the searched times for tracking

        # remove the duplicates

        return base_df
    
    def __removeFiller(words: list) -> list:
        filter: list = ["to", "the", "a"]
        return [word for word in words if word not in filter]