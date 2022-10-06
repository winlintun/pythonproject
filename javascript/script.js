"use strict"
// document.getElementById("demo").innerHTML = "My First JavaScript";

// function change(){
// 	document.getElementById("demo").innerHTML = "hello";
// }


// // Using document.write() after an HTML document is loaded, will delete all existing HTML:

// function writeIt() {
// 	document.write(5+6);
// }

// function callAlert(){
// 	window.alert(5+6);
// }


// // Statement

// let x,y,z;

// x = 5;
// y = 6;
// z = x + y ;

// console.log(z);


// document.getElementById("he").innerHTML = 
// "Hello Dolly";


// let $ = "Hello Wolrd";
// let $$ = 2;
// let $myMoney = 5;

// console.log($, $$, $myMoney);


// // Data tyupes
// let lengths = 16; // number
// let lastName = "Johnson"; // string
// let ob = { // Object
// 	firstName:"John", 
// 	_lastName:"Doe"
// };


// console.log(typeof(lengths));
// console.log(typeof(lastName));
// console.log(typeof(ob));
// console.log(lastName.length);

// console.log(ob);

// let str = "Apple, Banana, Kiwi";
// let part = str.slice(7, 13)
// console.log(part);
// let part1 = str.substring(7, 13);
// console.log(part1);
// let part2 = str.substr(7, 6);
// console.log(part2);

// // replace
// let text = "Please visit Microsoft!";
// let newText = text.replace("Microsoft", "W3School");
// console.log(newText);

// // CONVERTING
// let text1 = "Hello World!";
// let text2 = text1.toUpperCase();
// let text3 = text2.toLowerCase();

// console.log(text2, text3);

// let text4 = text1.concat(" ", text2);
// console.log(text4);

// let text5 = "     Hello ICEFACE!";
// console.log(text5.trim());

// console.log(text5.split(" "));

// let str1 = "Please locate where `locate` occurs!";
// console.log(str1.indexOf("locate"));

// console.log(str1.lastIndexOf("locate"));
// console.log(str1.search("locate"));
// console.log(str1.includes("where"));
// console.log(str1.startsWith("P"));

// // Object method

// let person = {
// 	firstN: "John",
// 	lastN: "Doe",
// 	sayH() {
// 		console.log("Say HHHH");
// 	},
// 	getFullName: function () {
// 		return this.firstN + " " + this.lastN;
// 	},
// };

// person.greet = function () {
// 	console.log("Hello! Greeting!");
// }


// function sayhi() {
// 	console.log("say hi!");
// }

// person.greet();

// person.sayhi = sayhi;

// person.sayhi();

// person.sayH();

// console.log(person.getFullName());


// function Person(firstName, lastName) {
// 	console.log(new.target);

// 	this.firstName = firstName;
// 	this.lastName = lastName;

// 	// this.getFullN = function () {
// 	// 	return this.firstName + " " + this.lastName;
// 	// };
// }

// let p1 = new Person("John", "Doeeeee");

// //console.log(p1.getFullN());

// let pp = {'name': "John"};

// //console.log(pp);

// Person.prototype.getFullN = function () {
// 	return this.firstName + " " + this.lastName;
// }

// let p2 = new Person("John", "DOa");
// let p3 = new Person("Jane", "Doa");

// console.log(p2.getFullN());
// console.log(p3.getFullN());


// Classes in ES6

// class Person {
// 	constructor(firstName, lastName) {
// 		this.firstName = firstName;
// 		this.lastName = lastName;
// 	}
// 	getFullName() {
// 		return this.firstName+ " " + this.lastName;
// 	}
// }


// let p1 = new Person("John", "Doe");
// let p2 = new Person("Jane", "Doe");

// console.log(p1.getFullName());
// console.log(p2.getFullName());

// let counter = {
// 	cout : 0,
// 	next: function () {
// 		return ++this.cout;
// 	},
// };

// console.log(counter.next());
// console.log(counter.next());
// console.log(counter.next());
// console.log(counter.next());
// console.log(counter.next());

// // Global context

// console.log(this == window);

// this.color = "Red";

// console.log(window.color);


// function show() {
// 	console.log(this == undefined);

// 	function dispaly() {
// 		console.log(this == undefined);
// 	}
// 	dispaly();
// }

// show();
// window.show();

// // Method Invocation

// let car = {
// 	brand: "Honda",
// 	getBrand : function () {
// 		return this.brand;
// 	}
// }

