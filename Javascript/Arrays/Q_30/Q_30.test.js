const apartmentHunting= require('./Q_30');


test('apartmentHunting',()=>{
    blocks = [
        {
            "gym": false,
            "school": true,
            "store": false,
        },
        {
            "gym": true,
            "school": false,
            "store": false,
        },
        {
            "gym": true,
            "school": true,
            "store": false,
        },
        {
            "gym": false,
            "school": true,
            "store": false,
        },
        {
            "gym": false,
            "school": true,
            "store": true,
        },
    ]
    reqs = ["gym", "school", "store"]
    expect(apartmentHunting(blocks,reqs)).toEqual(3)
})