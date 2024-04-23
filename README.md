# NLP Text Toxicity FastAPI Containerized

## Introduction
This project aims to develop a text toxicity analyzer using natural language processing (NLP) techniques. The project involves creating a Python script to fetch comments from the dummyjson website. Subsequently, an application will be built using FastAPI or Flask to clean the comments, perform toxicity analysis using the Detoxify model, and store the data in MongoDB. Finally, the application will be containerized using Docker for easy deployment and scalability.

## Instructions
1. **Fetch Comments:** Develop a Python script to fetch comments from the dummyjson website [dummyjson.com](https://dummyjson.com/).
2. **Build Application:** Create a FastAPI application to:
   - Clean the comments.
   - Analyze the toxicity of the comments using the Detoxify model [GitHub Repository](https://github.com/unitaryai/detoxify).
   - Load the data into MongoDB.
3. **Containerize Application:** Containerize the ETL (Extract, Transform, Load) application using Docker.

## Getting Started

For simplicity, we first wrote the entire code in a Jupiter notebook file "JupyterCode.ipynb" without the use of container nor FastAPI just to ensure all commands.

The project solution is structured in two folders as follows:

### WebToCsv

In this folder, there is the Docker container of the Python script that fetches comments from the dummyjson website and saves them in a CSV file.

### CsvToMongo

In this folder, there is the Docker container of a FastAPI application that reads the comments from the CSV file, then cleans it and analyzes the toxicity using the Detoxify model. Finally, it loads the data into MongoDB.

## Testing the Project

To test the project, follow these steps:

1. **Build and Run the WebToCsv Docker Container:**
   - Navigate to the `WebToCsv` folder.
   - Build the Docker image using the command:
   - Run the Docker image
   - After running the image, the CSV file containing the comments will be created.

2. **Build and Run the CsvToMongo Docker Container:**
   - Navigate to the `CsvToMongo` folder.
   - Build the Docker image using the command:
   - Run the Docker image:
   

3. **Access the FastAPI Application:**
   - Once the `CsvToMongo` Docker container is running, you can access the FastAPI application.
   - Open your browser and navigate to the FastAPI address and port.
   - Alternatively, you can use a Python command to request the FastAPI address and port.
   - The FastAPI application will read the comments from the CSV file, clean them, apply the toxicity analyzer, and save them in MongoDB.



## Dependencies
- Python
- FastAPI 
- Detoxify
- MongoDB
- Docker


