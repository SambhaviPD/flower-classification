import streamlit as st

from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import requests

st.markdown(':sunflower:')
st.title('Let\'s classify a few flowers!')

st.sidebar.title('Intent of this project')

st.sidebar.text('To classify 5 different flowers,')
st.sidebar.text('using model selected by end-user.')
st.sidebar.text('Compare & contrast 2 different models.')

st.sidebar.title('Dataset')
st.sidebar.markdown('**Flowers Dataset from Tensorflow**')
st.sidebar.text('@ONLINE {tfflowers')
st.sidebar.text('author = "The TensorFlow Team",')
st.sidebar.text('title = "Flowers",')
st.sidebar.text('month = "jan",')
st.sidebar.text('year = "2019",')
st.sidebar.text('url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }')

st.sidebar.title('Future work')


st.subheader('Step 1: Choose a flower image to upload')
uploaded_file = st.file_uploader(label="The models are trained to classify sunflower, rose, dandelion, tulip and daisy only.", type=['png', 'jpg', 'jpeg'], accept_multiple_files=False, key="None", help="Only .png, .jpg, and .jpeg files are supported")

st.subheader('Step 2: Choose a model')
st.selectbox(label="Selected model will be used to classify uploaded flower image", options=('Squeezenet', 'Densenet152', 'Resnet50', 'Yolo', 'Custom CNN'))

st.subheader('Step 3: Click on Classify button below')
st.button('Classify')

classifyapi_url = "http://139.59.13.253:8008/predict"

if uploaded_file is None:
	st.subheader('Please upload an image first and then click Classify!')
else:
	m = MultipartEncoder(
        fields={'input_image': ('filename', uploaded_file, 'image/jpeg')}
        )

	response = requests.post(classifyapi_url, 
					data=m,
					headers={
						'Content-Type': m.content_type
					})

	output = response.json()

	st.subheader('Output: Here''s what the model classifies your input as:')					
	st.markdown(output['Prediction'])
	#st.subheader('Here are the unnormalized log probabilities:')
	#st.text(output['Probability'])