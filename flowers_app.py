import streamlit as st

from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import requests

st.set_page_config(
	page_title = "Flower Classifier",
	page_icon = "sunflower"
	)
	
st.title(':sunflower: Flower classifier')
st.subheader('At the moment, only 5 different flowers can be classified.')

st.sidebar.title('Intent of this project')

st.sidebar.write('To classify 5 different flowers, using transfer learning.')

st.sidebar.title('Dataset')
st.sidebar.markdown('**Flowers Dataset from Tensorflow**')
st.sidebar.text('@ONLINE {tfflowers')
st.sidebar.text('author = "The TensorFlow Team",')
st.sidebar.text('title = "Flowers",')
st.sidebar.text('month = "jan",')
st.sidebar.text('year = "2019",')
st.sidebar.text('url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }')

st.sidebar.title('Future work')
st.sidebar.write('1. Add more categories of flowers & re-train')
st.sidebar.write('2. Object detection so that bounding boxes can be put. SqueezeDet model to be explored.')

st.sidebar.title('Author')
st.sidebar.write('[Sambhavi Dhanabalan] (https://www.linkedin.com/in/sambhavi-dhanabalan/)')

st.write('Feature extraction of Torchvision\'s Squeezenet model (version 1) has been used in this project. Prediction call is performed using FastAPI.')
st.write('To know more about Squeezenet architecture, refer to this paper:')
st.write('[SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size](https://arxiv.org/abs/1602.07360)')
expander = st.beta_expander("Click to know more on the training process")
expander.write('Dataset used is the [Tensorflow\'s flower dataset.](https://www.tensorflow.org/datasets/catalog/tf_flowers)')
expander.write('Daisy, Dandelion, Rose, Sunflower & Tulips are the five different classes in the dataset.')
expander.write('A total of 3670 images is present, approximately 700-800 images per class.')
expander.write('50 epochs were run for training the dataset. Weights and Biases was used for experiment tracking.')
expander.write('80% of images was used for training, 10% for validation and 5% for testing. A training accuracy of 92% was reached.')
expander.write('This is how the confusion matrix looks like:')
image = Image.open('https://ibb.co/mzYm1Kc')
expander.image(image, width=500)
expander.write('FastAPI was used to invoke the actual prediction of uploaded flower used the weights trained as explained above. That piece of code is deployed in another cloud server.')

st.subheader('Upload a flower image')
uploaded_file = st.file_uploader(label="The models are trained to classify sunflower, rose, dandelion, tulip and daisy only.", 	type=['png', 'jpg', 'jpeg'], accept_multiple_files=False, key="None", help="Only .png, .jpg, and .jpeg files are supported")

classifyapi_url = "http://139.59.13.253:8008/predict"

if uploaded_file is not None:
	m = MultipartEncoder(
		fields={'input_image': ('filename', uploaded_file, 'image/jpeg')}
	)

	response = requests.post(classifyapi_url, 
					data=m,
					headers={
						'Content-Type': m.content_type
					})
	if response is None:
		st.subheader('Classify API is down. Please try later!')
	else:
		output = response.json()
		
		col1, col2 = st.beta_columns(2)
		col1.subheader('Output from Model:')
		col2.subheader(output['Prediction'])
		
		col1, col2 = st.beta_columns(2)
		col1.subheader('Prediction score:')
		col2.subheader(output['Score'])
		
		st.subheader('Prediction scores of all classes')
		col1, col2 = st.beta_columns(2)
		col1.write(output['labels'])
		col2.write(output['Scores'])
