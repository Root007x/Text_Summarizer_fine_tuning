# Text Summarizer

A machine learning project for automatic text summarization using transformer-based models. This project provides both a training pipeline and a FastAPI-based API for generating summaries from input text.

## Overview

This project implements an end-to-end text summarization solution using:
- **Transformers** for state-of-the-art NLP models
- **Hugging Face Datasets** for dataset management
- **FastAPI** for serving predictions
- **Docker** for containerization
- **MLOps pipeline** with data ingestion, transformation, model training, and evaluation stages

## Features

- ✨ **Multi-stage pipeline**: Data ingestion → Transformation → Model Training → Evaluation
- 🚀 **FastAPI REST API**: Easy-to-use endpoints for training and predictions
- 📊 **Comprehensive evaluation**: Uses ROUGE and SacreBLEU metrics
- 🐳 **Docker support**: Containerized deployment
- 📝 **Jupyter notebooks**: Exploratory research and development
- 📈 **Logging and configuration**: Centralized config management with YAML

## Project Structure

```
.
├── app.py                          # FastAPI application
├── main.py                         # Training pipeline entry point
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project configuration
├── params.yaml                     # Model training parameters
├── Dockerfile                      # Docker configuration
├── config/
│   └── config.yaml                 # Application configuration
├── src/textSummarizer/
│   ├── components/
│   │   ├── data_ingestion.py       # Data loading and preparation
│   │   └── data_transformation.py  # Tokenization and preprocessing
│   ├── pipeline/
│   │   ├── stage_1_data_ingestion_pipeline.py
│   │   ├── stage_2_data_transformation_pipeline.py
│   │   ├── stage_3_model_trainer_pipeline.py
│   │   └── stage_4_model_evaluation_pipeline.py
│   ├── config/
│   │   └── configuration.py        # Configuration management
│   ├── utils/
│   │   └── common.py               # Utility functions
│   └── logging/                    # Logging setup
├── research/                       # Jupyter notebooks for exploration
└── artifacts/                      # Generated artifacts (data, models)
```

## Installation

### Prerequisites
- Python 3.10 or higher
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Text_Summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt --index https://pypi.org/simple --index https://download.pytorch.org/whl/cu128
   ```
   
   Or with pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### API Server

Start the FastAPI server:

```bash
python app.py
```

The API will be available at `http://localhost:8080`

#### Endpoints

- **GET `/`** - Redirects to interactive API documentation (`/docs`)
- **GET `/train`** - Trigger the training pipeline
- **POST `/predict`** - Generate a summary for input text

### Predict via API

```bash
curl -X POST "http://localhost:8080/predict?text=Your+text+here" \
  -H "accept: application/json"
```

Response:
```json
{
  "Summarized Text": "Generated summary..."
}
```

### Training Pipeline

Run the full training pipeline:

```bash
python main.py
```

This executes the following stages:
1. **Data Ingestion**: Load SAMSum dataset
2. **Data Transformation**: Tokenize and prepare data
3. **Model Training**: Fine-tune transformer model
4. **Evaluation**: Compute ROUGE and SacreBLEU metrics

## Configuration

### Model Parameters (`params.yaml`)

```yaml
TrainingArguments:
    num_train_epochs: 1
    warmup_steps: 500
    per_device_train_batch_size: 1
    weight_decay: 0.01
    logging_steps: 10
    eval_strategy: steps
    eval_steps: 500
    save_steps: 1000000
    gradient_accumulation_steps: 16
    report_to: none
```

Modify `params.yaml` to customize training behavior.

## Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t text-summarizer .

# Run container
docker run -p 8080:8080 text-summarizer
```

## Dependencies

Key packages:
- `transformers` - Hugging Face transformer models
- `datasets` - Dataset loading and processing
- `torch` - PyTorch deep learning framework
- `fastapi` & `uvicorn` - API framework
- `rouge_score` & `sacrebleu` - Evaluation metrics
- `pandas`, `nltk`, `matplotlib` - Data processing and visualization

See `requirements.txt` for complete list.

## Data

The project uses the **SAMSum dataset** containing:
- Abstractive summaries of conversations
- Training, validation, and test splits
- Split across multiple cached arrow files for efficiency

## Evaluation Metrics

- **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation)
- **SacreBLEU** (Machine translation evaluation metric)

## Development

Exploratory notebooks available in `research/`:
- `1_data_ingestion.ipynb` - Dataset exploration
- `2_data_transformation.ipynb` - Preprocessing pipeline
- `3_model_trainer.ipynb` - Model training
- `text_summarizer.ipynb` - Full pipeline walkthrough

## Logging

Logs are configured in `src/textSummarizer/logging/`. All pipeline stages output detailed logs to help with debugging and monitoring.

## Architecture

The project follows MLOps best practices:

1. **Config Management** - Centralized configuration via YAML files
2. **Entity Layer** - Data models for configuration
3. **Component Layer** - Individual processing components
4. **Pipeline Layer** - Orchestrates components into stages
5. **API Layer** - FastAPI endpoints for inference and training

## License

See [LICENSE](LICENSE) file for details.

## Contributing

1. Create a branch for your feature
2. Make your changes
3. Submit a pull request

## Support

For issues and questions, please open an issue in the repository.

---

**Version**: 0.1.0  
**Last Updated**: January 2026