// console.log(car.getBrand());

// // let brand = car.getBrand();
// let brand = car.getBrand.bind(car);

// console.log(brand());

// let bike = {
// 	brand: "Harlay Davidsion"
// }

// let brandd = car.getBrand.bind(bike);
// console.log(brandd());

// // constructor invocation

// function Car(brande) {
// 	//if(!(this instanceof Car)) {
// 	if(! new.target) {
// 		throw Error("Must use the new operator to call the function");
// 	}
// 	this.brande = brande;
// }

// Car.prototype.getBrand = function() {
// 	return this.brand;
// };

// let carr = new Car('Honda');
// console.log(carr.getBrand());


// var bmw = Car("BMW")
// console.log(bmw.brande);

// 4 Indirect Invocation

// function getBrand(prefix) {
// 	console.log(prefix + this.brand);
// }

// let honda = {
// 	brand : "Honda"
// };

// let audi = {
// 	brand : "Audi"
// };

// getBrand.call(honda, "It's a ");
// getBrand.call(audi, "It's a ");

// // Arrow function

// let getThis = () => this;

// console.log(getThis() == window);

// function Car() {
// 	this.speed = 120;
// }

// Car.prototype.getSpeed = () => {
// 	return this.speed;
// }

// var car = new Car();
// console.log(car.getSpeed());

// Global This

// const canFetch = typeof globalThis.fetch == "function";

// console.log(canFetch);

// Object Property types

// 1 Dat properties

// let person = {
// 	firstName : "John",
// 	lastName: "Doe"
// };

// let p1 = {};
// p1.age = 25;
// console.log(p1.age);

// delete p1.age;
// console.log('after delete.',p1.age);

// Object.defineProperty(p1, "ssn", {
// 	configurable: false, // can't delete
// 	value: "012-38-9119"
// });

// console.log(p1.ssn);
// delete p1.ssn;

// p1.age = 25;
// p1.ssn = "012-38-9119"

// // for (let property in p1) {
// // 	console.log(property);
// // }

// Object.defineProperty(p1, 'ssn', {
//     enumerable: false
// });
// for (let prop in p1) {
// 	console.log(prop);
// }

// // 2 Accessor properties

// Object.defineProperty(person, "fullName", {
// 	get: function() {
// 		return this.firstName + " " + this.lastName;
// 	},
// 	set: function(value) {
// 		let parts = value.split(" ");
// 		if(parts.length == 2) {
// 			this.firstName = parts[0];
// 			this.lastName = parts[1];
// 		} else {
// 			throw "Invalid name format";
// 		}
// 	}
// });

// console.log(person.fullName);

// var product = {};

// Object.defineProperties(product, {
// 	name: {
// 		value: "Smartphone"
// 	}, 
// 	price: {
// 		value: 799
// 	}, 
// 	tax: {
// 		value: 0.1
// 	}, 
// 	netPrice: {
// 		get: function () {
// 			return this.price * (1 + this.tax);
// 		}
// 	}
// });

// console.log("The net price of a " + product.name + " is " + product.netPrice.toFixed(2) + " USD");

// for loop

// var person=  {
// 	firstName: "John",
// 	lastName: "Doe",
// 	ssn: "229-14-2351",
// 	age: 25
// };

// for(var prop in person) {
// 	console.log(prop + ": " + person[prop]);
// }

// const items = [10, 20, 30];

// let total = 0;

// for (const item in items) {
// 	total += items[item];
// }

// console.log(total);

// Array.prototype.foo = 100;

// for (const item in items) {
// 	console.log({item, value: items[item]});
// 	total += items[item];
// }

// console.log(total);

// for (let i=0; i<items.length; i++) {
// 	console.log(items[i]);
// }



// const employee = Object.create(person, {
// 	job: {
// 		value: "JS Developer",
// 		enumerable: true
// 	}
// });

// console.log(employee.hasOwnProperty("job"));
// console.log(employee.hasOwnProperty("firstName"));
// console.log(employee.hasOwnProperty("lastName"));


// for (const key in person) {
// 	if (person.hasOwnProperty(key)) {
// 		const value = person[key];
// 		console.log(value);
// 	}
// }

// const profile = Object.values(person);
// console.log(profile);

// const kv = Object.entries(person);
// console.log(kv);

// let widget = {
// 	color: "red"
// };

// let cloneWidget = Object.assign({}, widget);

// console.log(cloneWidget);


// Factory function

