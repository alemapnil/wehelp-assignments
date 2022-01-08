//要求一
// function calculate(min, max){
//     let total = 0
//     for (let i = min; i < max+1;i++){
//         total+=i

//     }
//     console.log(total)
// }
// calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
// calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

//要求二
// function avg(data){
//     let allpeople = data.count
//     if (allpeople === 0){
//         console.log(0);
//     }
//     else{    
//     let persons = data.employees
//     let total = 0
//     for (let person of persons){
//         total+= person['salary']
//     }
//     let ans =total/allpeople
//     console.log(ans)
// }}

// avg({
//     "count":3,
//     "employees":[
//     {
//     "name":"John",
//     "salary":30000
//     },
//     {
//     "name":"Bob",
//     "salary":60000
//     },
//     {
//     "name":"Jenny",
//     "salary":50000
//     }
//     ]
//     }); // 呼叫 avg 函式


//要求三
// function arrayEquals(a, b) {
//     return Array.isArray(a) &&
//         Array.isArray(b) &&
//         a.length === b.length &&
//         a.every((val, index) => val === b[index]);}

// function find_max(nums){
//     let max_arr =[];
//     for (let n of nums){
//         if(arrayEquals(max_arr, [])){max_arr.push(n)}
//         else{if (n > max_arr[0]){max_arr[0] = n}}
//     }
//     return max_arr[0]}

// function find_min(nums){
//     let min_arr =[];
//     for (let n of nums){
//         if(arrayEquals(min_arr, [])){min_arr.push(n)}
//         else{if (n < min_arr[0]){min_arr[0] = n}}
//     }
//     return min_arr[0]}

// function maxProduct(nums){
//     let big1 = find_max(nums)
//     let keys = nums.keys();
//     for (let x of keys) {
//         if (nums[x] === big1){
//             nums.splice(x,1);
//             {break;}
//         }
//     } //remove max int
//     let big2 = find_max(nums)
//     let big_mul = big1 * big2
//     nums.push(big1) //回復原狀
//     //
//     let small1 = find_min(nums)
//     let index = nums.keys();
//     for (let x of index) {
//         if (nums[x] === small1){
//             nums.splice(x,1);
//             {break;}
//         }
//     } //remove min int
//     let small2 = find_min(nums)
//     let small_mul = small1 * small2
//     nums.push(small1) //回復原狀

//     if (big_mul >= small_mul){console.log(big_mul);}
//     else{console.log(small_mul)}    
// }
// maxProduct([5, 20, 2, 6]) // 得到 120
// maxProduct([10, -20, 0, 3]) // 得到 30
// maxProduct([-1, 2]) // 得到 -2
// maxProduct([-1, 0, 2]) // 得到 0
// maxProduct([-1, -2, 0]) // 得到 2

//要求四
// function twoSum(nums, target){
//     for(let id in nums){
//         let index = parseInt(id,10)
//         let n = nums[index] 
//         let p = target - n 
//         let rest = nums.slice(index + 1)

//         if (rest.includes(p)){
//             let _i = index + 1 + rest.indexOf(p)
//             return ([index, _i])}        
//     }
// }
// let result=twoSum([2, 11, 7, 15], 9);
// console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


//要求五
// function maxZeros(nums){
//     let sum = nums.reduce((total,val)=>total + val);
//     let len =nums.length 
//     if (len === sum){console.log(0)}
//     else if(sum === 0){console.log(len)}
//     else{

//         let head = 0; tail = len - 1;
//         let one_i = []; //將1的索引值放入陣列
//         let keys = nums.keys();

//         for (let k of keys) {if (nums[k]===1){one_i.push(k)};}
        
//         let gap = [];
//         let index = one_i.keys();
//         for(let i of index){

//             if (i === 0){gap.push(one_i[i] - head)}
//             if (i === one_i.length - 1){
//                 let former = one_i[i - 1];
//                 if (one_i[i] - former -1 > gap[0]){gap[0] = one_i[i] - former - 1}
//                 if (tail - one_i[i] > gap[0]){gap[0] = tail- one_i[i]}}
//             else{
//                 let former = one_i[i - 1];
//                 if (one_i[i] - former -1 > gap[0]){gap[0] = one_i[i] - former - 1}}}
//         console.log(gap[0])}
// }
// maxZeros([0, 1, 0, 0]) //得到 2
// maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) //得到 4
// maxZeros([1, 1, 1, 1, 1]) //得到 0
// maxZeros([0, 0, 0, 1, 1]) //得到 3