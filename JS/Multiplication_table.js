// Your task, is to create N×N multiplication table, of size provided in parameter.

// For example, when given size is 3:

// 1 2 3
// 2 4 6
// 3 6 9
// For the given example, the return value should be:

// [[1,2,3],[2,4,6],[3,6,9]]


multiplicationTable = function(size) {
    // insert code here
    // setup array to return
    return_array = []
    // create a for loop to go through the size
    // each loop needs to create an array that goes to size an increase each number by that increment
    for (let i = 1; i <= size; i++) {
        // second for loop to create each individual array
        this_array = []
        for (let j = 1; j <= size; j++) {
            this_array.push(i*j)
            
        }
        return_array.push(this_array)
    }
    return return_array
  }
  

console.log(multiplicationTable(4))