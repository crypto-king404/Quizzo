# `Document_Ingestion.py`

## Overview

`Document_Ingestion.py` is a Python module designed for processing PDF documents using the `PyPDFLoader` from the `langchain_community` library. The module integrates with Streamlit to provide an interactive file uploader interface, allowing users to upload multiple PDFs, extract their pages, and store them for downstream processing. It is ideal for applications that require extracting and analyzing content from large PDF documents.

### Table of Contents
1. [Installation](#installation)
2. [Classes and Methods](#classes-and-methods)
    - [DocumentProcessor](#documentprocessor)
        - [`__init__`](#__init__)
        - [`ingest_documents`](#ingest_documents)
3. [Usage](#usage)
4. [Example](#example)
5. [Dependencies](#dependencies)

## Installation

Make sure the following libraries are installed before using the module:

```bash
pip install streamlit langchain langchain_community
```

## Classes and Methods

### `DocumentProcessor`

This class encapsulates all functionalities for processing uploaded PDF documents using Streamlit and Langchain’s `PyPDFLoader`. It provides a method to render a file uploader widget, process the uploaded PDF files, extract their pages, and display the total number of pages extracted.

#### `__init__(self)`

**Description:**
Initializes the `DocumentProcessor` class. The constructor creates an empty list, `self.pages`, which will store pages extracted from uploaded PDF documents.

---

#### `ingest_documents(self)`

**Description:**
Renders a file uploader widget in a Streamlit app for users to upload multiple PDF files. It processes each uploaded file, extracts its pages using `PyPDFLoader`, and updates the `self.pages` list with the extracted content. This method is designed to be used in a Streamlit environment to enable real-time interaction and feedback.

**Detailed Functionality:**
1. Uses Streamlit’s `st.file_uploader` widget to allow users to upload multiple PDF files simultaneously.
2. For each uploaded file:
   - Creates a temporary file with a unique identifier.
   - Loads the PDF using `PyPDFLoader`.
   - Splits the PDF into pages and adds the pages to `self.pages`.
3. Displays the total number of pages processed.

**Output:**
- Streamlit success message showing the total number of pages processed from the uploaded files.

---

## Usage

```python
import streamlit as st
from Document_Ingestion import DocumentProcessor

# Initialize the document processor
doc_processor = DocumentProcessor()

# Ingest and process uploaded documents
doc_processor.ingest_documents()

# Display the total number of pages processed
st.write(f"Total pages processed: {len(doc_processor.pages)}")
```

## Example

To run this module, make sure you are in a Streamlit environment. Simply import the `DocumentProcessor` class, call the `ingest_documents()` method, and upload the PDFs via the rendered Streamlit interface.

## Dependencies

- Python 3.x
- `streamlit`
- `langchain_community`
