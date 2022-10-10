/**This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17.''''\\'''''''
return true since 10 + 7 is 17 ***/
const { ethers } = require("ethers");

const provider = new ethers.providers.WebSocketProvider("wss://ws-nd-455-693-912.p2pify.com/ab870a782db1a62584325ff3edecb044");
//const toPCS = '0x10ED43C718714eb63d5aA57B78B54704E256024E';

async function mempool(){
    provider.on("pending", async(tx)=>{
        const txInfo = await provider.getTransaction(tx);
        try{
          console.log(ethers.utils.formatEther(txInfo.gasLimit))
            
        }
        catch{
            console.log("no data to show")
        }
        
    })
}

mempool()


