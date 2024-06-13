
export class Song{
    private name: string;
    private artist: string;
    private duration: number;
    private vector: number[];


    constructor(name:string, artist:string, duration:number){
        this.name = name;
        this.artist = artist;
        this.duration = duration;
    }

    public getName():string {
        return this.name;
    }   

    public getArtist():string {
        return this.artist;
    }

    public getDuration():number {
        return this.duration;
    }

    public getVector():number[] {
        return this.vector;
    }
}

