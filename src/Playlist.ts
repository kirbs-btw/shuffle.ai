import {Song} from '../src/Song.js';

class Playlist{
    private songs: Song[];
    private magic: number;

    public addSong(song: Song){
        this.songs.push(song);
    }

    public removeSong(song: Song){
         this.songs = this.songs.filter(item => item != song);
    }
    public getMagic(): number{
        return this.magic;
    }

    // saving the songs

    // load playlist 
}
