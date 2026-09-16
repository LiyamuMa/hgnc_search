# Summary
[![codecov](https://codecov.io/gh/LiyamuMa/hgnc_search/graph/badge.svg?token=78T6BWD75F)](https://codecov.io/gh/LiyamuMa/hgnc_search)

This webapp takes in **HGNC ID** or **Gene Symbol** and returns the following information:
- HGNC ID
- Gene Symbol
- Gene Name
- Previous Gene Symbol
- Previous Gene Name
- Alias Symbol
- Alias Name
- Mane Select Transcripts

## Instructions
To create conda environment, run:
```python
conda env create -f environment.yaml
```

To activate conda environment, run:
```python
conda activate hgnc_app_env
```

To install applications, run:
```python
pip install -e
```

To load the webapp, run:
```python
python manage.py runserver
```
