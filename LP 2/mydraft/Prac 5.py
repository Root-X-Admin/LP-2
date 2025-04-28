# 5.	Develop an elementary Chatbot for any suitable customer interaction application.

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for easy matching

    if "order" in user_input or "status" in user_input:
        return "You can check your order status by logging into your account and visiting 'My Orders'."
    elif "return" in user_input or "refund" in user_input:
        return "Our return policy allows returns within 30 days. Please visit the 'Returns' page for details."
    elif "shipping" in user_input or "delivery" in user_input:
        return "We offer free shipping on orders above $50. Delivery usually takes 3-5 business days."
    elif "contact" in user_input or "support" in user_input:
        return "You can contact our support team at support@example.com or call us at 123-456-7890."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "thank" in user_input:
        return "You're welcome! Happy to assist you."
    else:
        return "I'm sorry, I didn't understand your question. Could you please rephrase?"

# Main loop
def run_chatbot():
    print("Welcome to Online Store Chatbot!")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
run_chatbot()
