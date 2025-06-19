# Resume Classifier API

## 📌 About the Project

The **Resume Classifier API** is a backend service designed to classify resumes (CVs) using machine learning models. It provides an API endpoint for uploading resumes as raw text or files (PDF), processes them to extract relevant content, and returns predicted job categories along with confidence scores.

This project is built using:

- ⚙️ **FastAPI** for the API layer
- 🧠 **scikit-learn** for the initial machine learning pipeline (with future support for PyTorch/TensorFlow)
- 📦 **MongoDB** for storing extracted resumes, classification results, and submission metadata
- ✅ **Pydantic** for input validation
- 🧪 **Unittest** for API and service-level testing
- 🐳 **Docker** for containerized development and deployment

> The goal is to create a modular, scalable, and production-ready API that demonstrates backend and ML engineering skills while solving a realistic use case.

---

## 🗓️ Dev Log

### [2025-06-15] - Project Kickoff
- Researched:
  - How to build RESTful APIs using **FastAPI**
  - **Pydantic** models for request validation and OpenAPI documentation
  - Connecting **MongoDB** with FastAPI using the async driver `motor`
- Started project scaffolding:
  - Created initial folder structure:
    - `app/models` for Pydantic schemas
    - `app/db` for MongoDB connection logic
    - `app/services` for ML and file parsing logic
    - `app/api` for route definitions
- Planned initial API route `/upload_resume/`:
  - Accepts uploaded file (`UploadFile`)
  - Extracts text and classifies using a discriminative model
  - Stores classification result in MongoDB

### [2025-06-16] - upload_resume logic and Text Extraction Structure
- Defined the core `/upload_resume` route logic in `routes.py`:
- Began implementing the Text Extraction module in `/services/text_extractor.py`
    -  Implemented specialized subclasses:
        - `PdfTextExtractor()`
        - `MSWordTextExtractor()`
        - `PlainTextExtractor()`
    - I've also created a centralized extractor selection via `call_text_extractor()`
  
### [2025-06-19] - upload_resume logic and Text Extraction Structure
- Finished `text_extractor`module and created some tests for it at `./tests/text_extractor.py`
- I'm considering just using a LLM API for the classifier (although IDK if it would be the best decision)