var start = 0, end = 8;
var btn = document.getElementById("btn");
var url = 'https://alemapnil.github.io/wehelp-assignments/data/site.json';

function myFunction(photo_url, site_name){
    var main = document.getElementById('containter3_id');
    var _1div = document.createElement("div");
    _1div.className = "section";

    var _2div = document.createElement("div");
    _2div.className = "photo";
    var img = document.createElement('img');
    img.src = photo_url;
    _2div.appendChild(img);        

    var _3div = document.createElement("div");
    _3div.className = "word";

    var _4div = document.createElement("div");
    _4div.className ="overflow";
    var text = document.createTextNode(site_name);
    _4div.appendChild(text); 
    
    _3div.appendChild(_4div)
    _2div.appendChild(_3div)   
    _1div.appendChild(_2div)
    main.appendChild(_1div)}




fetch(url).then(function(response) {return response.json()}).then(function(result){
    let resulted = result.slice(start,end)
    start+=8; end+=8;

    //result is an Array
    for (let site of resulted){
        for (let s in site) {
            if (s==='file'){var photo_url = site[s]};
            if (s==='stitle'){var site_name = site[s]};}
          myFunction(photo_url, site_name); 
        }});

    
function catchJson(){

fetch(url).then(function(response) {return response.json()}).then(function(result){
    let resulted = result.slice(start,end)
    start+=8; end+=8;

    //result is an Array
    for (let site of resulted){
        for (let s in site) {
            if (s==='file'){var photo_url = site[s]};
            if (s==='stitle'){var site_name = site[s]};}
          myFunction(photo_url, site_name); 
        }});
    
    if (end >58 ){btn.style.display='none';}
        
}

