const person = {name: "Dave", age: 40, hair: "blue"}
const result = Object.keys(person).map(x => x.toUpperCase())

console.log(result)