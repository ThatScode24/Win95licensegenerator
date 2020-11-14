const author = 'miha_focsa';

let licenses = 0;

let genFirstNumber = () => {
    let number = Math.floor((Math.random() * 366 ) + 1);

    if(number <= 9) {
        number = `0${number}`;
    }
    if(number <= 99) {
        number = `0${number}`;
    }

    return number;
}
let genSecondNumber = () => {
    let number = Math.floor((Math.random() * 92 ) + 3);
    
    if(number <= 9) {
        number = `00${number}`;
    } else {
        number = `0${number}`;
    }

   return number;
}
let trial = () => {
    
    let year = genFirstNumber();
    let day = genSecondNumber();
    let d0 = 0;
    let d6 = Math.floor(Math.random() * 9 );
	let d7 = Math.floor(Math.random() * 9 );
	let d8 = Math.floor(Math.random() * 9 );
	let d9 = Math.floor(Math.random() * 9 );
	let d10 = Math.floor(Math.random() * 9 );
	let d11 = Math.floor(Math.random() * 9 );
    
    
    let d12 = Math.floor(Math.random() * 9 );
    let d13 = Math.floor(Math.random() * 9 );
    let d14 = Math.floor(Math.random() * 9 );
    let d15 = Math.floor(Math.random() * 9 );
    let d16 = Math.floor(Math.random() * 9 );
    
    let z = `${d0}${d6}${d7}${d8}${d9}${d10}${d11}`;

    if(z % 7 == 0) {
        console.log(`${year}${day}-OEM-${d0}${d6}${d7}${d8}${d9}${d10}${d11}-${d12}${d13}${d14}${d15}${d16}`);
        licenses++;
    }
}

let wantedLicenses = window.prompt(`Program made by ${author}. How many licenses do you want? : `);

while(wantedLicenses != licenses) {
    trial();
}


