# `newsreader-cli`

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/meobilivang/Phase-1-Training-VTDT-VTNET/blob/master/LICENSE)

## :book: Description

A simple CLI app to read articles from `Vnexpress` - ranking the most popular Vietnamese online newspaper.

## :dart: Why this app?

- First thing first, a great chance to brush up my programming skills in general and my Python in specific.
- I really want to read news in a cooler way. Who needs a smart phone/web browser? Now I can legitly read news during class on Terminal and people will think that I am hacking into `NASA` :technologist:.

## :gear: Tech Stack

- Programming Language: Python :snake:
- :scroll: Libs: 
    - Web Scraper: [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - Testing: [PyTest](https://docs.pytest.org/en/6.2.x/)
- :delivery: Continuous Integration: [Travis](https://docs.travis-ci.com/)

## :question: How to run the application ?

> Before starting, ensure that Python >= 3 has been installed on your system.

1. Clone the repository

```bash
$ git clone https://github.com/meobilivang/newsreader-cli
```

2. Navigate to application's directory

```
$ cd <path>/newsreader-cli
```

3. Install packages via `pip`

> Use `virtual environment` if you prefer

```bash
$ pip install -r requirements.txt
```

4. Run application!

```bash
$ python -m newsreadercli/app.py
```

## :file_folder: What to do next ?

- [ ] Add specific/advanced test cases
- [ ] Code refactor + reformatting (*Pardon me for my hideous code* :pleading_face:)
- [ ] Add comments