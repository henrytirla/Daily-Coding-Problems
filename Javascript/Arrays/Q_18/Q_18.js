function countC(str) {
    let count =0;

    for (let char in str){
        if (char ==="c" || char === "C"){
            count++;
        }

    }
    return count
}

console.log(countC('character'))