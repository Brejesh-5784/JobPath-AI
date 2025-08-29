# JobPath-AI

# Intelligent Resume Screening and Analysis System

[cite_start]This project is an Intelligent Resume Screening and Analysis System designed to revolutionize the recruitment process by automating and enhancing the initial screening stages[cite: 1, 13]. [cite_start]It tackles challenges like high application volume and human error by leveraging a hybrid AI approach[cite: 12, 13].

[cite_start]By combining a traditional Machine Learning (ML) model for rapid classification with a Large Language Model (LLM) for detailed data extraction, the system provides recruiters with fast, consistent, and insightful summaries of candidates[cite: 14].

## 🚀 Project Overview

[cite_start]The core goal is to transform manual recruitment into a strategic, data-driven function[cite: 84]. [cite_start]This system empowers HR teams to focus on strategic talent acquisition by handling administrative tasks, enabling them to build stronger talent pipelines more efficiently[cite: 58, 85].

### Key Benefits
* [cite_start]**Speed**: Rapidly processes a high volume of applications[cite: 15, 16].
* [cite_start]**Consistency**: Reduces human bias through a standardized evaluation process[cite: 17, 19].
* [cite_start]**Insights**: Provides a deeper analysis that goes beyond simple keyword matching[cite: 18, 20].

## ✨ Features

* [cite_start]**Automated Resume Classification**: The system automatically categorizes resumes into specific job roles using a KNN classifier[cite: 59, 61]. [cite_start]This eliminates the need for manual sorting[cite: 63].
* [cite_start]**Structured Information Extraction**: An LLM parses and extracts key information such as contact details, skills, and work history into a clean, structured JSON format[cite: 44, 62].
* [cite_start]**Domain Switch Suggestions**: The LLM analyzes a candidate's skills to suggest alternative job roles they might be suitable for[cite: 45, 65]. [cite_start]This helps in building a talent pipeline and prevents talent loss[cite: 66].
* [cite_start]**Skill Gap Analysis & Career Tips**: The system can generate career tips for candidates and highlight potential skill gaps for a given role[cite: 45, 72]. [cite_start]This provides deeper insight for interview preparation[cite: 77].
* [cite_start]**Centralized Final Output**: All the processed information, including the predicted role and extracted data, is aggregated into a single, user-friendly dashboard for a holistic view[cite: 34, 73, 75].

## 🏗️ System Architecture

[cite_start]The system is built on a dual-pipeline architecture that processes resume data in parallel to generate a comprehensive candidate profile efficiently[cite: 23, 25].

The workflow is as follows:

1.  **Resume Upload**: The user uploads a resume. [cite_start]The system supports `PDF`, `DOCX`, and `TXT` formats[cite: 26, 27].
2.  [cite_start]**PDF Parsing**: Raw text is extracted from the uploaded document for analysis[cite: 30, 31].
3.  [cite_start]**Parallel Processing**: The extracted text is sent to two pipelines simultaneously[cite: 28]:
    * [cite_start]**ML Classification Pipeline**: Predicts the job role[cite: 33].
    * [cite_start]**LLM Extraction Pipeline**: Extracts detailed information[cite: 33].
4.  [cite_start]**Final Output**: The results from both pipelines are aggregated into a single, user-friendly candidate summary[cite: 32, 34].

## 🛠️ Methodology & Technology

[cite_start]The system's core functionality is powered by robust ML and LLM components[cite: 38].

### Machine Learning Pipeline

* [cite_start]**TF-IDF Vectorizer**: Converts the resume text into numerical vectors[cite: 40, 52]. [cite_start]This allows the ML model to mathematically compare documents for precise predictions[cite: 40, 52].
* [cite_start]**K-Nearest Neighbors (KNN) Classifier**: A fast and reliable ML model trained on labeled data to recognize patterns and classify resumes into job categories[cite: 41, 50, 51].
* [cite_start]**Label Encoder**: Used to manage the categorical job role data during the model's training phase[cite: 42].

### LLM Extraction Pipeline

* [cite_start]**Large Language Model (LLM)**: Performs a deep analysis of the resume text to extract context-rich information like skills and work history into a structured format[cite: 44, 53]. [cite_start]It also powers advanced features like career tips and domain switch suggestions[cite: 45, 53].


## 👨‍💻 Author

* [cite_start]**Presented By**: Brejesh.V.D, ML Engineering Intern[cite: 2, 3].
