import google as genai                                                                                                                                                                                                    
import os                                                                                   
                                                                             
# Configure API key (you should set this as an environment variable for security)                                                                         
# Replace "YOUR_API_KEY" with your actual Gemini API key                                                           
# genai.configure(api_key="YOUR_API_KEY")  # Directly setting is discouraged for security                                                                                                                                              
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Get from environment variable                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                         
if not GOOGLE_API_KEY:                                                                                                                                                                                                                                                                                                                                                            
    print("Error: GOOGLE_API_KEY environment variable not set.")                                                                                                                                                                                                                                                                                                                  
    print("Please set the environment variable:  export GOOGLE_API_KEY='YOUR_API_KEY'")                                                                                                  
    exit()  # Exit the script if the API key is missing                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                  
client = genai.Client(api_key="AIzaSyCfDiiSYF9Rr2oezb9qHdhos7q8ovZwvo8")                                                                                                                    
                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                  
# Function to get user input from the terminal                                                                     
def get_user_input():                                                                                                                                                                    
    print("Enter your query (press Ctrl+D or Ctrl+Z (Windows) when finished):")                                    
    lines = []                                                                              
    try:                                                                                                                                                                                                                                                                                                            
        while True:                                                                         
            line = input()                                                                  
            lines.append(line)                                               
    except EOFError:                                                                        
        pass  # Handles Ctrl+D or Ctrl+Z                                                                           
    return "\n".join(lines)  # Join lines with newline characters                           
                                                                                            
                                                                                            
# Function to send a query to the Gemini API and print the response                         
def send_query_to_gemini(prompt_text):                                                      
    model = genai.GenerativeModel('gemini-pro')  # specify which model you are using                                                                                                                                                   
    try:                                                                                    
        response = model.generate_content(prompt_text)                                      
        print("\nGemini's Response:")                                                       
        print(response.text)                                                                
        # You can also print response.prompt_feedback for safety information if needed                                                                                                                                                 
    except Exception as e:                                                                                                                                                                                                                                                                                                                                                        
        print(f"Error during API call: {e}")                                                                       
                                                                                            

# Main part of the script                                                                   
if __name__ == "__main__":                                                                  
    user_query = get_user_input()                                                           
    if user_query:  # Check if user provided input                                          
        send_query_to_gemini(user_query)                                                                           
    else:                                                                                                                                                                                                                                                                                                                                                                         
        print("No query provided.  Exiting.")                                                                                                                                                                               
