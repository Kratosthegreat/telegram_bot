async function send(){
 const u=document.getElementById('input').value;
 const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:u})});
 const d=await r.json();
 document.getElementById('output').innerText+="\nYou: "+u+"\nBot: "+d.reply;
}