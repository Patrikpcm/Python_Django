const data = new Date();

console.log(data.toString()); //converte a data para uma string

console.log(data.getDate()); //recupera o dia do mês 
console.log(data.getMonth()); //recupera o mes (de 0 - 11)
console.log(data.getFullYear()); //recupera o ano
let d = data.getDate();
let m = data.getMonth()+1;
let a = data.getFullYear();
console.log(`data: ${d}/${m}/${a}`);

console.log("\n");

let h = data.getHours();
let min = data.getMinutes();
let s = data.getSeconds();
console.log(`hora: ${h}:${min}:${a}`);

console.log("\n");

console.log(data.setDate(data.getDate()+10)); //setar a data - dia
console.log(data.setMonth(data.getMonth()+1)); //setar a data - mês
console.log(data.setYear(data.getFullYear() + 10)); //setar data - ano
//ele atualiza as viradas de calendário automáticamente 
console.log(data.toString()); //verifique a data modificada

//essa mesma lógica funciona pra horas, minutos e segundos