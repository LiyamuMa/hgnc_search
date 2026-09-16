# Summary

This webapp takes in hgnc_id or symbol and returns the following information:
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