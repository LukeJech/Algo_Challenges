// Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

// Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

// Input range : 1 <= n < 4000

// In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

// Examples
// to roman:
// 2000 -> "MM"
// 1666 -> "MDCLXVI"
// 1000 -> "M"
//  400 -> "CD"
//   90 -> "XC"
//   40 -> "XL"
//    1 -> "I"

// from roman:
// "MM"      -> 2000
// "MDCLXVI" -> 1666
// "M"       -> 1000
// "CD"      -> 400
// "XC"      -> 90
// "XL"      -> 40
// "I"       -> 1
// Help
// Symbol	Value
// I	1
// IV	4
// V	5
// X	10
// L	50
// C	100
// D	500
// M	1000

class RomanNumerals {
    static roman_values = {
        M:1000,
        D:500,
        C:100,
        L:50,
        X:10,
        V:5,
        IV:4,
        I:1,
        
    }
    static toRoman(num) {
        // start with a new string
        let roman_num = ''
        // cast num as string loop through each digit 
        
        num = String(num)
        for(let i = num.length - 1; i >= 0; i--) {
            if(num[i] == 0) {continue}
            if(i == 0) {
                roman_num = 'M'.repeat(num[i]) + roman_num
            } else if (i == 1) {
                if(num[i] == 9) {
                    roman_num = 'CM'+ roman_num
                }
            } else if (i == 2) {
                if(num[i] == 9) {
                    roman_num = 'XC'+ roman_num
                }
            }
        }

        //  assign a value to that digit in roman numerals and add it to string
      return roman_num;
    }
  
    static fromRoman(str) {
      return 4;
    }
  }

    console.log(RomanNumerals.toRoman(1990))