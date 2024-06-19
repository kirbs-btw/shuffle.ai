import { Song } from "./Song.js";

class Search{
    private db: Song[];
    
    constructor(){
        this.db = this.get_db();
    }

    public get_db(): Song[]{
        return [];
    }


    public search(userinput: string): Song[]{
        // searching database as a stream
        // db a mapping of the songs with the titel 
        // searching with the author and the title just some 
        // simple pattern matching 
        
        let result = this.db.filter(item => (item.getArtist() + " " + item.getName()).includes(userinput));
        return result;
    
    }  
}

