import streamlit as st

from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import requests

st.title(':sunflower: Let\'s classify a few flowers!')

st.sidebar.title('Intent of this project')

st.sidebar.text('To classify 5 different flowers,')
st.sidebar.text('using transfer learning.')

st.sidebar.title('Dataset')
st.sidebar.markdown('**Flowers Dataset from Tensorflow**')
st.sidebar.text('@ONLINE {tfflowers')
st.sidebar.text('author = "The TensorFlow Team",')
st.sidebar.text('title = "Flowers",')
st.sidebar.text('month = "jan",')
st.sidebar.text('year = "2019",')
st.sidebar.text('url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }')

st.sidebar.title('Future work')

st.subheader('Step 1: Upload a flower image')
uploaded_file = st.file_uploader(label="The models are trained to classify sunflower, rose, dandelion, tulip and daisy only.", type=['png', 'jpg', 'jpeg'], accept_multiple_files=False, key="None", help="Only .png, .jpg, and .jpeg files are supported")

st.subheader('Step 2: Click on Classify button below')
st.button('Classify')

classifyapi_url = "http://139.59.13.253:8008/predict"

if uploaded_file is None:
	st.subheader('Please upload an image first and then click Classify!')
else:
	uploaded_file="https://github.com/SambhaviPD/flower-classification/tree/main/images/rose.jpg"
	
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

	st.subheader('Output: Here''s what the model classifies your input as:')					
	st.markdown(output['Prediction'])
