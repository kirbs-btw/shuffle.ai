class Song{
    private name: string;
    private duration: number;
    private vector: number[];


    constructor(name:string, duration:number){
        this.name = name;
        this.duration = duration;
    }

    public getName(): string {
        return this.name;
    }   

    public getDuration(): number{
        return this.duration;
    }
}

