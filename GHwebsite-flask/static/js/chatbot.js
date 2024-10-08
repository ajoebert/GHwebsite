const sendChatBtn = document.querySelector(".chat-input span");
const chatInput = document.querySelector(".chat-input input");
const chatBox = document.querySelector(".chatbox");
const chatbotToggler = document.querySelector(".chatbot-toggler");
const chatBot = document.querySelector(".chatbot");
const chatbotCloseButton = document.querySelector(".chatbot-close-btn");

let userMessage;

const createChatLi = (message , classname)=>{
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", classname);
    let chatContent = classname =="outgoing" ? `<p>${message}</p>`: `<span><ion-icon name="chatbubbles-outline"></ion-icon></span> <p>${message}</p>`

    chatLi.innerHTML = chatContent;
    return chatLi;
}

 chatbotToggler.addEventListener("click",()=>{
    chatBot.classList.toggle("active")
 })

 chatbotCloseButton.addEventListener("click",()=>{
    chatBot.classList.toggle("active")
 })

const generateResponse = (incomingChatLI)=>{
    const API_URL = "https://giaweb.gain-hub.com/chatbot/";
    const messageElement = incomingChatLI.querySelector("p");
    const requestOptions = {
        method: "POST",
        headers:{
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
             message: userMessage
        })
    }

    fetch(API_URL , requestOptions).then(res=> res.json()).then(data=>{
        console.log(data)
        messageElement.textContent = data.Chatbot
    }).catch((error)=>{
        messageElement.textContent = "Oops! Something went wrong. Please try again.";
        console.log(error)
    }).finally(()=> chatBox.scrollTo(0, chatBox.scrollHeight));
}

const handleChat = ()=>{
  userMessage = chatInput.value.trim();
  chatInput.value = "";
  if(!userMessage) return ;
  chatBox.appendChild(createChatLi(userMessage , "outgoing"));

  setTimeout(()=>{
    const incomingChatLI = createChatLi("thinking...", "incoming");
    chatBox.appendChild(incomingChatLI)
    generateResponse(incomingChatLI)
  },600)
}

const handleChat1 = (event)=>{
    if (event.key === 'Enter') {
        userMessage = chatInput.value.trim();
        chatInput.value = "";
        if(!userMessage) return ;
        chatBox.appendChild(createChatLi(userMessage , "outgoing"));
      
        setTimeout(()=>{
          const incomingChatLI = createChatLi("thinking...", "incoming");
          chatBox.appendChild(incomingChatLI)
          generateResponse(incomingChatLI)
        },600)
    }
  }

sendChatBtn.addEventListener("click",handleChat);

chatInput.addEventListener("keydown", handleChat1);
