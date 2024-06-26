import { Song } from "./Song.js";

class Search{
    private static instance: Search;

    private db: Song[];
    
    private constructor(){
        this.db = this.get_db();
    }

    public getInstance(): Search{
        if (Search.instance == null){Search.instance=new Search()}
        return Search.instance;
    }

    public get_db(): Song[]{
        // gettting song db

        return [];
    }

    public search(userinput: string, result_cap: number = 5): Song[]{
        // searching database as a stream
        // db a mapping of the songs with the titel 
        // searching with the author and the title just some 
        // simple pattern matching 
        
        let result = this.db.filter(item => (item.getArtist() + " " + item.getName()).includes(userinput));
        return result.slice(0, result_cap);
    
    }  
}

