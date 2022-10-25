/**
 Given two strings s and t, return true if t is an anagram of s,
 and false otherwise.

 An Anagram is a word or phrase formed by
 rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

 Example 1:

 Input: s = "anagram", t = "nagaram"
 Output: true
 Example 2:

 Input: s = "rat", t = "car"
 Output: false


 Constraints:

 1 <= s.length, t.length <= 5 * 104
 s and t consist of lowercase English letters.


 Follow up: What if the inputs contain Unicode characters?
 How would you adapt your solution to such a case?

 **/

function checkAnagram(s,t){
    if (s.length != t.length){
        return false
    }
    var countS = new Map();
    var countT = new Map();

    for (i=0; i< s.length;i++){

        if(countS.size != 0 && countS.has(s[i])){

            countS = countS.set(s[i],1+ countS.get(s[i]));

        }
        else{
            countS = countS.set(s[i],1);}

        if( countT.size != 0 && countT.has(t[i])){
            countT = countT.set(t[i],1+ countT.get(t[i]));
        }else{

            countT = countT.set(t[i],1);}
    }
     // console.log("S",countS)
     // console.log("T",countT)
    for (const key of countS.keys()){
        if (countS.get(key) != countT.get(key) ){
            return  false
        }
     }
    return  true


}
s ="anagram"

t="nagaran"

console.log(checkAnagram(s,t))


