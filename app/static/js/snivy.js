
 
    const state ={

        currentNode:"START",
        cancle:"BACK"
    }

    // Widget open/close toggle
    let isChatOpen = false;

    function toggleChat(){
        const chatwindow = document.getElementById("chatwindow");
        const toggleBtn = document.getElementById("chatToggleBtn");

        isChatOpen = !isChatOpen;

        if(isChatOpen){
            chatwindow.classList.add("chat-visible");
            toggleBtn.classList.add("hide");
        } else {
            chatwindow.classList.remove("chat-visible");
            toggleBtn.classList.remove("hide");
        }
    }

    function getCurrentNode(){
        return flow[state.currentNode]
    }

    var chatbox = document.getElementById("message");
    var chips = document.getElementById("suggest");
    var textf = document.getElementById("chat-input");

    function botBubble(message){

        var msg  = document.createElement("div");
        msg.innerHTML = message;
        msg.className = "bot-msg";
        chatbox.appendChild(msg);

        msg.scrollIntoView({behavior:"smooth"});
    }

    function userBubble(label){

        var msg  = document.createElement("div");
        msg.innerHTML = label;
        msg.className = "user-msg";
        chatbox.appendChild(msg);

        msg.scrollIntoView({behavior:"smooth"});

    }

    function textOutput(text){
        
        if (textf.value.trim() === "") return;
        
        var output = document.createElement("div")
        output.innerHTML = textf.value;
        output.className = "user-msg";
        chatbox.appendChild(output);

        if(textf.value==="/clear"){
            return start();
        }

        textf.value= "";

    }

    function handleKey(event){

        if(event.key==="Enter"){
            textOutput();
        }

    }

function showDeleteForm() {
    chips.innerHTML = "";
    document.getElementById("deleteForm").style.display = "block";
    // Auto-scroll to form
    document.getElementById("deleteForm").scrollIntoView({behavior: "smooth", block: "end"});
}

// Show complaint form
function showComplaintForm() {
    chips.innerHTML = "";
    document.getElementById("complaintForm").style.display = "block";
    // Auto-scroll to form
    document.getElementById("complaintForm").scrollIntoView({behavior: "smooth", block: "end"});
}

function showBookIssueForm() {
    chips.innerHTML = ""; 
    document.getElementById("bookIssueForm").style.display = "block";
    // Auto-scroll to form
    document.getElementById("bookIssueForm").scrollIntoView({behavior: "smooth", block: "end"});
}

// Show message form
function showMessageForm() {
    chips.innerHTML = "";
    document.getElementById("messageForm").style.display = "block";
    // Auto-scroll to form
    document.getElementById("messageForm").scrollIntoView({behavior: "smooth", block: "end"});
}

// Hide all forms
async function cancelForm() {
    
    chips.innerHTML="";
    document.getElementById("complaintForm").style.display = "none";
    document.getElementById("bookIssueForm").style.display = "none";
    document.getElementById("messageForm").style.display = "none";
    document.getElementById("deleteForm").style.display = "none";
    const node  = await fetch('/back',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(
            {Back:"BACK"}
        )
    });
    
    const response = await node.json();
    botBubble(response.message)
    suggest(response.buttons)// Show buttons again

}

// Submit complaint to database
async function submitComplaint() {
    const complaint = document.getElementById("complaintText").value;
    
    // Validate inputs
    if (!complaint) {
        alert("Please fill in all required fields");
        return;
    }
    
    try {
        const response = await fetch('/submit-complaint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                complaint: complaint
            })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            botBubble(`✅ Thank you! Your complaint has been logged.Reference <br><b>#${result.complaint_id}</b>`);
            // Clear form
            document.getElementById("complaintText").value = "";
            cancelForm();
        }
    } catch (error) {
        console.error('Error:', error);
        botBubble("❌ Error submitting complaint. Please try again.");
    }
}

async function submitBookIssue() {
    const bookIssue = document.getElementById("bookIssueText").value;
    
    // Validate inputs
    if (!bookIssue) {
        alert("Please fill in all required fields");
        return;
    }
    
    
    try {
        const response = await fetch('/submit-book-issue', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                bookIssue: bookIssue
            })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            botBubble(`✅ Thank you! Your book issue has been logged.Reference <br><b>#${result.bookIssue_id}</b>`);
            // Clear form
            document.getElementById("bookIssueText").value = "";
            cancelForm();
        }
    } catch (error) {
        console.error('Error:', error);
        botBubble("❌ Error submitting Booking Issue. Please try again.");
    }
}

