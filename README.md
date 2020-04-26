This work is based on this repo: https://github.com/karpathy/char-rnn

Requirements not stated in the setup.py

- Docker

For using GPU's when generating tweets, you also need:

- nvidia driver >= 418
- nvidia-docker v2

Install:
```
pip install .
```

Run:
```
$ python
Python 3.8.2 (default, Mar 26 2020, 15:53:00) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import trumptweeter
>>> trumptweeter.fetch_tweet("MAKEAMERICAGREATAGAIN!")
'@Markerandon: @realDonaldTrump @realDonaldTrump @realDonaldTrump @realDonaldTrump is the best the best start the truth in the the start that it would be a great than the control the country and the only best the problems to the problems of the problems in the best start and the\n'
```
