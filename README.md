🎓 Education Recommendation System using Machine Learning
This project is a machine learning-powered recommendation system that suggests the most suitable career paths or study fields to students based on their academic performance, personal interests, and other factors such as part-time jobs and extracurricular activities.

The application is built using Streamlit for the web interface and uses a trained machine learning model for predictions.

🚀 Features:
Easy-to-use web interface powered by Streamlit.

Accepts student details such as:

Academic scores (Math, History, Physics, Chemistry, Biology, English, Geography)

Weekly self-study hours

Absence days

Gender

Part-time job status

Extracurricular activities

Predicts and recommends top 3 suitable career fields along with probabilities.

Responsive multi-page app experience.

📂 Project Structure:

Education_Recommendation_system_using_Machine_Learning/
│
├── pages/                             # Streamlit App Files
│                       
│   ├── Recommend.py                 # Input page script
│                      
│
├── Models/                          # Model Files
│   ├── model.pkl                    # Trained ML model
│   └── scaler.pkl                   # Scaler for preprocessing
│--Home.py
├── README.md                        # Project Documentation (this file)
├── requirements.txt                 # Required Python libraries
└── main.py                          # Main app runner (optional for Streamlit single-file mode)
🛠️ Technologies Used:
Python 3.x

scikit-learn (for model building & loading)

numpy (for numeric processing)

Streamlit (for web interface)

pandas (optional, if needed for data handling)

✅ How to Run the Project:
Clone this repository:

git clone https://github.com/your-username/Education_Recommendation_system_using_Machine_Learning.git
cd Education_Recommendation_system_using_Machine_Learning
Install dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app/Home.py
Use the navigation sidebar to switch between:

Home

Recommendation Form

Result Page

🎯 Model Details:
Supervised Classification Model.

Predicts career recommendations based on academic & personal features.

Shows Top 3 recommendations with associated prediction probabilities.

📝 Future Improvements:
Add visuals/graphs to result page.

Save user recommendation history.

Improve UI/UX for better engagement.

Integrate backend database (Optional).

