function solve(s) {
    // start max number at 0
    let max_num = 0
    // loop through the string
    for (let i = 0; i < s.length; i++) {
        // if index is a number, check the indexes to the right to see if there are more numbers

        if (Number(s[i])) {
            let this_num = Number(s[i])
            let j = 1

            while(Number(s[i + 1]) || Number(s[i + 1]) == 0){
                console.log(s[i + 1])
                this_num = Number(String(this_num) + String(s[i + 1]))
                
                i += 1
            }
            // check if new number is bigger than max number
            if(this_num > max_num) {max_num = this_num}
        }
        
    }
    // return max number
    return max_num;
  };

  console.log(solve('k285403efouljzrsexewxyxuncn92569vize'))