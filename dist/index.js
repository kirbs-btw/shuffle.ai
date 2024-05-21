// justing working myself in typescript
// to write the backend i need to understand ts
// static type
let name = "brian";
// console.log(name);
// type shifting
let something = "this is a string";
something = 5;
// console.log(something);
// arrays 
const ids = [
    5, 6, 7, 132, 41
];
// loops 
for (let index = 0; index < ids.length; index++) {
    const element = ids[index];
    // console.log(element);
}
// objects
const car = { name: "Car", price: 15 };
// casting 
let couldbenumcouldbestr = 5;
let theString = couldbenumcouldbestr;
// console.log(theString);
// classes
class TheCar {
    constructor(name, num) {
        this.name = name;
        this.price = num;
        this.serialNum = "AFES32131DSS";
    }
    getNum() {
        return this.serialNum;
    }
}
const a3audi = new TheCar("A3", 20000);
console.log(a3audi.getNum());
class Rect {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    getArea() {
        return this.width * this.height;
    }
}
console.log("ffs" > "23");
export {};
//# sourceMappingURL=index.js.map