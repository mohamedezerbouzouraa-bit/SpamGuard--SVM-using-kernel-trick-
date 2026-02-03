import pandas as pd
#the data with which we will train the model
def load_data():
    data = {
        'Message': [
            "Congratulations! You won a prize. Click now!",
            "Hi, are we meeting tomorrow?",
            "Claim your free money today!!!",
            "Don't forget to submit the report",
            "Urgent! Update your account information",
            "Let's have lunch tomorrow",
        ],
        'Label': [1, 0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)
