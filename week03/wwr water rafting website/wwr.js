document.querySelectorAll(".year").forEach(function(el){el.textContent=new Date().getFullYear();});
const form=document.getElementById("contactForm");
if(form){form.addEventListener("submit",function(e){e.preventDefault();document.getElementById("formMessage").textContent="Thanks! Your message has been received in this demo.";form.reset();});}
