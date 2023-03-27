const arrayOf_products = require('./Q_18');



test('Array of Products',() =>{
    expect(arrayOf_products([5,1,4,2])).toEqual([ 8, 40, 10, 20 ]
    )
})

//npx jest test_file.jsls
