class DbHandler:
    def __init__(self):
        pass
    
    def search_input(self, search_input:str) -> list:
        results: dict = {
            "some spec how the dict will look idk"
        }
        # checking for sql inject
        search_lower: str = search_input.lower()

        # search for complete input artist and title
        query: str = "SELECT * FROM songs WHERE title LIKE '%{}%';".format(search_lower) # rank spot #0
        query: str = "SELECT * FROM songs WHERE artist LIKE '%{}%';".format(search_lower) # rank #1

        # search for parts of the input ignore middle words like ("to", "the", "a", ...)
        words: list = search_lower.split()
        for word in words:
            query: str = "SELECT * FROM songs WHERE title LIKE '%{}%';".format(word) # rank spot #2
            query: str = "SELECT * FROM songs WHERE artist LIKE '%{}%';".format(word) # rank #3        
            # results.append("query results")

        # maybe combine the querys to one big one to have faster search ?


        # ranking search results
        # contains  id, title, link, all other data from that db...
        
        return results   