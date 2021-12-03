/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    hmap=new Object()

    for(let i=0;i<nums.length;i++){
        
        if(nums[i] in hmap==false){
            hmap[target-nums[i]]=i
        }
        else{
            return [hmap[nums[i]],i]
        }
    }
};