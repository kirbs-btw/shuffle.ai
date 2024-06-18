import { Song } from "./Song.js";

// executed with every typing in the keyboard from the searchbar
// one change
function search(userinput: string): Song[]{
    // searching database as a stream
    let result = db.filter(item => item.includes(userinput));
    return result;
}   