// let person = {
// 	firstName: "John",
// 	lastName: "Doe",
// 	getfullName() {
// 		return this.firstName + " " + this.lastName;
// 	}, 
// }

// console.log(person.getfullName());


// function createPerson(firstName, lastName) {
// 	return {
// 		firstName: firstName,
// 		lastName: lastName,
// 		getfullName() {
// 			return firstName + " " + lastName;
// 		},
// 	};
// }

// let p1 = createPerson("John", "Doe");
// let p2 = createPerson("Jane", "Doe");

// console.log(p1.getfullName());
// console.log(p2.getfullName());


// var personActions = {
// 	getfullName() {
// 		return this.firstName + " " + this.lastName;
// 	},
// };

// function createP(firstName, lastName) {
// 	let p  = Object.create(personActions);
// 	p.firstName = firstName;
// 	p.lastName = lastName;
// 	return p ;
// }


// let pp = createP("Jhon", "Doe");
// let pp1 = createP("Jane", "Doe");

// console.log(pp.getfullName());
// console.log(pp1.getfullName());


// function getUser(id) {
// 	if(id<=0) {
// 		return null;
// 	}

// 	// get the user form database
// 	// and return null if id does not exit


// 	//if user was found, return the user
// 	return { 
// 		id: id,
// 		username: "admin",
// 		profile: {
// 			avatar: "/avatar.png",
// 			language: "English"
// 		}
// 	}
// }

// let user = getUser(1);
// let profile1 = user.profile;

// let user2 = getUser(2)
// let profile2 = user2 && user2.profile;


// console.log(user, profile1, user2, profile2);

// Class



// function Person(name) {
// 	this.name = name;
// }

// Person.prototype.getName = function () {
// 	return this.name;
// }

// var john = new Person("John Doe");
// console.log(john.getName());


// class Person {
// 	constructor(name) {
// 		this.name = name;
// 	}

// 	getName() {
// 		return this.name;
// 	}

// 	setName(newName) {
// 		newName = newName.trim();
// 		if(newName === "") {
// 			throw "The name cannot be empty";
// 		}
// 		this.name = newName;
// 	}
// }


// let obj = new Person("John Doe");
// console.log(obj.getName());
// console.log(typeof(Person));
// obj.setName("Win Lin Tun");
// console.log(obj.getName());

// // getter in object
// let meeting = {
// 	attendees : [],
// 	add(attendees) {
// 		console.log(`${attendees} joined the meeting.`);
// 		this.attendees.push(attendees);
// 		return this;
// 	}, 
// 	get latest() {
// 		let count = this.attendees.length;
// 		return count == 0 ? undefined : this.attendees[count - 1];
// 	}
// }

// meeting.add("John").add("Jane").add("Peter");

// console.log(`The latest attendees is ${meeting.latest}.`);

// Inheritance

// function Animal(legs) {
// 	this.legs = legs;
// }

// Animal.prototype.walk = function () {
// 	console.log("walking on " + this.legs + " legs");
// }

// function Bird(legs) {
// 	Animal.call(this, legs);
// }

// Bird.prototype = Object.create(Animal.prototype);
// Bird.prototype.constructor = Animal;



// Bird.prototype.fly = function () {
// 	console.log("Flying");
// }

// var pigeon = new Bird(2);

// pigeon.walk();
// pigeon.fly();


// class Animal {
// 	constructor(legs) {
// 		this.legs = legs;
// 	}
// 	walk() {
// 		console.log("walking on " + this.legs + " legs");
// 	}
// 	static helloWorld() {
// 		console.log("Hello Wrold");
// 	}
// }

// class Bird extends Animal {
// 	constructor(legs, color) {
// 		super(legs);
// 		this.color = color;
// 	}

// 	fly() {
// 		console.log("Flying");
// 	}

// 	getColor() {
// 		return this.color;
// 	}
// }


// let bird = new Bird(2, "white");

// bird.walk();
// bird.fly();

// console.log(bird.getColor());

// Bird.helloWorld();

// Queue

class Queue extends Array {
	enqueue(e) {
		super.push(e);
	}
	dequeue() {
		return super.shift();
	}

	peek() {
		return !this.empty() ? this[0] : undefined;
	}
	empty() {
		return this.length == 0;
	}
}



var customers = new Queue();
customers.enqueue("A");
customers.enqueue("B");
customers.enqueue("C");

while(!customers.empty()) {
	console.log(customers.dequeue());
}