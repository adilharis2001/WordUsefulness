# Is This Word Worth Remembering?

For those preparing for standardized tests like the GRE or TOEFL, cramming up thousands of English words is a part of the tall order of test prep. Having gone through this idiotic experience more than a few times, I decided to make a small tool to measure whether a given set of words are worth remembering in the long run.

The tool makes use of [Google NGrams](https://books.google.com/ngrams) and measures two factors
1. **The frequency of the word** as of the year 2008 (As measured by NGrams as a percentage of occurrences of the word in all text of Google Books)
2. **The percentage increase or decrease in usage of word** between the years 1900-2008 as measured by my version of calculating the slope of a non-linear line

Both the above numbers are absurdly small for each word, hence I've multiplied them by 10^8 to make them more human readable. Suggestions for improving on this idea are always welcome. 

## Installation

The above tool is coded to work on Python 2.x. Install XlsxWriter

```bash
pip install XlsxWriter
```
Done! You're good to go.

## Usage
Update the words you wish to obtain the ratings for in textfile words.txt

Run the following command to generate the required xlsx file

```bash
python ngramscraper.py
```
A randomized 10-second pause is implemented between queries to avoid stepping over google API thresholds. Hence longer word lists may run to a few hours.

## Interpretation

The generated xlsx file will feature two columns for the frequency of the word (as of 2008) and the percentage increase/decrease of usage of a given word (between 1900-2008). We can safely assume that words which have high positive values for both frequency or percentage increases are well worth remembering.

In this repository, I have attached a sample xlsx file that I manually prepared while querying through the Barron 1100 GRE word list.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits
Cheers to the creator of the original [NGramScraper.py](https://github.com/jbowens/google-ngrams-scraper/blob/master/NgramScraper.py)


## Contact
[Adil Haris](http://www.consultmelive.com)
