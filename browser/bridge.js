let DEBUG = false;
let targeturl;
if(DEBUG){
    targeturl ="http://127.0.0.1:8000/compile";
}else{
    targeturl ="https://weblish.onrender.com/compile";
}

function get_url_extension( url ) {
    return url.split(/[#?]/)[0].split('.').pop().trim();
}
async function execute(content) {
    let weblishtext=encodeURIComponent(content);
    try{
        let response = await fetch(targeturl+"/?script="+weblishtext);
        if (!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        else{
            console.log("Request successful");
        }
        let outputcode = await response.text();
        try{
        eval(outputcode);
        }catch(error){
            alert(error);
        }
    }
    catch(error){
        console.error("Fetch error: ",error);
    }   
}
async function extract() {
    let weblish = document.querySelectorAll("script");
    for(let one of weblish){
        if(one.type=="text/english"){
            if(one.textContent){               
                execute(one.textContent.trim());
            }
            else if (get_url_extension(one.src)=="wbh"){
                let content = null;
                try{
                content = fetch(one.src);
                text_content=await content.text();
                execute(text_content.trim());
                }
                catch(error){
                    console.error("Cannot load src:",error);
                }
            }
        }
    }
}
if (typeof window != "undefined"){
    window.addEventListener("DOMContentLoaded",extract);
}else{console.log("Use a browser");}
