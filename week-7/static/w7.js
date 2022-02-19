var input = document.getElementById("search_name");

input.addEventListener("keypress", function(event) {
    if (event.key === 'Enter') {
        connction()
      }
  }); 

function searchName(){
    connction()
};


function connction(){
    let search_name = document.getElementById("search_name").value;
    let url = '/api/members?username='+search_name;
    fetch(url).then(function(response) {return response.json()}).then(function(ele){
        if(ele['data']) { 
            document.getElementById("search_result").innerHTML = ele['data']['name'];
        } 
        else { 
            document.getElementById("search_result").innerHTML = "Not Found"
        }
    })   
};


var form = document.getElementById('form');
form.addEventListener('submit', function(event){
    event.preventDefault();
    let newName= document.getElementById('change_name').value
    let submitResult = document.getElementById('submitResult')
    let inputname_id = document.getElementById('inputname_id')

    if (newName === ''){ 
        submitResult.innerHTML = '輸入的值為空白'
        document.getElementById('change_name').value = ''
    }
    else{    
        fetch("/apiResult",{
        'method':'POST',
        body:JSON.stringify({"name":newName}),
        headers:{
            "Content-Type":"application/json; charset=UTF-8",
            'Accept': 'application/json'
        }
        })
        .then(function(response){
            return response.json();
            })
        .catch(error => console.error('Error:', error))
        .then(function(result){
            document.getElementById('change_name').value = ''
            submitResult.innerHTML='更新成功'
            inputname_id.innerHTML=`${newName}，歡迎登入系統`
        });
    }
})