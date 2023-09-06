// Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

// Examples:

// * 'abc' =>  ['ab', 'c_']
// * 'abcdef' => ['ab', 'cd', 'ef']

function solution(str){
    let pairs = []
   for(let i = 0; i < str.length; i+=2){
        let this_pair = str[i]
        if(str[i+1]) {
            this_pair += str[i+1]
        } else {
            this_pair += '_'
        }
        pairs.push(this_pair)
   }
   return pairs
}


console.log(solution(""))