
export class Song{
    private name: string;
    private artist: string;
    private duration: number;
    private link: string;
    private vector: number[];

    constructor(name:string, artist:string, duration:number, link:string){
        this.name = name;
        this.artist = artist;
        this.duration = duration;
        this.link = link; // on our site or just web idk

        this.initVector();
    }

    public initVector(): number[] {
        // getting the v with the db i guess
    
        return this.vector;
    }

    public getName(): string {
        return this.name;
    }   

    public getArtist(): string {
        return this.artist;
    }

    public getDuration(): number {
        return this.duration;
    }

    public setLink(newLink:string): void {
        // the link to the song can change
        this.link = newLink;
    }

    public getLink(): string {
        return this.link;
    }

    public getVector(): number[] {
        return this.vector;
    }
}

