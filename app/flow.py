Flow = {

    "START": {
        "message":"Hello! Welcome to <strong>Grand Stay Hotel.</strong><br><br>I am Snivy, your <b>virtual assistant</b>. How can I help you today?",
        "buttons": [
            {"label": "Book a room",   "next": "book_menu"},
            {"label": "Our services",  "next": "services_menu"},
            {"label": "FAQs",          "next": "faq_menu"},
            {"label": "Complaints",    "next": "complaintX"},
            {"label": "Contact us",    "next": "contact_menu"},
        ]
    },

    # -- BOOKING --

    "book_menu": {
        "message": "Great! I can help you with your reservation.<br>What would you like to know?",
        "buttons": [
            {"label": "Check availability",     "next": "book_availability"},
            {"label": "Room types",             "next": "book_rooms"},
            {"label": "Pricing",                "next": "book_pricing"},
            {"label": "How to book",            "next": "book_process"},
            {"label": "I have a booking issue", "next": "complaint_booking"},
            {"label": "Back",                   "next": "BACK"},
        ]
    },

    "book_availability": {
        "message": "Our rooms are available year-round!<br>To check specific dates, visit our booking page or call the front desk.<br><br><b>Phone</b>: +91-XXXX-XXXXXX<br><b>Web</b>: grandstay.com/book",
        "buttons": [
            {"label": "See room types", "next": "book_rooms"},
            {"label": "See pricing",    "next": "book_pricing"},
            {"label": "Back",           "next": "book_menu"},
        ]
    },

    "book_rooms": {
        "message": "We offer three room categories:<br><br><strong>Standard Room</strong> - Cozy queen bed, city view, all essentials.<br><strong>Deluxe Room</strong> - King bed, garden or pool view, mini-bar.<br><strong>Suite</strong> - Living area, king bed, premium amenities, top-floor views.",
        "buttons": [
            {"label": "See pricing",  "next": "book_pricing"},
            {"label": "How to book",  "next": "book_process"},
            {"label": "Back",         "next": "book_menu"},
        ]
    },

    "book_pricing": {
        "message": "Current nightly rates:<br><br><strong>Standard Room</strong> - from Rs. 3,500/night<br><strong>Deluxe Room</strong> - from Rs. 5,500/night<br><strong>Suite</strong> - from Rs. 9,000/night<br><br>Prices may vary by season. Breakfast packages available.",
        "buttons": [
            {"label": "How to book",  "next": "book_process"},
            {"label": "Back",         "next": "book_menu"},
        ]
    },

    "book_process": {
        "message": "Booking is simple!<br><br>1. Visit <strong>grandstay.com/book</strong><br>2. Choose your dates and room type<br>3. Enter your details and confirm<br>4. You will receive a confirmation email instantly.<br><br>Our team is available 24/7 to help.",
        "buttons": [
            {"label": "I have a booking issue", "next": "complaint_booking"},
            {"label": "Back",                   "next": "book_menu"},
        ]
    },

    # -- SERVICES --

    "services_menu": {
        "message": "We offer a range of <b>premium services</b>. What are you interested in?",
        "buttons": [
            {"label": "Airport pickup",   "next": "svc_airport"},
            {"label": "Dining",           "next": "svc_dining"},
            {"label": "Spa and Wellness", "next": "svc_spa"},
            {"label": "Parking",          "next": "svc_parking"},
            {"label": "Laundry",          "next": "svc_laundry"},
            {"label": "Pool and Gym",     "next": "svc_pool"},
            {"label": "Back",             "next": "BACK"},
        ]
    },

    "svc_airport": {
        "message": "Yes! We provide <strong>airport pickup and drop-off</strong> service.<br><br>Sedan - Rs. 800 one way<br>SUV - Rs. 1,200 one way<br><br>Please inform us at least <b>3 hours in advance</b>. Book via front desk or email.",
        "buttons": [
            {"label": "Contact front desk", "next": "contact_menu"},
            {"label": "More services",      "next": "services_menu"},
            {"label": "Back",               "next": "BACK"},
        ]
    },

    "svc_dining": {
        "message": "<strong>The Grand Table</strong> - our in-house restaurant:<br><br><b>Breakfast</b>: 7 AM - 10:30 AM<br><b>Lunch</b>: 12:30 PM - 3 PM<br><b>Dinner</b>: 7 PM - 10:30 PM<br><br>Room service available <b>24/7</b>. We offer Indian, Continental and Chinese cuisines.",
        "buttons": [
            {"label": "Room service menu", "next": "svc_roomservice"},
            {"label": "More services",     "next": "services_menu"},
            {"label": "Back",              "next": "BACK"},
        ]
    },

    "svc_roomservice": {
        "message": "Our <b>24/7 room service</b> menu includes:<br><br>- Sandwiches, salads and soups<br><br>- Indian thali and Chinese combos<br><br>- Desserts and beverages",
        "buttons": [
            {"label": "More services",  "next": "services_menu"},
            {"label": "Back",           "next": "BACK"},
        ]
    },

    "svc_spa": {
        "message": "<strong>Serenity Spa and Wellness Centre</strong><br><br><b>Open</b>: 9 AM - 9 PM (daily)<br><br><b>Services</b>: Swedish massage, aromatherapy, facials, yoga sessions.<br><br><b>Sessions</b> from Rs. 1,500. Prior appointment recommended.",
        "buttons": [
            {"label": "Book a session", "next": "contact_menu"},
            {"label": "More services",  "next": "services_menu"},
            {"label": "Back",           "next": "BACK"},
        ]
    },

    "svc_parking": {
        "message": "We offer <strong>complimentary valet parking</strong> for all hotel guests.<br><br><b>50+ spots</b> available,<b> 24/7</b> security monitored.<br><br><b>Visitor parking</b> available at Rs. 50/hour.",
        "buttons": [
            {"label": "More services",  "next": "services_menu"},
            {"label": "Back",           "next": "BACK"},
        ]
    },

    "svc_laundry": {
        "message": "<strong>Laundry and Dry Cleaning</strong><br><br><b>Same-day service</b>: order before 9 AM, ready by 6 PM.<br><br><b>Express service (+50%)</b>: 4-hour turnaround.",
        "buttons": [
            {"label": "More services",  "next": "services_menu"},
            {"label": "Back",           "next": "BACK"},
        ]
    },

    "svc_pool": {
        "message": "<strong>Pool and Fitness Centre</strong><br><br><b>Pool</b>: 6 AM - 10 PM<br><b>Gym</b>: 5 AM - 11 PM<br><br>Complimentary for all guests. Towels provided. Swimwear required in pool area.",
        "buttons": [
            {"label": "More services",  "next": "services_menu"},
            {"label": "Back",           "next": "BACK"},
        ]
    },

    # -- FAQs --

    "faq_menu": {
        "message": "Here are our most frequently asked questions. What would you like to know?",
        "buttons": [
            {"label": "Check-in and check-out",  "next": "faq_checkin"},
            {"label": "Pet policy",              "next": "faq_pets"},
            {"label": "Cancellation policy",     "next": "faq_cancel"},
            {"label": "Smoking policy",          "next": "faq_smoking"},
            {"label": "Wi-Fi",                   "next": "faq_wifi"},
            {"label": "Children and extra beds", "next": "faq_kids"},
            {"label": "Back",                    "next": "BACK"},
        ]
    },

    "faq_checkin": {
        "message": "<strong>Check-in:</strong> 3:00 PM onwards<br><strong>Check-out:</strong> 11:00 AM<br><br>Early check-in and late check-out available on request (subject to availability, extra charge may apply).<br><br>ID proof required at check-in.",
        "buttons": [
            {"label": "More FAQs",  "next": "faq_menu"},
            {"label": "Back",       "next": "BACK"},
        ]
    },

    "faq_pets": {
        "message": "We are a <strong>pet-friendly hotel!</strong><br><br>Small pets (under 10 kg) are welcome with a Rs. 500/night pet fee. <br><br>Please notify us in advance. Pets must be leashed in public areas.",
        "buttons": [
            {"label": "More FAQs",  "next": "faq_menu"},
            {"label": "Back",       "next": "BACK"},
        ]
    },

    "faq_cancel": {
        "message": "<strong>Cancellation Policy:</strong><br><br>- <b>Free cancellation</b> up to 48 hours before check-in<br><br>- <b>Within 48 hours</b>: 1 night charge applies<br><br>- <b>No-show</b>: Full booking charged<br><br>Flexible rates available for extra peace of mind.",
        "buttons": [
            {"label": "More FAQs",     "next": "faq_menu"},
            {"label": "Booking issue", "next": "complaint_booking"},
            {"label": "Back",          "next": "BACK"},
        ]
    },

    "faq_smoking": {
        "message": "<strong>Grand Stay is a smoke-free hotel.</strong><br><br>Smoking is permitted only in designated outdoor areas. A deep-cleaning fee of Rs. 2,500 applies if smoking is detected in a room.",
        "buttons": [
            {"label": "More FAQs",  "next": "faq_menu"},
            {"label": "Back",       "next": "BACK"},
        ]
    },

    "faq_wifi": {
        "message": "<strong>Complimentary high-speed Wi-Fi</strong> is available throughout the hotel.<br><br><b>Network</b>: GrandStay<br><br><b>Password</b>: Available at reception or in your room welcome card.<br><br><b>Speed</b>: up to <b>100 Mbps</b>.",
        "buttons": [
            {"label": "More FAQs",  "next": "faq_menu"},
            {"label": "Back",       "next": "BACK"},
        ]
    },

    "faq_kids": {
        "message": "<strong>Children are welcome!</strong><br><br>- <b>Children under 5</b>: stay free<br><br>- <b>Extra bed</b>: Rs. 800/night (for children under 12)<br><br>- <b>Baby cots</b> available on request (free)<br><br>We have a <b>kids play area</b> open 10 AM - 7 PM.",
        "buttons": [
            {"label": "More FAQs",  "next": "faq_menu"},
            {"label": "Back",       "next": "BACK"},
        ]
    },

    # -- COMPLAINTS --

    "complaintX": {
            "message": "Please select the apporpriate option.",
            "buttons":[
                {"label":"Make a complaint", "next": "complaint"},
                {"label":"Delete a complaint or message", "next":"delete_request"},
                {"label":"Back", "next":"BACK"}
            ]

    },
    "delete_request":{
            "message":"🗑️ Accidentally shared personal info in a complaint or message?<br><br>Enter your <b>unique reference ID</b> below (e.g. <code>CP-H722NRAZ</code>) and we'll delete that entry for you.<br><br><b>⚠️ Note:</b> This only removes the entry — it cannot undo any harm already caused by sharing the info.",
            "buttons":[
                {"label":"Main Menu", "next": "BACK"},
                {"label":"Back", "next":"complaintX"}
            ]
    },
    "complaint": {
        "message": "😔 Sorry you're facing an issue.Please describe your complaint below.<br><br><b>⚠️ Do not share personal details</b><br>(name, email, phone, address, etc.)<br><br>You're responsible for any personal info shared here.",
        "buttons": [
            {"label": "Back",       "next": "BACK"},
            {"label": "Start over", "next": "START"}]
    },

    "complaint_booking": {
        "message": "😔 Sorry about the booking trouble.Please describe your issue below.<br><br><b>⚠️ Do not share personal details</b><br>(name, email, phone, address, etc.)<br><br>You're responsible for any personal info shared here.",
         "buttons": [
            {"label": "Back",       "next": "BACK"},
            {"label": "Start over", "next": "START"}]
    },  

    "complaint_forward": {
        "message": "Your complaint has been logged.<br><br>We sincerely apologize for the inconvenience.",
        "buttons": [
            {"label": "Back",       "next": "BACK"},
            {"label": "Start over", "next": "START"}
        ]
    },

    # -- CONTACT --

    "contact_menu": {
        "message": "Here is how you can reach us:<br><br><strong>Front desk (24/7):</strong> +91-XXXX-XXXXXX<br><strong>Email:</strong> hello@grandstay.com<br><strong>Website:</strong> grandstay.com<br><br>Or leave a message here and we will get back to you.",
        "buttons": [
            {"label": "Leave a message",  "next": "contact_message"},
            {"label": "Back",             "next": "BACK"},
        ]
    },

    "contact_message": {
        "message": "💬 Type your message below and we'll forward it to our team.<br><br>⚠️ <b>Do not share personal details</b><br>(name, email, phone, address, etc.)<br><br>You're responsible for any personal info shared here.",
        "buttons": [
            {"label": "Message sent - thank you!", "next": "resolve_check"},
            {"label": "Back",                      "next": "BACK"},
        ]
    },

    # -- RESOLUTION --

    "resolve_check": {
        "message": "Was there anything else I can help you with today?",
        "buttons": [
            {"label": "Yes, I need more help",  "next": "BACK"},
            {"label": "No, I am all set",        "next": "goodbye"},
        ]
    },

    "goodbye": {
        "message": "Thank you for choosing <strong>Grand Stay Hotel</strong>!<br><br>We hope to make your stay truly memorable. Have a wonderful day!<br><br><em>- The Grand Stay Team</em>",
        "buttons": [
            {"label": "Start over", "next": "START"},
        ]
    },

    # -- BACK TO MAIN --

    "BACK": {
        "message": "Welcome back! How else can I assist you?",
        "buttons": [
            {"label": "Book a room",   "next": "book_menu"},
            {"label": "Our services",  "next": "services_menu"},
            {"label": "FAQs",          "next": "faq_menu"},
            {"label": "Complaints",    "next": "complaintX"},
            {"label": "Contact us",    "next": "contact_menu"},
        ]
    },
}

starN = {"currentNode":"START"}

def start_node():
    return Flow[starN["currentNode"]]

def get_node(node_key):
    """Return a flow node by its key, or None if not found."""
    return Flow.get(node_key)

