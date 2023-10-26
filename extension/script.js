

const btn = document.getElementById("summarize")
btn.addEventListener("click",function(){
    btn.disabled = true;
    btn.innerHTML = "Summarising";
    chrome.tabs.query({currentWindow: true, active: true},function(tabs){
        
    });
});