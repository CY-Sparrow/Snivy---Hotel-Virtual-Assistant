from flask import Flask, jsonify, render_template,request,session
from app import app
import app.flow as chatF
from app.models import add_complaint,add_bookIssue,add_Message, delete_data

@app.route('/')

def home():
    return render_template("index.html")

@app.route('/chat',methods=['POST','GET'])

def response():
    begin = chatF.start_node()
    return jsonify(begin)

@app.route('/click',methods=['POST','GET'])
def suggest():

    data = request.json
    next_node = data.get("nextNode")
    session["currentNode"] = next_node
    node = chatF.Flow[next_node]
 
    return jsonify({"message":node["message"],
                    "buttons":node["buttons"]})

@app.route('/back', methods=['POST'])
def go_back():
    data = request.json
    back_node = data.get("Back")
    if back_node not in chatF.Flow:
        return jsonify({"status": "fail", "message": "Invalid node"}), 400
    session["currentNode"] = back_node
    node = chatF.Flow[back_node]
    return jsonify({"message": node["message"], "buttons": node["buttons"]})


# When complaint is submitted
@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.json
    complaint_text = data.get("complaint")
    # Add complaint to database
    complaint_id = add_complaint(complaint_text)
    
    return jsonify({
        "status": "success",
        "message": "Your complaint has been logged",
        "complaint_id": complaint_id
    })


@app.route('/submit-book-issue', methods=['POST'])
def submit_book_issue():
    data = request.json
    complaint_text = data.get("bookIssue")
    # Add complaint to database
    bookIssue_id = add_bookIssue(complaint_text)
    
    return jsonify({
        "status": "success",
        "message": "Your booking issue has been logged",
        "bookIssue_id": bookIssue_id
    })



# When contact message is submitted
@app.route('/submit-message', methods=['POST'])
def submit_message():
    data = request.json
    message_text = data.get("message")
    # Add message to database
    message_id = add_Message(message_text)
    
    return jsonify({
        "status": "success",
        "message": "Your message has been sent",
        "message_id": message_id
    })

@app.route('/delete-sended-msg', methods=["POST"])
def delete_msg():
    data = request.json
    reference_no = data.get("deleteRef")
    if delete_data(reference_no) == True:
        return jsonify({
            "status": "success",
            "message": "Your details has been deleted successfully!"
        })
    else:
        return jsonify({
            "status": "fail",
            "message": "No matching Reference no found!"
        })


if __name__ == "__main__":
    app.run()
