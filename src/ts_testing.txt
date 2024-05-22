// justing working myself in typescript
// to write the backend i need to understand ts

// static type
let name:string = "brian";
// console.log(name);

// type shifting
let something: unknown = "this is a string";
something = 5;
// console.log(something);

// arrays 
const ids: number[] = [
    5, 6, 7, 132, 41
];

// loops 
for (let index: number = 0; index < ids.length; index++) {
    const element: number = ids[index];
    // console.log(element);
}

// objects
const car: {name: string, price: number} = {name: "Car", price: 15};

// casting 

let couldbenumcouldbestr: unknown = 5;
let theString: string = couldbenumcouldbestr as string;

// console.log(theString);

// classes

class TheCar {
    name: string;
    price: number;
    serialNum: string;

    public constructor(name: string, num: number){
        this.name = name;
        this.price = num;
        this.serialNum = "AFES32131DSS";
    }

    public getNum(): string {
        return this.serialNum;
    }
}

const a3audi = new TheCar("A3", 20_000);
console.log(a3audi.getNum());

// interface 
interface Shape {
    getArea: () => number;
}

class Rect implements Shape{
    public constructor(protected readonly width: number, protected readonly height: number){}

    public getArea(): number{
        return this.width * this.height;
    }
}
