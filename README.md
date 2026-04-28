# IMT 542 - I4: Easy to Access

Three small Python scripts that each pull a sample of information from a different
information structure using a different access technology. Each function includes
in-comment pros/cons of its access methodology, and each prints a sample to stdout.

| Script | Information structure | Access technology |
| --- | --- | --- |
| `access_example.py` | JSON | HTTP GET to a public REST-ish API (Seattle Public Utilities taxonomy) |
| `html_example.py` | HTML | HTTP GET + HTML parsing with BeautifulSoup (Wikipedia) |
| `hf_example.py` | Tabular dataset (streamed) | Hugging Face `datasets` library |

No API keys, accounts, or local data files are needed.

## Run locally

Requires Python 3.8+.

```bash
pip install -r requirements.txt
python3 access_example.py
python3 html_example.py
python3 hf_example.py
```

## Run in Google Colab

Open a new Colab notebook and paste this into a single cell (replace the URL with
this repo's clone URL):

```python
!git clone https://github.com/zach8421/imt542-i4.git
%cd imt542-i4
!pip install -q -r requirements.txt
!python access_example.py
!python html_example.py
!python hf_example.py
```
