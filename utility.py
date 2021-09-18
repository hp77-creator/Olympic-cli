import pickle

model_name = "data/svg files/"

def run_model(event: str):
	global model_name
	model_name += event+".sav"
	model_l = pickle.load(model_name, 'rb')
	return model_l


def predict_model(model, inp):
	return model.predict([inp])

