const BestSeat= require('./Q_21')


test('BestSeat',()=>{
    let seat= [1, 0, 1, 0, 0, 0, 1]
    expect(BestSeat(seat)).toEqual(4)
});