// Submit message to database
async function submitMessage() {

    const message = document.getElementById("messageText").value;
    
    // Validate inputs
    if (!message) {
        alert("Please fill in all required fields");
        return;
    }
    
    try {
        const response = await fetch('/submit-message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message
            })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            botBubble(`✅ Thank you! Your message has been sent.Reference <br><b>#${result.message_id}</b>`);
            // Clear form
            document.getElementById("messageText").value = "";
            cancelForm();
        }
    } catch (error) {
        console.error('Error:', error);
        botBubble("❌ Error sending message. Please try again.");
    }
}

async function submitDelete() {
    const deleteRef = document.getElementById("deleteText").value;
    
    // Validate inputs
    if (!deleteRef) {
        alert("Please fill in all required fields");
        return;
    }
    
    try {
        const response = await fetch('/delete-sended-msg', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                deleteRef: deleteRef
            })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            botBubble(result.message);
            // Clear form
            document.getElementById("deleteText").value = "";
            cancelForm();
        }

        else {
            botBubble(result.message);  
            // Clear form
            document.getElementById("deleteText").value = "";
            cancelForm();
        }
    } catch (error) {
        console.error('Error:', error);
        botBubble("❌ Error submitting deletion request. Please try again.");
    }
}

async function getChat() {
    var startNode = await fetch('/chat')
    var node = await startNode.json()
    botBubble(node.message)
    suggest(node.buttons)
}

getChat()

async function handleChoice(label, nextNode) {
    
        userBubble(label);
        // Normal flow - fetch next node from server
        var response = await fetch('/click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nextNode: nextNode })
        });
        var node = await response.json();
        botBubble(node.message);
        suggest(node.buttons);
        

}

async function handleComplain(label, nextNode) {
   
    // Check if this is a complaint or message node
    if (nextNode === "complaint") {
        
        userBubble(label);
        
        // Fetch the message first, then show form
        var response = await fetch('/click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nextNode: nextNode })
        });
        var node = await response.json();
        
        botBubble(node.message);
        // Don't show buttons, just show the form
        showComplaintForm();
        return;
    }
    
    if (nextNode === "complaint_booking") {
        
        userBubble(label);
        
        
        // Fetch the message first, then show form
        var response = await fetch('/click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nextNode: nextNode })
        });
        var node = await response.json();
        botBubble(node.message);
        // Don't show buttons, just show the form
        showBookIssueForm();
        return;
    }

    if (nextNode === "contact_message") {
        
        userBubble(label);
        
        // Fetch the message first, then show form
        var response = await fetch('/click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nextNode: nextNode })
        });
        var node = await response.json();
        botBubble(node.message);
        // Don't show buttons, just show the form
        showMessageForm();
        return;
    }

    if (nextNode === "delete_request") {
        
        userBubble(label);
        
        // Fetch the message first, then show form
        var response = await fetch('/click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nextNode: nextNode })
        });
        var node = await response.json();
        botBubble(node.message);
        // Don't show buttons, just show the form
        showDeleteForm();
        return;
    }

}
   function suggest(buttons){
        
        chips.innerHTML = "";

        buttons.forEach(function(btns){
            var btn = document.createElement("Button");
            btn.innerHTML = btns.label;
            btn.className = "chip";
            
            if (btns.next === "complaint" || btns.next === "complaint_booking" || btns.next === "contact_message" || btns.next === "delete_request") {
                btn.onclick = function(){
                    handleComplain(btns.label, btns.next);
                }
            }
            else{
                btn.onclick = function(){
                    handleChoice(btns.label, btns.next);
                }
            }    
            chips.appendChild(btn);
        });
        
        // Auto-scroll to latest buttons
        document.getElementById("suggest").scrollIntoView({behavior: "smooth", block: "end"});
    }


    function start(){
        
        chatbox.innerHTML ="";
        chips.innerHTML = "";

        var startNode = flow["START"];
        botBubble(startNode.message)
        suggest(startNode.buttons)
        
        

        textf.value = "";
    }