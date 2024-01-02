# Real-time Weather Data Pipeline

## Overview

Welcome to the Real-time Weather Data Pipeline project! This solution fetches real-time weather data, stores it in the cloud, and visualizes it on a Power BI dashboard. The pipeline is built using Apache Kafka, AWS S3, Apache Airflow, and Power BI.

# Architecture
![weather_pipeline](https://github.com/KadamAkshay5595/Open_weather_streaming_datapipeline/assets/135830881/a2adaf8e-66f2-46b1-ab2d-0ec661245c9d)

## Key Components

1. **Apache Kafka:**
   - Real-time data streaming for efficient communication between producers and consumers.

2. **AWS S3 (Simple Storage Service):**
   - Scalable and reliable cloud storage for storing real-time weather data.

3. **Apache Airflow:**
   - Orchestrates the entire data pipeline, automating tasks such as data fetching, processing, and storage.

4. **Power BI:**
   - Data visualization tool creating interactive dashboards for real-time insights.

## Pipeline Workflow

1. **Data Ingestion with Kafka:**
   - Real-time weather data is ingested into the pipeline using Apache Kafka.

2. **Data Storage in AWS S3:**
   - Fetched weather data is stored in AWS S3 for scalable and reliable storage.

3. **Airflow Orchestration:**
   - Apache Airflow automates the entire data pipeline, ensuring smooth data flow.

4. **Power BI Visualization:**
   - Power BI connects to AWS S3, creating visually rich dashboards for real-time weather insights.

## Benefits

- **Real-time Insights:** Apache Kafka enables up-to-the-minute insights into changing weather conditions.

- **Scalability:** AWS S3 accommodates the growing volume of real-time weather data.

- **Automation:** Apache Airflow automates the pipeline, reducing manual intervention and ensuring reliable data processing.

- **Interactive Dashboards:** Power BI offers dynamic and interactive dashboards for exploring real-time weather data.

## Getting Started

To explore the real-time weather data pipeline, follow these steps:

1. Clone the repository: `git clone [repository_url]`
2. Install and configure Apache Kafka, AWS CLI, Apache Airflow, and Power BI.
3. Run the Airflow DAG for orchestrating the pipeline.
4. Connect Power BI to the AWS S3 bucket and visualize real-time weather data.

## Contributing

We welcome contributions! If you'd like to contribute, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the open-source communities of Apache Kafka, Apache Airflow, and Power BI.
- Inspiration from the advancements in real-time data processing and visualization.

Feel free to explore the project, contribute, and enjoy the real-time insights into weather conditions with our powerful data pipeline!

