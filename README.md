# Text Classification Using Naive Bayes (Persian Texts)

This project focuses on developing a text classification program for Persian text datasets using the Naive Bayes algorithm. The project was developed as part of a Bachelor’s thesis and demonstrates the use of data preprocessing, normalization, and machine learning to classify Persian texts into specific categories.

## **Features**
- Classifies Persian texts into categories:
  - Normal
  - Rudeness
  - Ads
  - Political
- Implements a custom normalization process tailored for Persian texts.
- Supports offline dataset processing and real-time web-based classification.
- Outputs the model’s accuracy and allows saving the trained model for future use.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `scikit-learn` for machine learning
  - `BeautifulSoup` for web scraping
  - `requests` for accessing web content
  - `joblib` for model persistence

---

## **Project Structure**
```
Text-Classification/
├── main-multi-final_web.py    # Main Python script for the project
├── dataset-example.xlsx       # Example dataset (not included in the repo)
├── finalized_model_Classifier.sav # Saved model file for reuse
└── README.md                  # Project documentation
```

---

## **How to Run the Project**

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/faryanadib/Text-Classification.git
cd Text-Classification
```

### Step 2: Install Required Libraries
Install the dependencies listed below:
```bash
pip install pandas scikit-learn beautifulsoup4 requests joblib
```

### Step 3: Add Your Dataset
Place your `.xlsx` dataset in the project folder. The dataset should have the following columns:
- `label`: The category of the text (e.g., Normal, Ads, Political, etc.).
- `body`: The text content to be classified.

### Step 4: Run the Script
Run the main script:
```bash
python main-multi-final_web.py
```

Follow the instructions in the terminal to:
1. Train the model on the provided dataset.
2. Analyze the content of a given website.

---

## **Outputs**
- **Accuracy**: The script prints the accuracy of the Naive Bayes model.
- **Web Content Analysis**: Analyzes and categorizes text content from websites and prints counts for each category.

---

## **Future Improvements**
- Enhance the normalization process for Persian texts.
- Add support for additional machine learning models (e.g., SVM, Random Forest).
- Deploy the model as an API for integration with web applications.
- Extend the project to support multilingual text classification.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- Developed as part of a Bachelor’s thesis under the supervision of **Dr. Amine Amini**.
- Special thanks to all contributors and reviewers.
