
# Movie Recommendation System 🎥  
**A content-based filtering system that recommends movies tailored to user preferences.**  

This project uses a content-based approach to suggest movies based on user-selected inputs. It enhances the experience by providing posters, ratings, cast, and director details for each recommended movie.  

---

## 🌟 **Features**

- **Personalized Recommendations**  
  Suggests movies based on their similarity to the selected title.  
- **Poster Integration**  
  Dynamically fetches and displays movie posters for recommended titles.  
- **Movie Details**  
  Provides IMDb ratings, cast, directors, and an overview for each movie.  
- **Interactive Interface**  
  Built with **Streamlit**, offering a responsive and easy-to-use platform.  

---

## 📂 **Project Structure**

```plaintext
Movie-Recommendation-System/
│
├── 📄 app.py                # Main Streamlit application file
├── 📄 Movies_dict.pkl       # Required movies dictionary pickle file
├── 📁 APP_UI                # Folder show how user interface will looks like
└── 📄 README.md             # Project description and usage details
```

---

## 🛠 **Tech Stack**

- **Programming Language**: Python  
- **Libraries**:  
  - Pandas: Data cleaning and manipulation  
  - Scikit-learn: TF-IDF Vectorizer and Cosine Similarity  
  - Requests: API integration for fetching movie posters  
  - Streamlit: Interactive app development  

---

## 📊 **Key Functionalities**

1. **Recommendation System**  
   - Computes similarity scores using **TF-IDF Vectorization**.  
   - Employs **Cosine Similarity** to find movies most similar to the input title.  

2. **Fetching Posters and Information**  
   - Uses the **TMDb (The Movie Database) API** to fetch:  
     - High-resolution movie posters.  
     - Ratings and descriptions.  
     - Cast and crew information.  
   - Integrates results seamlessly into the app interface.  

3. **Interactive Features**  
   - User clicks a movie to view its recommendations.  
   - Details are displayed without reloads for a smooth experience.  

---

## 🚀 **How to Run the App**

1. Clone the repository:  
   ```bash
   git clone https://github.com/Praveenravva61/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```

2. Obtain TMDb API Key:  
   - Sign up at [The Movie Database](https://www.themoviedb.org/).  
   - Generate an API key from your account settings.  
   - Save it in the app as an environment variable or directly in the code.  

3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at:  
   `http://localhost:8501`

---

## 📈 **App Demo**

![1](https://github.com/user-attachments/assets/92b434d3-de93-4f64-8306-45de65797abb)
![2](https://github.com/user-attachments/assets/7f96de61-062d-414d-8c4f-7aa5330453ba)
![3](https://github.com/user-attachments/assets/1ceb7dc9-cd3f-4ce2-91e0-a5492c35d6e9)
![4](https://github.com/user-attachments/assets/4b3326e0-1ba8-4c6f-9325-e0d755a5b0e0)
![5](https://github.com/user-attachments/assets/71a76fb3-09d9-4436-b61a-db58475743f2)



## 🏗️ **How It Works**

1. **Data Preprocessing**  
   - The movie dataset is cleaned and prepared for analysis.  
   - Content features like genres, keywords, cast, and crew are extracted.  

2. **Content-Based Filtering**  
   - A **TF-IDF Vectorizer** converts text-based features into numerical vectors.  
   - **Cosine Similarity** measures the similarity between movies.  

3. **Integration with TMDb API**  
   - For each recommended movie:  
     - A GET request is sent to TMDb to fetch the poster and metadata.  
     - The results are displayed in the app.  

---

## 👨‍💻 **About Me**

I am a Data Scientist passionate about building personalized recommendation systems and interactive applications. Check out more of my work: [Praveenravva61](https://github.com/Praveenravva61).

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.  

---

## 🤝 **Contributions**

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repository and submit a pull request.  

---

## 📧 **Contact**

For inquiries or collaborations:  
- **Email**: praveen.ravva61@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/praveen-ravva

---
