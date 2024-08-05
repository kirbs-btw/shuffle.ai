import pandas as pd

# just doint some quick api with a df as a database to test the architecture

class DbHandler:
    def __init__(self, data_path = "api/song_data.csv"):
        self.df = pd.read_csv(data_path)
    
    def get_data_from_ids(self, data):
        id_list = [i["id"] for i in data["song_ids"]]        

        matching_rows = self.df[self.df['track_id'].isin(id_list)]

        print(matching_rows)
        # checking matching rows how they are structured to pars them later into the correct info that is needed by the 
        # front end still thinking about what is needed
        return matching_rows

    def __get_data_from_id(self):
        pass


    def search_input(self, search_input:str) -> list:
        results: dict = {
            "songs" : [
                
            ]
        }
        
        # searching for trackname 
        matching_rows = self.df[self.df['track_name'].str.contains(search_input, case=False, na=False)]
        matching_rows = matching_rows.sort_values(by='track_popularity')

        # still need to do the same for the rest... adding them together to resuslts and thinking of a structure to send 
        # the api response

        # search for complete input artist and title
        query: str = "SELECT * FROM songs WHERE title LIKE '%{}%';".format(search_lower) # rank spot #0
        query: str = "SELECT * FROM songs WHERE artist LIKE '%{}%';".format(search_lower) # rank #1
        results["songs"].append(self.__query_db(query))  

        # search for parts of the input ignore middle words like ("to", "the", "a", ...)
        words: list = search_lower.split()

        for word in words:
            query: str = "SELECT * FROM songs WHERE title LIKE '%{}%';".format(word) # rank spot #2
            query: str = "SELECT * FROM songs WHERE artist LIKE '%{}%';".format(word) # rank #3      
            results["songs"].append(self.__query_db(query))  


        # maybe combine the querys to one big one to have faster search ?

        # ranking search results
        # contains  id, title, link, all other data from that db...
        
        # send ping to a other db api that count the searched times for tracking

        return results   