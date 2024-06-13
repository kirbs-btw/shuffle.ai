import {Song} from '../src/Song.js';

class Playlist{
    private songs: Song[];
    private magic: number;

    public addSong(song: Song){
        this.songs.push(song);
    }

    public removeSong(song: Song){
        // remove song from Songs
    }

    public getMagic(): number{
        return this.magic;
    }

    // saving the songs

    // vector a

    // add method

    // delete method
}