class DbHandler:
    def __init__(self):
        pass
    
    def search_input(self, search_input:str) -> list:
        # checking for sql inject
        
        # search for complete input artist and title
        query = "FROM songs SELECT * WHERE title == {search_input}"
        query = "FROM songs SELECT * WHERE artist == {search_input}"

        # search for parts of the input ignore middle words like ("to", "the", "a", ...)

        # ranking search results
        # contains  id, title, link, all other data from that db...
        results: dict
        return results 