// Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

// Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.


const cakes = (recipe, ingredients) => {
    // create a maxamount variable
    let maxBaked = Infinity
    // loop through the recipe and check how much available ingredients there are
    // compare the available to how much the recipe needs
    for (item in recipe) {
        if(!ingredients[item]){return 0}
        this_ingredient_max = Math.floor(ingredients[item]/recipe[item])
        maxBaked = this_ingredient_max < maxBaked ? this_ingredient_max : maxBaked 
        // update the max amount we can bake if it's less than the previous
    }
    return(maxBaked)
}
// Examples:

// // must return 2
console.log(cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}))
// // must return 0
console.log(cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}))