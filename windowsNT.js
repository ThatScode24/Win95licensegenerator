const author = 'miha_focsa';

let licenses = 0;

let genThreeDigitNumber = () => {
    number = Math.floor((Math.random() * 999 ) + 100);

    if(number <= 1000) {
        return number;
    } else {
        return false;
    }
}
let trial = () => {
    let d1 = genThreeDigitNumber();
    
    if(d1 == false) {
        genThreeDigitNumber();
    } else{
        d2 =  Math.floor(Math.random() * 9 );
        d3 =  Math.floor(Math.random() * 9 );
        d4 =  Math.floor(Math.random() * 9 );
        d5 =  Math.floor(Math.random() * 9 );
        d6 =  Math.floor(Math.random() * 9 );
        d7 =  Math.floor(Math.random() * 9 );
        d8 =  Math.floor(Math.random() * 9 );
        
        let z = `${d2}${d3}${d4}${d5}${d6}${d7}${d8}`;

        if(z % 7 == 0) {
            if(d1 != 999 || d1 != 888 || d1 != 777 || d1 != 666 || d1 != 555 || d1 != 444 || d1 != 333 || d1 != 222 || d1 != 111) {
                if(d8 != 9 || d8 != 8 || d8 != 0) {
                    console.log(`${d1}-${d2}${d3}${d4}${d5}${d6}${d7}${d8}`);
                    licenses++;
                }
                else{
                    foundlicense = false;
                }
            }
            else{
                foundlicense = false;
            }
        }
        else{
            foundlicense = false;
        }
    }
}


let wantedLicenses = window.prompt(`Program made by ${author}. How many licenses do you want? : `);

while(wantedLicenses != licenses) {
    trial();
}
