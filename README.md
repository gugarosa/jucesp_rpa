# JUCESP Robot Process Automation

*This repository holds all the necessary code to run the an automation robot that extracts company-related information at [JUCESP](https://www.jucesponline.sp.gov.br/BuscaAvancada.aspx).*

---

## Package Guidelines

### Installation

Install all the pre-needed requirements using:

```Python
pip install -r requirements.txt
```

### Configuration File

Please copy `config.ini.example` to `config.ini` and fill out the 2Captcha API key.

---

## Usage

### Advanced Search

The first step is to perform the advanced search at JUCESP and extracts its HTML content. To accomplish such a step, one needs to use the following script:

```Python
python advanced_search.py -h
```

*Note that `-h` invokes the script helper, which assists users in employing the appropriate parameters.*

### Parse Advanced Search

After conducting the search, one needs to parse the HTML into a CSV holding the companies' identifier and city. Please, use the following script to accomplish such a procedure:

```Python
python parse_advanced_search.py -h
```

### Company Information

With the identifier of each company, it is possible to extract their information HTML, as dollows:

```Python
python company_info.py -h
```

### Parse Company Information

Finally, all companies HTML will be dumped to `companies/` folder. One can use the following script to parse their information into a readable CSV:

```Python
python parse_company_info.py -h
```

### Bash Script

Instead of invoking every script to conduct the automation, it is also possible to use the provided shell script, as follows:

```Bash
./pipeline.sh
```

Such a script will conduct every step needed to accomplish the automation process. Furthermore, one can change any input argument that is defined in the script.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository.

---
