from data.dataset import load_data
from model.spam_model import train_model
from gui.app import launch_gui
df = load_data()
model, vectorizer = train_model(df)
launch_gui(model, vectorizer)
